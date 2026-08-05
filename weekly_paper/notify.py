from __future__ import annotations

import argparse
import json
import os
from datetime import date
from pathlib import Path

import requests
from dotenv import load_dotenv

from .pipeline import load_config
from .render import render_wecom
from .storage import load_papers, load_weeks
from .utils import edition_week_id, now_utc_iso, read_json, write_json
from .wecom import send_wecom


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Send an already-generated weekly briefing")
    parser.add_argument("--config", type=Path, default=ROOT / "config" / "config.example.yaml")
    parser.add_argument("--reference-date", type=date.fromisoformat, default=date.today())
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--skip-health-check", action="store_true")
    args = parser.parse_args()
    load_dotenv(ROOT / ".env")
    config = load_config(args.config)
    webhook = os.getenv("WECOM_WEBHOOK_URL", "").strip()
    if not webhook:
        print(json.dumps({"ok": True, "sent": False, "skipped": "missing WECOM_WEBHOOK_URL"}))
        return 0

    current_week = edition_week_id(args.reference_date)
    week = next((item for item in load_weeks(ROOT) if item.get("week") == current_week), None)
    if not week:
        print(json.dumps({"ok": False, "error": f"missing generated week {current_week}"}, ensure_ascii=False))
        return 2
    by_id = load_papers(ROOT)
    featured = [by_id[identifier] for identifier in week["featured_ids"] if identifier in by_id]
    if not featured:
        print(json.dumps({"ok": False, "error": "no featured papers qualified"}, ensure_ascii=False))
        return 3
    incomplete = [paper.id for paper in featured if not paper.summary_zh or not paper.why_it_matters_zh]
    if incomplete:
        print(json.dumps({"ok": False, "error": f"{len(incomplete)} featured papers lack Chinese editorial content"}, ensure_ascii=False))
        return 4

    week_url = f"{config['site']['production_url'].rstrip('/')}/weekly/{current_week.lower()}/"
    if not args.skip_health_check:
        response = requests.get(week_url, timeout=int(config["request_timeout_seconds"]))
        if response.status_code != 200:
            print(json.dumps({"ok": False, "error": f"site health check returned {response.status_code}"}))
            return 5
        digest_marker = week["digest"][:12]
        if digest_marker not in response.text:
            print(
                json.dumps(
                    {"ok": False, "error": f"site is stale; missing digest {digest_marker}"},
                    ensure_ascii=False,
                )
            )
            return 6

    deliveries_path = ROOT / "data" / "state" / "deliveries.json"
    deliveries = read_json(deliveries_path, {})
    if deliveries.get(current_week, {}).get("digest") == week["digest"] and not args.force:
        print(json.dumps({"ok": True, "sent": False, "skipped": "already delivered"}))
        return 0
    send_wecom(render_wecom(current_week, featured, config["site"]["production_url"]), config)
    deliveries[current_week] = {"digest": week["digest"], "sent_at": now_utc_iso()}
    write_json(deliveries_path, deliveries)
    print(json.dumps({"ok": True, "sent": True, "week": current_week}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
