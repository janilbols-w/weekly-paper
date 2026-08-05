from __future__ import annotations

from typing import Dict, Iterable, List

from .models import Paper
from .utils import normalized_title


def _preferred_id(first: Paper, second: Paper) -> str:
    doi = second.doi or first.doi
    if doi:
        return f"doi:{doi.lower().removeprefix('https://doi.org/')}"
    for candidate in (first.id, second.id):
        if candidate.startswith("arxiv:"):
            return candidate
    return first.id


def merge_paper(target: Paper, incoming: Paper) -> Paper:
    target.id = _preferred_id(target, incoming)
    if incoming.updated >= target.updated:
        for field in ("title", "abstract", "url", "pdf_url", "updated", "comment", "journal_ref"):
            value = getattr(incoming, field)
            if value:
                setattr(target, field, value)
    target.published = min(target.published, incoming.published)
    target.authors = target.authors or incoming.authors
    target.categories = sorted(set(target.categories + incoming.categories))
    target.doi = target.doi or incoming.doi
    target.venue = target.venue or incoming.venue
    target.code_url = target.code_url or incoming.code_url
    target.source_records = target.source_records + [
        item for item in incoming.source_records if item not in target.source_records
    ]
    if incoming.source_type != "discovery":
        target.source = incoming.source
        target.source_type = incoming.source_type
    return target


def deduplicate(papers: Iterable[Paper]) -> List[Paper]:
    by_id: Dict[str, Paper] = {}
    by_title: Dict[str, Paper] = {}
    for paper in sorted(papers, key=lambda item: (item.published, item.updated, item.id)):
        title_key = normalized_title(paper.title)
        existing = by_id.get(paper.id) or by_title.get(title_key)
        if existing:
            old_id = existing.id
            merge_paper(existing, paper)
            if existing.id != old_id:
                by_id.pop(old_id, None)
            by_id[existing.id] = existing
            by_title[title_key] = existing
        else:
            by_id[paper.id] = paper
            by_title[title_key] = paper
    unique: Dict[int, Paper] = {id(paper): paper for paper in by_id.values()}
    return sorted(unique.values(), key=lambda item: (item.published, item.title), reverse=True)

