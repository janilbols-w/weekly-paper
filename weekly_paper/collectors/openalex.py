from __future__ import annotations

import os
import re
from datetime import date
from typing import Any, Dict, List, Tuple

import requests

from ..models import Paper
from ..utils import canonical_url, clean_text


ARXIV_RE = re.compile(r"(?:arxiv[./:]|abs/)(\d{4}\.\d{4,5}(?:v\d+)?)", re.IGNORECASE)


def _abstract(inverted_index: Any) -> str:
    if not isinstance(inverted_index, dict):
        return ""
    positioned = []
    for token, positions in inverted_index.items():
        if isinstance(positions, list):
            positioned.extend((int(position), token) for position in positions)
    return clean_text(" ".join(token for _, token in sorted(positioned)), 8000)


def _arxiv_id(work: Dict[str, Any]) -> str:
    candidates = [
        work.get("doi", ""),
        work.get("primary_location", {}).get("landing_page_url", ""),
        work.get("primary_location", {}).get("pdf_url", ""),
    ]
    for value in candidates:
        match = ARXIV_RE.search(value or "")
        if match:
            return match.group(1).split("v", 1)[0]
    return ""


def collect_openalex(
    source_config: Dict[str, Any],
    global_config: Dict[str, Any],
    start_date: date,
    end_date: date,
) -> Tuple[List[Paper], List[str]]:
    """Collect arXiv records through OpenAlex as a resilient discovery path."""
    if not source_config.get("enabled", True):
        return [], []
    api_key = os.getenv("OPENALEX_API_KEY", "").strip()
    if source_config.get("requires_api_key", False) and not api_key:
        return [], []
    papers: List[Paper] = []
    errors: List[str] = []
    headers = {"User-Agent": global_config["user_agent"]}
    filters = ",".join(
        [
            f"from_publication_date:{start_date.isoformat()}",
            f"to_publication_date:{end_date.isoformat()}",
            f"primary_location.source.id:{source_config['arxiv_source_id']}",
        ]
    )
    fields = ",".join(
        [
            "id",
            "doi",
            "title",
            "publication_date",
            "authorships",
            "primary_location",
            "abstract_inverted_index",
            "topics",
        ]
    )
    for query in source_config.get("queries", []):
        try:
            response = requests.get(
                source_config["endpoint"],
                params={
                    "search": query,
                    "filter": filters,
                    "per-page": int(source_config.get("max_results_per_query", 100)),
                    "select": fields,
                    **({"api_key": api_key} if api_key else {}),
                },
                headers=headers,
                timeout=int(global_config["request_timeout_seconds"]),
            )
            response.raise_for_status()
            works = response.json().get("results", [])
        except Exception as exc:
            errors.append(f"OpenAlex/{query}: {type(exc).__name__}: {exc}")
            continue

        for work in works:
            identifier = _arxiv_id(work)
            location = work.get("primary_location") or {}
            abstract = _abstract(work.get("abstract_inverted_index"))
            title = clean_text(work.get("title"), 500)
            if not identifier or not title or not abstract:
                continue
            arxiv_url = f"https://arxiv.org/abs/{identifier}"
            authors = [
                clean_text(item.get("author", {}).get("display_name"), 160)
                for item in work.get("authorships", [])
                if item.get("author", {}).get("display_name")
            ]
            topics = [
                clean_text(item.get("display_name"), 160)
                for item in work.get("topics", [])
                if item.get("display_name")
            ]
            papers.append(
                Paper(
                    id=f"arxiv:{identifier}",
                    title=title,
                    abstract=abstract,
                    url=arxiv_url,
                    pdf_url=canonical_url(location.get("pdf_url") or f"https://arxiv.org/pdf/{identifier}"),
                    published=work.get("publication_date") or start_date.isoformat(),
                    updated=work.get("publication_date") or start_date.isoformat(),
                    authors=authors,
                    source="arXiv via OpenAlex",
                    source_type="preprint",
                    categories=topics,
                    doi=clean_text(work.get("doi"), 200),
                    source_records=[
                        {"source": "arXiv", "id": identifier, "url": arxiv_url},
                        {"source": "OpenAlex", "id": work.get("id", ""), "url": work.get("id", "")},
                    ],
                )
            )
    return papers, errors
