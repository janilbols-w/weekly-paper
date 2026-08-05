from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Any, Dict, List, Tuple

import requests

from ..models import Paper
from ..utils import canonical_url, clean_text


def _value(content: Dict[str, Any], key: str, default: Any = "") -> Any:
    value = content.get(key, default)
    if isinstance(value, dict) and "value" in value:
        return value["value"]
    return value


def _millis_date(value: Any) -> str:
    try:
        return datetime.fromtimestamp(int(value) / 1000, tz=timezone.utc).date().isoformat()
    except (TypeError, ValueError, OSError):
        return "1970-01-01"


def collect_openreview(
    source_config: Dict[str, Any],
    global_config: Dict[str, Any],
    start_date: date,
    end_date: date,
) -> Tuple[List[Paper], List[str]]:
    """Collect public submission notes for configured OpenReview venues."""
    if not source_config.get("enabled", True):
        return [], []
    papers: List[Paper] = []
    errors: List[str] = []
    headers = {"User-Agent": global_config["user_agent"]}

    for venue in source_config.get("venues", []):
        try:
            response = requests.get(
                source_config["endpoint"],
                params={
                    "domain": venue["id"],
                    "limit": int(source_config.get("max_results_per_venue", 1000)),
                    "details": "replyCount",
                },
                headers=headers,
                timeout=int(global_config["request_timeout_seconds"]),
            )
            response.raise_for_status()
            notes = response.json().get("notes", [])
        except Exception as exc:
            errors.append(f"OpenReview/{venue['name']}: {type(exc).__name__}: {exc}")
            continue

        for note in notes:
            content = note.get("content", {})
            title = clean_text(_value(content, "title"), 500)
            abstract = clean_text(_value(content, "abstract"), 8000)
            authors = _value(content, "authors", [])
            if not title or not abstract or not isinstance(authors, list):
                continue
            published = _millis_date(note.get("pdate") or note.get("cdate"))
            if not (start_date.isoformat() <= published <= end_date.isoformat()):
                continue
            note_id = note.get("id", "")
            forum_id = note.get("forum") or note_id
            url = f"https://openreview.net/forum?id={forum_id}"
            paper = Paper(
                id=f"openreview:{forum_id}",
                title=title,
                abstract=abstract,
                url=canonical_url(url),
                pdf_url=f"https://openreview.net/pdf?id={forum_id}",
                published=published,
                updated=_millis_date(note.get("mdate") or note.get("cdate")),
                authors=[clean_text(name, 160) for name in authors],
                source="OpenReview",
                source_type="conference-submission",
                venue=clean_text(_value(content, "venue") or venue["name"], 300),
                categories=[clean_text(value, 160) for value in (_value(content, "keywords", []) or [])],
                source_records=[{"source": "OpenReview", "id": note_id, "url": url}],
            )
            papers.append(paper)

    return papers, errors

