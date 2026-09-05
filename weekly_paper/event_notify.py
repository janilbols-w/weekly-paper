from __future__ import annotations

import argparse
import json
import os
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv

from .event_models import EventPaper
from .notify import not_ready, site_readiness_error
from .pipeline import load_config
from .render import render_event_wecom
from .utils import now_utc_iso, read_json, write_json
from .wecom import send_wecom, split_markdown


ROOT = Path(__file__).resolve().parents[1]


def _generated_date(value: Any) -> date:
    return date.fromisoformat(str(value).split("T", 1)[0])


def select_delivery_event(
    root: Path,
    event_id: Optional[str],
    reference_date: date,
    max_age_days: int,
) -> Optional[dict[str, Any]]:
    if event_id:
        event = read_json(root / "data" / "events" / event_id / "event.json", {})
        return event or None

    runs = read_json(root / "data" / "state" / "event-runs.json", {})
    if not runs:
        return None
    run_key, latest = max(runs.items(), key=lambda item: str(item[1].get("generated_at", "")))
    latest_event_id = run_key.rsplit(":", 1)[0]
    event = read_json(root / "data" / "events" / latest_event_id / "event.json", {})
    if not event or not event.get("generated_at"):
        return None
    if _generated_date(event["generated_at"]) < reference_date - timedelta(days=max_age_days):
        return None
    if latest.get("digest") != event.get("source_digest"):
        return None
    return event


def main() -> int:
    parser = argparse.ArgumentParser(description="Send a published conference/event briefing")
    parser.add_argument("--config", type=Path, default=ROOT / "config" / "config.example.yaml")
    parser.add_argument("--event", help="Explicit event id; otherwise use the most recently generated event")
    parser.add_argument("--reference-date", type=date.fromisoformat, default=date.today())
    parser.add_argument("--max-age-days", type=int, default=7)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Validate and render without posting to WeCom")
    parser.add_argument("--skip-health-check", action="store_true")
    parser.add_argument("--allow-not-ready", action="store_true")
    parser.add_argument("--health-check-attempts", type=int, default=1)
    parser.add_argument("--health-check-interval-seconds", type=float, default=0)
    args = parser.parse_args()

    load_dotenv(ROOT / ".env")
    config = load_config(args.config)
    webhook = os.getenv("WECOM_WEBHOOK_URL", "").strip()
    if not webhook and not args.dry_run:
        print(json.dumps({"ok": False, "sent": False, "error": "missing WECOM_WEBHOOK_URL"}))
        return 7

    event = select_delivery_event(ROOT, args.event, args.reference_date, args.max_age_days)
    if not event:
        return not_ready("no recent generated event briefing", 2, args.allow_not_ready)

    digest = str(event.get("source_digest", ""))
    if not digest:
        return not_ready("event briefing has no source digest", 3, args.allow_not_ready)
    delivery_key = f"{event['id']}:{event.get('trigger_type', 'update')}"
    deliveries_path = ROOT / "data" / "state" / "event-deliveries.json"
    deliveries = read_json(deliveries_path, {})
    if deliveries.get(delivery_key, {}).get("digest") == digest and not args.force:
        print(json.dumps({"ok": True, "sent": False, "skipped": "already delivered", "event": event["id"]}))
        return 0

    event_url = f"{config['site']['production_url'].rstrip('/')}/events/{event['id']}/"
    if not args.skip_health_check:
        readiness_error = site_readiness_error(
            event_url,
            digest,
            int(config["request_timeout_seconds"]),
            attempts=args.health_check_attempts,
            interval_seconds=args.health_check_interval_seconds,
        )
        if readiness_error:
            return not_ready(readiness_error, 6, args.allow_not_ready)

    papers = [
        EventPaper.from_dict(value)
        for value in read_json(ROOT / "data" / "events" / event["id"] / "papers.json", [])
    ]
    message = render_event_wecom(event, papers, config["site"]["production_url"])
    if args.dry_run:
        chunks = split_markdown(message)
        print(
            json.dumps(
                {
                    "ok": True,
                    "sent": False,
                    "dry_run": True,
                    "event": event["id"],
                    "chunks": len(chunks),
                    "bytes": len(message.encode("utf-8")),
                },
                ensure_ascii=False,
            )
        )
        return 0

    try:
        send_wecom(message, config, continuation_label="会议简报续")
    except Exception as exc:
        print(
            json.dumps(
                {"ok": False, "sent": False, "error": f"WeCom event delivery failed: {exc}"},
                ensure_ascii=False,
            )
        )
        return 8

    deliveries[delivery_key] = {"digest": digest, "sent_at": now_utc_iso()}
    write_json(deliveries_path, deliveries)
    print(json.dumps({"ok": True, "sent": True, "event": event["id"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
