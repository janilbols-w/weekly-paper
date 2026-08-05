from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml

from .collectors import (
    collect_arxiv,
    collect_arxiv_rss,
    collect_openalex,
    collect_openreview,
    collect_rss_sources,
)
from .dedupe import deduplicate
from .editorial import enrich_with_llm
from .evaluation import evaluate, select_featured
from .models import Paper
from .pdf_reader import extract_targeted_context
from .render import render_weekly_report, render_wecom
from .sitegen import build_site_data
from .storage import load_papers, load_weeks, save_papers, save_week
from .taxonomy import load_taxonomy
from .utils import edition_bounds, edition_week_id, now_utc_iso, read_json, stable_digest, write_json
from .wecom import send_wecom


def load_config(path: Path) -> Dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _collect(
    config: Dict[str, Any],
    start_date: date,
    end_date: date,
    skip_arxiv: bool,
    skip_openreview: bool,
) -> Tuple[List[Paper], List[str]]:
    jobs = [
        ("arxiv-rss", collect_arxiv_rss, config["arxiv_rss"]),
        ("openalex", collect_openalex, config["openalex"]),
        ("rss", collect_rss_sources, config.get("rss_sources", [])),
    ]
    if not skip_arxiv:
        jobs.append(("arxiv", collect_arxiv, config["arxiv"]))
    if not skip_openreview:
        jobs.append(("openreview", collect_openreview, config["openreview"]))
    papers: List[Paper] = []
    errors: List[str] = []
    with ThreadPoolExecutor(max_workers=len(jobs)) as pool:
        futures = {
            pool.submit(function, source_config, config, start_date, end_date): name
            for name, function, source_config in jobs
        }
        for future in as_completed(futures):
            name = futures[future]
            try:
                result, source_errors = future.result()
                papers.extend(result)
                errors.extend(source_errors)
            except Exception as exc:
                errors.append(f"{name}: {type(exc).__name__}: {exc}")
    return papers, errors


def _targeted_contexts(
    papers: List[Paper], config: Dict[str, Any], enabled: bool
) -> Tuple[List[Tuple[Paper, str]], List[str]]:
    if not enabled or not papers:
        return [(paper, "") for paper in papers], []
    results: Dict[str, str] = {}
    errors: List[str] = []
    with ThreadPoolExecutor(max_workers=min(4, len(papers))) as pool:
        futures = {pool.submit(extract_targeted_context, paper, config): paper for paper in papers}
        for future in as_completed(futures):
            paper = futures[future]
            try:
                context, depth = future.result()
                results[paper.id] = context
                paper.reading_depth = depth
            except Exception as exc:
                errors.append(f"PDF/{paper.id}: {type(exc).__name__}: {exc}")
    return [(paper, results.get(paper.id, "")) for paper in papers], errors


def _fixture_papers(path: Path) -> List[Paper]:
    value = read_json(path, [])
    if isinstance(value, dict):
        value = value.get("papers", [])
    return [Paper.from_dict(item) for item in value]


