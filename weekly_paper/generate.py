from __future__ import annotations

import json
from pathlib import Path

from .render import render_weekly_report
from .sitegen import build_site_data
from .storage import load_papers, load_weeks
from .taxonomy import load_taxonomy


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    papers = load_papers(ROOT)
    weeks = load_weeks(ROOT)
    taxonomy = load_taxonomy(str(ROOT / "config" / "taxonomy.yaml"))
    build_site_data(ROOT, list(papers.values()), weeks, taxonomy)
    for week in weeks:
        weekly_papers = [papers[paper_id] for paper_id in week["paper_ids"] if paper_id in papers]
        featured = [papers[paper_id] for paper_id in week["featured_ids"] if paper_id in papers]
        report = render_weekly_report(week["week"], weekly_papers, featured, week)
        (ROOT / "reports" / f"{week['week']}.md").write_text(report, encoding="utf-8")
    print(json.dumps({"ok": True, "papers": len(papers), "weeks": len(weeks)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
