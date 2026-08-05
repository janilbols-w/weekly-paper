from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List

from .models import Paper


@dataclass
class EventPaper:
    paper: Paper
    event_id: str
    track: str = ""
    presentation: str = ""
    awards: List[str] = field(default_factory=list)
    selected: bool = False
    selection_reason_zh: str = ""
    event_score_evidence: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        value = asdict(self)
        value["paper"] = self.paper.to_dict()
        return value

    @classmethod
    def from_dict(cls, value: Dict[str, Any]) -> "EventPaper":
        fields = cls.__dataclass_fields__
        payload = {key: val for key, val in value.items() if key in fields and key != "paper"}
        return cls(paper=Paper.from_dict(value.get("paper", {})), **payload)
