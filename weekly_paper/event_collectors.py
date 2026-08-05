from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import Any, Dict, List, Tuple

import requests

from .event_models import EventPaper
from .models import Paper
from .utils import clean_text


def _text(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return clean_text("".join(node.itertext()))


def _author(node: ET.Element) -> str:
    first = _text(node.find("first"))
    last = _text(node.find("last"))
    name = " ".join(part for part in (first, last) if part)
    return name or _text(node)


def parse_acl_anthology_xml(payload: bytes, event: Dict[str, Any]) -> Tuple[List[EventPaper], int]:
    root = ET.fromstring(payload)
    collection_id = str(root.get("id", "2026.acl"))
    wanted = set(event.get("volumes", []))
    publication_date = str(event.get("publication_date", event["start_date"]))
    output: List[EventPaper] = []
    total = 0
    for volume in root.findall(".//volume"):
        volume_id = str(volume.get("id", ""))
        if wanted and volume_id not in wanted:
            continue
        track = "Findings" if "finding" in collection_id else volume_id.replace("-", " ").title()
        for item in volume.findall("paper"):
            total += 1
            item_id = str(item.get("id", ""))
            anthology_id = f"{collection_id}-{volume_id}.{item_id}"
            url = f"https://aclanthology.org/{anthology_id}/"
            paper = Paper(
                id=f"acl:{anthology_id}",
                title=_text(item.find("title")),
                abstract=_text(item.find("abstract")),
                url=url,
                pdf_url=f"https://aclanthology.org/{anthology_id}.pdf",
                published=publication_date,
                updated=publication_date,
                authors=[_author(author) for author in item.findall("author")],
                source="ACL Anthology",
                source_type="proceedings",
                doi=_text(item.find("doi")),
                venue=event["short_name"],
                source_records=[{"source": "ACL Anthology", "id": anthology_id, "url": url}],
            )
            output.append(EventPaper(paper=paper, event_id=event["id"], track=track))
    return output, total


def collect_acl_anthology(event: Dict[str, Any], timeout: int = 90) -> Tuple[List[EventPaper], int]:
    sources = event.get("anthology_sources") or [
        {"url": event["anthology_xml_url"], "volumes": event.get("volumes", [])}
    ]
    output: List[EventPaper] = []
    total = 0
    for source in sources:
        response = requests.get(
            source["url"],
            timeout=timeout,
            headers={"User-Agent": "WeeklyPaper/0.2 (+https://github.com/janilbols-w/weekly-paper)"},
        )
        response.raise_for_status()
        source_event = dict(event)
        source_event["volumes"] = source.get("volumes", [])
        values, source_total = parse_acl_anthology_xml(response.content, source_event)
        output.extend(values)
        total += source_total
    return output, total
