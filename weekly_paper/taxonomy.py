from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any, Dict, Iterable, List, Tuple

import yaml

from .models import Paper


LLM_SCOPE_RE = re.compile(
    r"\b(?:llms?|large language models?|language models?|foundation models?|transformers?|"
    r"generative (?:ai|models?))\b",
    re.IGNORECASE,
)
AI_MODEL_RE = re.compile(
    r"\b(?:machine learning|deep learning|neural networks?|artificial intelligence|ai models?|ml models?)\b",
    re.IGNORECASE,
)
INFERENCE_SYSTEM_RE = re.compile(
    r"\b(?:inference|serving|gpus?|accelerators?|kernels?|quantization)\b", re.IGNORECASE
)
INFRA_SYSTEM_RE = re.compile(
    r"\b(?:inference|serving|training|gpus?|accelerators?|clusters?|distributed|datacenters?|"
    r"checkpoints?|rdma|interconnects?)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Leaf:
    domain_id: str
    domain_name: str
    domain_name_zh: str
    group_id: str
    group_name: str
    group_name_zh: str
    leaf_id: str
    leaf_name: str
    leaf_name_zh: str
    keywords: Tuple[str, ...]

    def path(self) -> Dict[str, str]:
        return {
            "domain_id": self.domain_id,
            "domain": self.domain_name,
            "domain_zh": self.domain_name_zh,
            "group_id": self.group_id,
            "group": self.group_name,
            "group_zh": self.group_name_zh,
            "leaf_id": self.leaf_id,
            "leaf": self.leaf_name,
            "leaf_zh": self.leaf_name_zh,
        }


def load_taxonomy(path: str) -> Dict[str, Any]:
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def iter_leaves(taxonomy: Dict[str, Any]) -> Iterable[Leaf]:
    for domain in taxonomy["domains"]:
        for group in domain["groups"]:
            for leaf in group["leaves"]:
                yield Leaf(
                    domain_id=domain["id"],
                    domain_name=domain["name"],
                    domain_name_zh=domain["name_zh"],
                    group_id=group["id"],
                    group_name=group["name"],
                    group_name_zh=group["name_zh"],
                    leaf_id=leaf["id"],
                    leaf_name=leaf["name"],
                    leaf_name_zh=leaf["name_zh"],
                    keywords=tuple(str(keyword).lower() for keyword in leaf.get("keywords", [])),
                )


def _contains(text: str, keyword: str) -> bool:
    return bool(re.search(rf"(?<!\w){re.escape(keyword)}(?!\w)", text))


def _in_scope(domain_id: str, text: str) -> bool:
    if LLM_SCOPE_RE.search(text):
        return True
    if not AI_MODEL_RE.search(text):
        return False
    if domain_id == "efficient-inference":
        return bool(INFERENCE_SYSTEM_RE.search(text))
    return bool(INFRA_SYSTEM_RE.search(text))


def classify(paper: Paper, taxonomy: Dict[str, Any]) -> Tuple[Dict[str, str], List[str], List[str], int]:
    title = paper.title.lower()
    searchable = f"{paper.title} {paper.abstract} {paper.comment} {' '.join(paper.categories)}".lower()
    scored: List[Tuple[int, Leaf, List[str]]] = []
    for leaf in iter_leaves(taxonomy):
        if not _in_scope(leaf.domain_id, searchable):
            continue
        evidence: List[str] = []
        score = 0
        for keyword in leaf.keywords:
            if _contains(searchable, keyword):
                evidence.append(keyword)
                score += 3 if _contains(title, keyword) else 1
        if score:
            scored.append((score, leaf, evidence))
    if not scored:
        return {}, [], [], 0
    scored.sort(key=lambda item: (-item[0], item[1].leaf_id))
    best_score, best_leaf, evidence = scored[0]
    secondary = [item[1].leaf_id for item in scored[1:5] if item[0] >= max(2, best_score // 3)]
    return best_leaf.path(), secondary, sorted(set(evidence)), best_score
