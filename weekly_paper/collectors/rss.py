from __future__ import annotations

import calendar
from datetime import date, datetime, timezone
from typing import Any, Dict, List, Tuple

import feedparser
import requests

from ..models import Paper
from ..utils import canonical_url, clean_text, normalized_title


def _published(entry: Any) -> str:
    struct = entry.get("published_parsed") or entry.get("updated_parsed")
    if struct:
        return datetime.fromtimestamp(calendar.timegm(struct), tz=timezone.utc).date().isoformat()
    return "1970-01-01"


def collect_rss_sources(
    sources: List[Dict[str, Any]],
    global_config: Dict[str, Any],
    start_date: date,
    end_date: date,
) -> Tuple[List[Paper], List[str]]:
    papers: List[Paper] = []
    errors: List[str] = []
    headers = {"User-Agent": global_config["user_agent"]}
    for source in sources:
        try:
            response = requests.get(
                source["url"], headers=headers, timeout=int(global_config["request_timeout_seconds"])
            )
            response.raise_for_status()
            parsed = feedparser.parse(response.content)
        except Exception as exc:
            errors.append(f"RSS/{source['name']}: {type(exc).__name__}: {exc}")
            continue
        for entry in parsed.entries:
            published = _published(entry)
            if not (start_date.isoformat() <= published <= end_date.isoformat()):
                continue
            title = clean_text(entry.get("title"), 500)
            url = canonical_url(entry.get("link", ""))
            abstract = clean_text(entry.get("summary") or entry.get("description"), 8000)
            if not title or not url or not abstract:
                continue
            papers.append(
                Paper(
                    id=f"web:{normalized_title(title)[:80]}",
                    title=title,
                    abstract=abstract,
                    url=url,
                    pdf_url="",
                    published=published,
                    updated=published,
                    authors=[],
                    source=source["name"],
                    source_type="discovery",
                    source_records=[{"source": source["name"], "url": url}],
                )
            )
    return papers, errors

