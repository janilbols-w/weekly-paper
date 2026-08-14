from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from .event_pipeline import detect_due_events, load_events, run_event
from .event_sitegen import build_event_site


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build independent conference/event paper briefings")
    parser.add_argument("--config", type=Path, default=ROOT / "config" / "events.yaml")
    parser.add_argument("--taxonomy", type=Path, default=ROOT / "config" / "taxonomy.yaml")
    parser.add_argument("--event", help="Event id for an explicit research run")
    parser.add_argument("--scan", action="store_true", help="Run configured events in the event-week window")
    parser.add_argument("--reference-date", type=date.fromisoformat, default=date.today())
    parser.add_argument("--fixture", type=Path, help="Use a local event paper fixture")
    parser.add_argument(
        "--trigger-type",
        choices=(
            "announced",
            "papers_released",
            "program_released",
            "event_week",
            "awards_released",
            "manual_backfill",
        ),
        default="manual_backfill",
        help="Lifecycle trigger recorded for an explicit --event run",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        config = load_events(args.config)
        summaries = []
        if args.event:
            summaries.append(
                run_event(
                    ROOT,
                    args.config,
                    args.taxonomy,
                    args.event,
                    args.reference_date,
                    args.fixture,
                    trigger_type=args.trigger_type,
                )
            )
        elif args.scan:
            for event in detect_due_events(config, args.reference_date):
                if event.get("collector"):
                    summaries.append(
                        run_event(
                            ROOT,
                            args.config,
                            args.taxonomy,
                            event["id"],
                            args.reference_date,
                            trigger_type=event["trigger_type"],
                        )
                    )
            build_event_site(ROOT, config.get("events", []))
        else:
            build_event_site(ROOT, config.get("events", []))
        print(json.dumps({"ok": True, "events": summaries}, ensure_ascii=False))
        return 0
    except Exception as exc:
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
