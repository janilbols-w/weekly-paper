from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

from .pipeline import run


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the weekly LLM inference and AI infra paper briefing")
    parser.add_argument("--config", type=Path, default=ROOT / "config" / "config.example.yaml")
    parser.add_argument("--taxonomy", type=Path, default=ROOT / "config" / "taxonomy.yaml")
    parser.add_argument("--reference-date", type=date.fromisoformat, default=date.today())
    parser.add_argument("--weeks-back", type=int, default=1)
    parser.add_argument("--fixture", type=Path, help="Use a local JSON fixture instead of network collectors")
    parser.add_argument("--skip-arxiv", action="store_true")
    parser.add_argument("--skip-openreview", action="store_true")
    parser.add_argument("--skip-pdf", action="store_true")
    parser.add_argument("--send", action="store_true")
    parser.add_argument("--force-send", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_dotenv(ROOT / ".env")
    try:
        summary = run(
            root=ROOT,
            config_path=args.config,
            taxonomy_path=args.taxonomy,
            reference_date=args.reference_date,
            weeks_back=max(1, args.weeks_back),
            fixture_path=args.fixture,
            skip_arxiv=args.skip_arxiv,
            skip_openreview=args.skip_openreview,
            skip_pdf=args.skip_pdf,
            send=args.send,
            force_send=args.force_send,
        )
    except Exception as exc:
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}, ensure_ascii=False))
        return 1
    print(json.dumps({"ok": True, **summary}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
