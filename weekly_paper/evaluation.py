from __future__ import annotations

import re
from typing import Any, Dict, Iterable, List

from .models import Paper
from .taxonomy import classify


URL_RE = re.compile(r"https?://(?:www\.)?github\.com/[^\s)\],;]+", re.IGNORECASE)
NUMBER_CLAIM_RE = re.compile(
    r"\b(?:\d+(?:\.\d+)?\s*[x×%]|\d+(?:\.\d+)?\s*(?:times|percent))\b", re.IGNORECASE
)


def _count_terms(text: str, terms: Iterable[str]) -> int:
    lower = text.lower()
    return sum(1 for term in terms if term in lower)


def first_sentence(text: str, limit: int = 360) -> str:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return (parts[0] if parts else text).strip()[:limit]


def evaluate(paper: Paper, taxonomy: Dict[str, Any]) -> Paper:
    path, secondary, keyword_evidence, keyword_score = classify(paper, taxonomy)
    if not path:
        paper.score = 0
        return paper
    paper.primary_category = path
    paper.secondary_tags = secondary
    paper.keyword_evidence = keyword_evidence

    text = f"{paper.title} {paper.abstract} {paper.comment} {paper.journal_ref}"
    lower = text.lower()
    code_match = URL_RE.search(text)
    if code_match:
        paper.code_url = code_match.group(0).rstrip(".")

    relevance = min(25, 10 + min(15, keyword_score * 2))
    novelty = min(
        15,
        5 + _count_terms(lower, ["novel", "new approach", "first", "we introduce", "we propose", "unexplored"]),
    )
    rigor = min(
        20,
        5
        + 2
        * _count_terms(
            lower,
            ["evaluate", "evaluation", "experiment", "baseline", "benchmark", "ablation", "workload", "dataset"],
        ),
    )
    impact = min(
        20,
        5
        + 2
        * _count_terms(
            lower,
            ["throughput", "latency", "memory", "cost", "speedup", "utilization", "energy", "scalability"],
        )
        + (3 if NUMBER_CLAIM_RE.search(text) else 0),
    )
    reproducibility = min(
        10,
        2
        + (5 if paper.code_url else 0)
        + _count_terms(lower, ["open source", "artifact", "repository", "reproducible"]),
    )
    credibility = 3
    if paper.venue or paper.journal_ref:
        credibility += 3
    if paper.source == "OpenReview":
        credibility += 2
    if paper.source_type == "discovery":
        credibility = max(0, credibility - 3)
    credibility = min(10, credibility)

    components = {
        "relevance": relevance,
        "novelty": novelty,
        "rigor": rigor,
        "practical_impact": impact,
        "reproducibility": reproducibility,
        "credibility": credibility,
    }
    paper.score_components = components
    paper.score = sum(components.values())
    paper.score_evidence = [
        f"taxonomy keywords: {', '.join(keyword_evidence[:8])}",
        "quantitative claim detected" if NUMBER_CLAIM_RE.search(text) else "no quantitative claim in metadata",
        "code/artifact link detected" if paper.code_url else "no code link detected in metadata",
    ]
    paper.summary_en = first_sentence(paper.abstract)
    return paper


def select_featured(
    papers: List[Paper], top_n: int, feature_threshold: int, max_same_leaf: int
) -> List[Paper]:
    eligible = sorted(
        [paper for paper in papers if paper.score >= feature_threshold],
        key=lambda item: (item.score, bool(item.code_url), item.updated),
        reverse=True,
    )
    selected: List[Paper] = []
    leaf_counts: Dict[str, int] = {}
    domain_counts: Dict[str, int] = {}

    # First pass encourages both top-level domains when qualified candidates exist.
    domains = sorted({paper.primary_category.get("domain_id", "") for paper in eligible})
    for domain in domains:
        candidate = next((paper for paper in eligible if paper.primary_category.get("domain_id") == domain), None)
        if candidate and len(selected) < top_n:
            selected.append(candidate)
            leaf = candidate.primary_category.get("leaf_id", "")
            leaf_counts[leaf] = leaf_counts.get(leaf, 0) + 1
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

    for paper in eligible:
        if paper in selected or len(selected) >= top_n:
            continue
        leaf = paper.primary_category.get("leaf_id", "")
        if leaf_counts.get(leaf, 0) >= max_same_leaf:
            continue
        selected.append(paper)
        leaf_counts[leaf] = leaf_counts.get(leaf, 0) + 1
        domain = paper.primary_category.get("domain_id", "")
        domain_counts[domain] = domain_counts.get(domain, 0) + 1
    return selected
