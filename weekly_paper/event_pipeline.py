from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path
import re
from typing import Any, Dict, List

import yaml

from .evaluation import evaluate
from .event_collectors import collect_acl_anthology
from .event_models import EventPaper
from .event_sitegen import build_event_site
from .models import Paper
from .taxonomy import load_taxonomy
from .utils import now_utc_iso, read_json, stable_digest, write_json


EVENT_SYSTEM_RE = re.compile(
    r"\b(?:inference|serving|time-to-first-token|ttft|latency|throughput|kv[- ]cache|"
    r"speculative decoding|quantization|low[- ]precision|gpu|accelerator|paged attention|"
    r"flashattention|prefill|decode|distributed training|training speedup|training optimization|"
    r"sparse attention|structured pruning|hardware[- ]efficient|edge devices?|memory footprint|"
    r"memory[- ]efficient|compute efficiency|computational cost)\b",
    re.IGNORECASE,
)
EVENT_TITLE_RE = re.compile(
    r"\b(?:inference|serving|time-to-first-token|ttft|latency|throughput|kv[- ]cache|"
    r"speculative decoding|quantization|low[- ]precision|gpu|accelerator|paged attention|"
    r"prefill|distributed training|sparse attention|structured pruning|hardware[- ]efficient|"
    r"memory[- ]efficient)\b",
    re.IGNORECASE,
)


def _in_event_scope(paper: Paper) -> bool:
    if EVENT_TITLE_RE.search(paper.title):
        return True
    signals = {value.lower() for value in EVENT_SYSTEM_RE.findall(f"{paper.title} {paper.abstract}")}
    return len(signals) >= 2


def load_events(path: Path) -> Dict[str, Any]:
    def normalize(value: Any) -> Any:
        if isinstance(value, date):
            return value.isoformat()
        if isinstance(value, dict):
            return {key: normalize(item) for key, item in value.items()}
        if isinstance(value, list):
            return [normalize(item) for item in value]
        return value

    return normalize(yaml.safe_load(path.read_text(encoding="utf-8")))


def detect_due_events(config: Dict[str, Any], reference_date: date) -> List[Dict[str, Any]]:
    window = timedelta(days=int(config.get("scan_window_days", 3)))
    due: List[Dict[str, Any]] = []
    for value in config.get("events", []):
        start = date.fromisoformat(str(value["start_date"]))
        end = date.fromisoformat(str(value["end_date"]))
        if start - window <= reference_date <= end + window:
            event = dict(value)
            event["trigger_type"] = "event_week"
            due.append(event)
    return due


def _fixture_papers(path: Path, event_id: str) -> tuple[List[EventPaper], int]:
    value = read_json(path, {})
    papers: List[EventPaper] = []
    for item in value.get("papers", value if isinstance(value, list) else []):
        if "paper" in item:
            papers.append(EventPaper.from_dict(item))
        else:
            papers.append(EventPaper(paper=Paper.from_dict(item), event_id=event_id, track=item.get("track", "")))
    return papers, int(value.get("corpus_total", len(papers))) if isinstance(value, dict) else len(papers)


def _apply_editorial(root: Path, event_id: str, papers: List[EventPaper]) -> None:
    path = root / "config" / "event_editorial" / f"{event_id}.yaml"
    if not path.exists():
        return
    values = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    for item in papers:
        editorial = values.get(item.paper.id, values.get(item.paper.id.removeprefix("acl:"), {}))
        if not editorial:
            continue
        for field in ("summary_zh", "why_it_matters_zh", "limitations_zh", "code_url", "reading_depth"):
            if field in editorial:
                setattr(item.paper, field, editorial[field])
        if "primary_category" in editorial:
            item.paper.primary_category = editorial["primary_category"]
        item.selection_reason_zh = editorial.get("selection_reason_zh", item.selection_reason_zh)
        item.presentation = editorial.get("presentation", item.presentation)
        item.awards = editorial.get("awards", item.awards)


def _score(papers: List[EventPaper], taxonomy: Dict[str, Any]) -> List[EventPaper]:
    relevant: List[EventPaper] = []
    for item in papers:
        evaluate(item.paper, taxonomy)
        if not item.paper.primary_category:
            continue
        if not _in_event_scope(item.paper):
            continue
        # Official proceedings are stronger evidence than discovery/preprint metadata.
        old = item.paper.score_components.get("credibility", 0)
        item.paper.score_components["credibility"] = min(10, old + 4)
        item.paper.score += item.paper.score_components["credibility"] - old
        item.event_score_evidence.append("official peer-reviewed proceedings")
        relevant.append(item)
    return relevant


