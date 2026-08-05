from __future__ import annotations

import calendar
import re
import time
from datetime import date, datetime, time as datetime_time, timezone
from typing import Any, Dict, List, Optional, Tuple

import feedparser
import requests

from ..models import Paper
from ..utils import canonical_url, clean_text, iso_date


ARXIV_ID_RE = re.compile(r"(?:abs/)?([^/]+?)(?:v\d+)?$")


def _entry_datetime(entry: Any, field: str) -> str:
    value = entry.get(f"{field}_parsed")
    if value:
        return datetime.fromtimestamp(calendar.timegm(value), tz=timezone.utc).date().isoformat()
    return iso_date(entry.get(field, ""))


def _arxiv_id(entry_id: str) -> str:
    match = ARXIV_ID_RE.search(entry_id or "")
    return f"arxiv:{match.group(1)}" if match else f"arxiv:{entry_id}"


def _query(config: Dict[str, Any], start_date: date, end_date: date) -> str:
    categories = " OR ".join(f"cat:{category}" for category in config["categories"])
    terms = " OR ".join(f'all:"{term}"' for term in config["query_terms"])
    start = datetime.combine(start_date, datetime_time.min, tzinfo=timezone.utc).strftime("%Y%m%d%H%M")
    end = datetime.combine(end_date, datetime_time.max, tzinfo=timezone.utc).strftime("%Y%m%d%H%M")
    return f"({categories}) AND ({terms}) AND submittedDate:[{start} TO {end}]"


def collect_arxiv(
    source_config: Dict[str, Any],
    global_config: Dict[str, Any],
    start_date: date,
    end_date: date,
) -> Tuple[List[Paper], List[str]]:
    """Collect matching arXiv entries while respecting configured pagination."""
    if not source_config.get("enabled", True):
        return [], []
    papers: List[Paper] = []
    errors: List[str] = []
    offset = 0
    page_size = int(source_config.get("page_size", 200))
    max_results = int(source_config.get("max_results", 1000))
    query = _query(source_config, start_date, end_date)
    session = requests.Session()
    headers = {"User-Agent": global_config["user_agent"]}

    while offset < max_results:
        params = {
            "search_query": query,
            "start": offset,
            "max_results": min(page_size, max_results - offset),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        response = None
        last_error: Optional[Exception] = None
        retry_attempts = int(source_config.get("retry_attempts", 3))
        for attempt in range(retry_attempts):
            try:
                response = session.get(
                    source_config["endpoint"],
                    params=params,
                    headers=headers,
                    timeout=int(
                        source_config.get(
                            "request_timeout_seconds", global_config["request_timeout_seconds"]
                        )
                    ),
                )
                response.raise_for_status()
                if "rate exceeded" in response.text.lower():
                    raise RuntimeError("arXiv rate limit exceeded")
                parsed = feedparser.parse(response.content)
                if getattr(parsed, "bozo", False) and not parsed.entries:
                    raise ValueError(f"invalid Atom response: {parsed.bozo_exception}")
                last_error = None
                break
            except Exception as exc:
                last_error = exc
                if attempt + 1 < retry_attempts:
                    retry_after = response.headers.get("Retry-After", "") if response is not None else ""
                    try:
                        wait_seconds = float(retry_after)
                    except ValueError:
                        wait_seconds = float(source_config.get("retry_backoff_seconds", 10)) * (2**attempt)
                    time.sleep(max(3.0, min(wait_seconds, 60.0)))
        if last_error is not None:
            errors.append(f"arXiv offset={offset}: {type(last_error).__name__}: {last_error}")
            break

        for entry in parsed.entries:
            entry_id = clean_text(entry.get("id"), 300)
            links = {link.get("type", ""): link.get("href", "") for link in entry.get("links", [])}
            authors = [clean_text(author.get("name"), 160) for author in entry.get("authors", [])]
            categories = [tag.get("term", "") for tag in entry.get("tags", []) if tag.get("term")]
            paper = Paper(
                id=_arxiv_id(entry_id),
                title=clean_text(entry.get("title"), 500),
                abstract=clean_text(entry.get("summary"), 8000),
                url=canonical_url(entry_id),
                pdf_url=canonical_url(links.get("application/pdf", "")),
                published=_entry_datetime(entry, "published"),
                updated=_entry_datetime(entry, "updated"),
                authors=authors,
                source="arXiv",
                source_type="preprint",
                categories=categories,
                doi=clean_text(entry.get("arxiv_doi"), 200),
                journal_ref=clean_text(entry.get("arxiv_journal_ref"), 500),
                comment=clean_text(entry.get("arxiv_comment"), 1000),
                source_records=[{"source": "arXiv", "id": entry_id, "url": canonical_url(entry_id)}],
            )
            if paper.title and paper.abstract and paper.url:
                papers.append(paper)

        if len(parsed.entries) < params["max_results"]:
            break
        offset += len(parsed.entries)
        time.sleep(float(source_config.get("request_delay_seconds", 3.0)))

    return papers, errors
