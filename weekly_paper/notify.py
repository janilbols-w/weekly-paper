from __future__ import annotations

import argparse
import json
import os
import time
from datetime import date
from pathlib import Path
from typing import Any, Optional

import requests
from dotenv import load_dotenv

from .pipeline import load_config
from .render import render_wecom
from .storage import load_papers, load_weeks
from .utils import edition_week_id, now_utc_iso, read_json, write_json
from .wecom import send_wecom, split_markdown


ROOT = Path(__file__).resolve().parents[1]


def select_delivery_week(weeks: list[dict[str, Any]], reference_date: date, latest_closed: bool) -> Optional[dict[str, Any]]:
    if not latest_closed:
        current_week = edition_week_id(reference_date)
        return next((item for item in weeks if item.get("week") == current_week), None)
    eligible = [item for item in weeks if str(item.get("end_date", "")) <= reference_date.isoformat()]
    return max(eligible, key=lambda item: str(item.get("end_date", "")), default=None)


def site_readiness_error(
    week_url: str,
    digest: str,
    timeout_seconds: int,
    attempts: int = 1,
    interval_seconds: float = 0,
) -> Optional[str]:
    last_error = "site health check failed"
    for attempt in range(max(1, attempts)):
        try:
            response = requests.get(week_url, timeout=timeout_seconds)
            if response.status_code != 200:
                last_error = f"site health check returned {response.status_code}"
            elif digest[:12] not in response.text:
                last_error = f"site is stale; missing digest {digest[:12]}"
            else:
                return None
        except requests.RequestException as exc:
            last_error = f"site health check failed: {type(exc).__name__}"
        if attempt + 1 < max(1, attempts):
            time.sleep(max(0, interval_seconds))
    return last_error


def not_ready(reason: str, code: int, allow_not_ready: bool) -> int:
    print(
        json.dumps(
            {
                "ok": allow_not_ready,
                "sent": False,
                "skipped": "not ready" if allow_not_ready else None,
                "reason": reason,
                "retryable": True,
            },
            ensure_ascii=False,
        )
    )
    return 0 if allow_not_ready else code


def main() -> int:
    parser = argparse.ArgumentParser(description="Send an already-generated weekly briefing")
    parser.add_argument("--config", type=Path, default=ROOT / "config" / "config.example.yaml")
    parser.add_argument("--reference-date", type=date.fromisoformat, default=date.today())
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Validate and render without posting to WeCom")
    parser.add_argument("--skip-health-check", action="store_true")
    parser.add_argument(
        "--latest-closed-week",
        action="store_true",
        help="Deliver the latest edition whose Friday end date has passed",
    )
    parser.add_argument(
        "--allow-not-ready",
        action="store_true",
        help="Exit successfully when collection, editorial, or Pages deployment is still pending",
    )
    parser.add_argument("--health-check-attempts", type=int, default=1)
    parser.add_argument("--health-check-interval-seconds", type=float, default=0)
    args = parser.parse_args()
    load_dotenv(ROOT / ".env")
    config = load_config(args.config)
    webhook = os.getenv("WECOM_WEBHOOK_URL", "").strip()
    if not webhook and not args.dry_run:
        print(json.dumps({"ok": False, "sent": False, "error": "missing WECOM_WEBHOOK_URL"}))
        return 7

    week = select_delivery_week(load_weeks(ROOT), args.reference_date, args.latest_closed_week)
    if not week:
        return not_ready("missing generated delivery week", 2, args.allow_not_ready)
    current_week = str(week["week"])
    by_id = load_papers(ROOT)
    featured = [by_id[identifier] for identifier in week["featured_ids"] if identifier in by_id]
    if not featured:
        return not_ready("no featured papers qualified", 3, args.allow_not_ready)
    incomplete = [paper.id for paper in featured if not paper.summary_zh or not paper.why_it_matters_zh]
    if incomplete:
        return not_ready(
            f"{len(incomplete)} featured papers lack Chinese editorial content",
            4,
            args.allow_not_ready,
        )

    week_url = f"{config['site']['production_url'].rstrip('/')}/weekly/{current_week.lower()}/"
    if not args.skip_health_check:
        readiness_error = site_readiness_error(
            week_url,
            str(week["digest"]),
            int(config["request_timeout_seconds"]),
            attempts=args.health_check_attempts,
            interval_seconds=args.health_check_interval_seconds,
        )
        if readiness_error:
            return not_ready(readiness_error, 6, args.allow_not_ready)

    deliveries_path = ROOT / "data" / "state" / "deliveries.json"
    deliveries = read_json(deliveries_path, {})
    if deliveries.get(current_week, {}).get("digest") == week["digest"] and not args.force:
        print(json.dumps({"ok": True, "sent": False, "skipped": "already delivered"}))
        return 0
    message = render_wecom(current_week, featured, config["site"]["production_url"])
    if args.dry_run:
        chunks = split_markdown(message)
        print(
            json.dumps(
                {
                    "ok": True,
                    "sent": False,
                    "dry_run": True,
                    "week": current_week,
                    "featured": len(featured),
                    "chunks": len(chunks),
                    "bytes": len(message.encode("utf-8")),
                },
                ensure_ascii=False,
            )
        )
        return 0
    try:
        send_wecom(message, config)
    except Exception as exc:
        print(
            json.dumps(
                {"ok": False, "sent": False, "error": f"WeCom delivery failed: {exc}"},
                ensure_ascii=False,
            )
        )
        return 8
    deliveries[current_week] = {"digest": week["digest"], "sent_at": now_utc_iso()}
    write_json(deliveries_path, deliveries)
    print(json.dumps({"ok": True, "sent": True, "week": current_week}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
