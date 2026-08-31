from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import Any, Dict, List, Tuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

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


def _usenix_authors(container: Tag | None) -> List[str]:
    if container is None:
        return []
    paragraph = container.find("p")
    if paragraph is None:
        return []
    authors: List[str] = []
    for child in paragraph.children:
        if isinstance(child, Tag):
            continue
        value = clean_text(str(child)).strip(" ;,")
        if not value:
            continue
        value = value.replace(", and ", ", ").replace(" and ", ", ")
        authors.extend(part.strip() for part in value.split(",") if part.strip())
    return authors


def parse_usenix_schedule_html(payload: bytes, event: Dict[str, Any]) -> Tuple[List[EventPaper], int]:
    soup = BeautifulSoup(payload, "html.parser")
    base_url = str(event["official_url"])
    publication_date = str(event.get("publication_date", event["start_date"]))
    excluded = set(event.get("exclude_presentations", ["keynote"]))
    pdf_template = str(event.get("pdf_url_template", ""))
    output: List[EventPaper] = []

    for article in soup.select("article.node-paper.view-mode-schedule"):
        title_link = article.select_one('h2 a[href*="/presentation/"]')
        if title_link is None:
            continue
        href = str(title_link.get("href", ""))
        slug = href.rstrip("/").rsplit("/", 1)[-1]
        if not slug or slug in excluded:
            continue

        description = article.select_one(".field-name-field-paper-description-long")
        abstract = clean_text(description.get_text(" ", strip=True)) if description else ""
        if not abstract:
            continue
        people = article.select_one(".field-name-field-paper-people-text")
        session = article.find_parent("article", class_="node-session")
        session_title = ""
        if session is not None:
            heading = session.select_one("h2.node-title") or session.find("h2")
            session_title = clean_text(heading.get_text(" ", strip=True)) if heading else ""
        operational = article.select_one(".field-name-field-paper-sub-type") is not None
        track = session_title + (" · Operational Systems" if operational else "")

        awards: List[str] = []
        people_text = clean_text(people.get_text(" ", strip=True)) if people else ""
        if "Awarded Best Paper" in people_text:
            awards.append("Jay Lepreau Best Paper Award")
        if "Distinguished Artifact Award Winner" in people_text:
            awards.append("Distinguished Artifact Award")

        code_url = ""
        for link in article.select('a[href*="github.com/"]'):
            code_url = str(link.get("href", "")).strip()
            if code_url:
                break
        url = urljoin(base_url, href)
        pdf_url = pdf_template.format(slug=slug) if pdf_template else url
        paper = Paper(
            id=f"usenix:{event['id']}:{slug}",
            title=clean_text(title_link.get_text(" ", strip=True)),
            abstract=abstract,
            url=url,
            pdf_url=pdf_url,
            published=publication_date,
            updated=publication_date,
            authors=_usenix_authors(people),
            source="USENIX",
            source_type="proceedings",
            venue=event["short_name"],
            code_url=code_url,
            source_records=[{"source": "USENIX", "id": slug, "url": url}],
        )
        output.append(
            EventPaper(
                paper=paper,
                event_id=event["id"],
                track=track,
                awards=awards,
                presentation="Operational Systems Paper" if operational else "Research Paper",
            )
        )
    return output, len(output)


def collect_usenix_schedule(event: Dict[str, Any], timeout: int = 90) -> Tuple[List[EventPaper], int]:
    response = requests.get(
        event["technical_sessions_url"],
        timeout=timeout,
        headers={"User-Agent": "WeeklyPaper/0.2 (+https://github.com/janilbols-w/weekly-paper)"},
    )
    response.raise_for_status()
    return parse_usenix_schedule_html(response.content, event)