def _select(
    papers: List[EventPaper], threshold: int, cap: int, max_same_leaf: int, require_editorial: bool
) -> None:
    counts: Dict[str, int] = {}
    chosen = 0
    for item in sorted(papers, key=lambda value: (value.paper.score, bool(value.paper.code_url)), reverse=True):
        leaf = item.paper.primary_category.get("leaf_id", "")
        complete = bool(
            item.paper.summary_zh and item.paper.why_it_matters_zh and item.paper.limitations_zh
        )
        if (
            item.paper.score < threshold
            or counts.get(leaf, 0) >= max_same_leaf
            or chosen >= cap
            or (require_editorial and not complete)
        ):
            item.selected = False
            continue
        item.selected = True
        counts[leaf] = counts.get(leaf, 0) + 1
        chosen += 1


def _status(event: Dict[str, Any], reference_date: date) -> str:
    start = date.fromisoformat(str(event["start_date"]))
    end = date.fromisoformat(str(event["end_date"]))
    if reference_date < start:
        return "即将举行"
    if reference_date <= end:
        return "进行中"
    return "已归档"


def run_event(
    root: Path,
    config_path: Path,
    taxonomy_path: Path,
    event_id: str,
    reference_date: date,
    fixture_path: Path | None = None,
    trigger_type: str = "manual_backfill",
) -> Dict[str, Any]:
    config = load_events(config_path)
    taxonomy = load_taxonomy(str(taxonomy_path))
    event = next((dict(value) for value in config.get("events", []) if value["id"] == event_id), None)
    if not event:
        raise ValueError(f"unknown event: {event_id}")

    if fixture_path:
        collected, corpus_total = _fixture_papers(fixture_path, event_id)
        corpus_source = "ACL Anthology curated fixture"
    elif event.get("collector") == "acl_anthology_xml":
        collected, corpus_total = collect_acl_anthology(event)
        corpus_source = "ACL Anthology XML"
    elif event.get("collector") == "official_program":
        collected, corpus_total = [], 0
        corpus_source = event.get("program_source_name", "Official program")
    else:
        raise ValueError(f"event {event_id} has no proceedings collector")

    relevant = _score(collected, taxonomy)
    _apply_editorial(root, event_id, relevant)
    _select(
        relevant,
        threshold=int(config.get("selection_threshold", 54)),
        cap=int(config.get("selection_cap", 12)),
        max_same_leaf=int(config.get("max_same_leaf", 2)),
        require_editorial=bool(config.get("selection_requires_editorial", True)),
    )
    timestamp = now_utc_iso()
    digest_value: Any = [item.to_dict() for item in relevant]
    if event.get("collector") == "official_program":
        digest_value = {
            "program_released_date": event.get("program_released_date", ""),
            "event_stats": event.get("event_stats", []),
            "key_programs": event.get("key_programs", []),
            "sources": [
                {key: value for key, value in source.items() if key != "checked_at"}
                for source in event.get("sources", [])
            ],
        }
    digest = stable_digest(digest_value)
    event.update(
        {
            "status": _status(event, reference_date),
            "trigger_type": trigger_type,
            "corpus_source": corpus_source,
            "corpus_total": corpus_total,
            "relevant_total": len(relevant),
            "selected_total": sum(item.selected for item in relevant),
            "source_digest": digest,
            "generated_at": timestamp,
        }
    )
    target = root / "data" / "events" / event_id
    write_json(target / "event.json", event)
    write_json(target / "papers.json", [item.to_dict() for item in relevant])
    runs_path = root / "data" / "state" / "event-runs.json"
    runs = read_json(runs_path, {})
    runs[f"{event_id}:{trigger_type}"] = {"digest": digest, "generated_at": timestamp}
    write_json(runs_path, runs)
    build_event_site(root, config.get("events", []))
    return {
        "event_id": event_id,
        "corpus_total": corpus_total,
        "relevant_total": len(relevant),
        "selected_total": event["selected_total"],
        "digest": digest,
    }
