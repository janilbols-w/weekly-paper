from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List


@dataclass
class Paper:
    id: str
    title: str
    abstract: str
    url: str
    pdf_url: str
    published: str
    updated: str
    authors: List[str]
    source: str
    source_type: str
    categories: List[str] = field(default_factory=list)
    doi: str = ""
    venue: str = ""
    journal_ref: str = ""
    comment: str = ""
    code_url: str = ""
    primary_category: Dict[str, str] = field(default_factory=dict)
    secondary_tags: List[str] = field(default_factory=list)
    keyword_evidence: List[str] = field(default_factory=list)
    score: int = 0
    score_components: Dict[str, int] = field(default_factory=dict)
    score_evidence: List[str] = field(default_factory=list)
    summary_en: str = ""
    summary_zh: str = ""
    why_it_matters_zh: str = ""
    limitations_zh: str = ""
    reading_depth: str = "metadata"
    first_seen: str = ""
    last_seen: str = ""
    featured_weeks: List[str] = field(default_factory=list)
    source_records: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, value: Dict[str, Any]) -> "Paper":
        fields = cls.__dataclass_fields__
        return cls(**{key: val for key, val in value.items() if key in fields})

