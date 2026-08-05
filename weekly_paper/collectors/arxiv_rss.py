from __future__ import annotations

import calendar
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timezone
from typing import Any, Dict, List, Tuple

import feedparser
import requests

from ..models import Paper
from ..utils import canonical_url, clean_text


ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
ABSTRACT_RE = re.compile(r"\bAbstract:\s*(.*)", re.IGNORECASE | re.DOTALL)


def _published(entry: Any) -> str:
    struct = entry.get("published_parsed") or entry.get("updated_parsed")
    if struct:
        return datetime.fromtimestamp(calendar.timegm(struct), tz=timezone.utc).date().isoformat()
    return "1970-01-01"


def _fetch_category(
    category: str,
    source_config: Dict[str, Any],
    global_config: Dict[str, Any],
    start_date: date,
    end_date: date,
) -> Tuple[List[Paper], List[str]]:
    url = source_config["url_template"].format(category=category)
    try:
        response = requests.get(
            url,
            headers={"User-Agent": global_config["user_agent"]},
            timeout=int(global_config["request_timeout_seconds"]),
        )
        response.raise_for_status()
        parsed = feedparser.parse(response.content)
    except Exception as exc:
        return [], [f"arXiv RSS/{category}: {type(exc).__name__}: {exc}"]

    papers: List[Paper] = []
    for entry in parsed.entries:
        published = _published(entry)
        if not (start_date.isoformat() <= published <= end_date.isoformat()):
            continue
        url = canonical_url(entry.get("link", ""))
        match = ARXIV_ID_RE.search(url)
        description = clean_text(entry.get("summary") or entry.get("description"), 10000)
        abstract_match = ABSTRACT_RE.search(description)
        abstract = clean_text(abstract_match.group(1) if abstract_match else description, 8000)
        title = clean_text(entry.get("title"), 500)
        if not match or not title or not abstract:
            continue
        identifier = match.group(1)
        creator = clean_text(entry.get("dc_creator") or entry.get("author"), 2000)
        authors = [name.strip() for name in creator.split(",") if name.strip()]
        categories = [tag.get("term", "") for tag in entry.get("tags", []) if tag.get("term")]
        papers.append(
            Paper(
                id=f"arxiv:{identifier}",
                title=title,
                abstract=abstract,
                url=f"https://arxiv.org/abs/{identifier}",
                pdf_url=f"https://arxiv.org/pdf/{identifier}",
                published=published,
                updated=published,
                authors=authors,
                source="arXiv RSS",
                source_type="preprint",
                categories=categories,
                source_records=[{"source": "arXiv RSS", "id": identifier, "url": url}],
            )
        )
    return papers, []


def collect_arxiv_rss(
    source_config: Dict[str, Any],
    global_config: Dict[str, Any],
    start_date: date,
    end_date: date,
) -> Tuple[List[Paper], List[str]]:
    """Collect the latest official arXiv announcement feeds by category."""
    if not source_config.get("enabled", True):
        return [], []
    papers: List[Paper] = []
    errors: List[str] = []
    categories = source_config.get("categories", [])
    with ThreadPoolExecutor(max_workers=min(6, len(categories) or 1)) as pool:
        futures = {
            pool.submit(
                _fetch_category, category, source_config, global_config, start_date, end_date
            ): category
            for category in categories
        }
        for future in as_completed(futures):
            category_papers, category_errors = future.result()
            papers.extend(category_papers)
            errors.extend(category_errors)
    return papers, errors