def run(
    root: Path,
    config_path: Path,
    taxonomy_path: Path,
    reference_date: date,
    weeks_back: int = 1,
    fixture_path: Path = None,
    skip_arxiv: bool = False,
    skip_openreview: bool = False,
    skip_pdf: bool = False,
    send: bool = False,
    force_send: bool = False,
) -> Dict[str, Any]:
    config = load_config(config_path)
    taxonomy = load_taxonomy(str(taxonomy_path))
    start_date = reference_date - timedelta(days=max(1, weeks_back) * 7 - 1)

    if fixture_path:
        collected = _fixture_papers(fixture_path)
        errors: List[str] = []
    else:
        collected, errors = _collect(config, start_date, reference_date, skip_arxiv, skip_openreview)

    existing = load_papers(root)
    merged = deduplicate(list(existing.values()) + collected)
    timestamp = now_utc_iso()
    for paper in merged:
        old = existing.get(paper.id)
        paper.first_seen = (old.first_seen if old else paper.first_seen) or timestamp
        paper.last_seen = timestamp
        evaluate(paper, taxonomy)

    metadata_max_score = max((paper.score for paper in merged), default=0)

    relevant = [paper for paper in merged if paper.score >= int(config["archive_threshold"])]
    period_papers = [paper for paper in relevant if start_date.isoformat() <= paper.published <= reference_date.isoformat()]
    period_papers.sort(key=lambda item: (item.score, item.published), reverse=True)
    shortlist_limit = int(config["shortlist_size"]) * max(1, weeks_back)
    shortlist = period_papers[:shortlist_limit]

    use_pdf = bool(os.getenv("OPENAI_API_KEY", "").strip()) and not skip_pdf
    editorial_inputs, pdf_errors = _targeted_contexts(shortlist, config, use_pdf)
    errors.extend(pdf_errors)
    errors.extend(enrich_with_llm(editorial_inputs, taxonomy))

    # Scores may have changed after editorial enrichment.
    relevant = [paper for paper in merged if paper.score >= int(config["archive_threshold"])]
    save_papers(root, relevant)

    by_week: Dict[str, List[Paper]] = {}
    for paper in relevant:
        if start_date.isoformat() <= paper.published <= reference_date.isoformat():
            by_week.setdefault(edition_week_id(paper.published), []).append(paper)

    generated_weeks: List[dict] = []
    for week in sorted(by_week):
        papers = sorted(by_week[week], key=lambda item: (item.score, item.published), reverse=True)
        featured = select_featured(
            papers,
            top_n=int(config["top_n"]),
            feature_threshold=int(config["feature_threshold"]),
            max_same_leaf=int(config["max_same_leaf"]),
        )
        for paper in featured:
            if week not in paper.featured_weeks:
                paper.featured_weeks.append(week)
        edition_start, edition_end = edition_bounds(week)
        week_value = {
            "week": week,
            "start_date": edition_start,
            "end_date": edition_end,
            "paper_ids": [paper.id for paper in papers],
            "featured_ids": [paper.id for paper in featured],
            "digest": stable_digest([paper.id for paper in featured]),
            "generated_at": timestamp,
            "source_errors": len(errors),
        }
        save_week(root, week_value)
        report = render_weekly_report(week, papers, featured, week_value)
        report_path = root / "reports" / f"{week}.md"
        report_path.write_text(report, encoding="utf-8")
        generated_weeks.append(week_value)

    # Persist featured week flags added above.
    save_papers(root, relevant)
    all_weeks = load_weeks(root)
    build_site_data(root, relevant, all_weeks, taxonomy)

    sent = False
    current_week = edition_week_id(reference_date)
    if send:
        current = next((value for value in all_weeks if value.get("week") == current_week), None)
        if not current:
            raise ValueError(f"no generated briefing exists for {current_week}")
        by_id = {paper.id: paper for paper in relevant}
        featured = [by_id[paper_id] for paper_id in current["featured_ids"] if paper_id in by_id]
        incomplete = [paper.id for paper in featured if not paper.summary_zh or not paper.why_it_matters_zh]
        if incomplete:
            raise ValueError(f"delivery blocked: {len(incomplete)} featured papers lack Chinese editorial content")
        deliveries_path = root / "data" / "state" / "deliveries.json"
        deliveries = read_json(deliveries_path, {})
        digest = current["digest"]
        if deliveries.get(current_week, {}).get("digest") == digest and not force_send:
            pass
        else:
            message = render_wecom(current_week, featured, config["site"]["production_url"])
            send_wecom(message, config)
            deliveries[current_week] = {"digest": digest, "sent_at": timestamp}
            write_json(deliveries_path, deliveries)
            sent = True

    summary = {
        "reference_date": reference_date.isoformat(),
        "start_date": start_date.isoformat(),
        "collected": len(collected),
        "classified": sum(bool(paper.primary_category) for paper in merged),
        "max_metadata_score": metadata_max_score,
        "relevant_total": len(relevant),
        "generated_weeks": [value["week"] for value in generated_weeks],
        "source_errors": len(errors),
        "errors": errors,
        "sent": sent,
    }
    write_json(root / "data" / "state" / "last-run.json", summary)
    return summary
