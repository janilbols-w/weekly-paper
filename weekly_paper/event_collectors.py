from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List, Tuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

from .event_models import EventPaper
from .models import Paper
from .utils import clean_text, normalized_title


COLM_ABSTRACT_RECALL_RE = re.compile(
    r"\b(?:inference|serving|latency|throughput|kv[- ]?cache|speculative|quantiz\w*|"
    r"low[- ]?precision|gpu|accelerat\w*|paged[- ]?attention|prefill|decod\w*|distributed|"
    r"sparse[- ]?attention|prun\w*|hardware|memory[- ]?efficient|efficient|efficiency|"
    r"compression|token pruning|model routing|mixture[- ]?of[- ]?experts|moe|"
    r"on[- ]?device|edge device|test[- ]?time compute|compute cost|parallelism)\b",
    re.IGNORECASE,
)


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


def _sosp_authors(node: Tag | None) -> List[str]:
    if node is None:
        return []
    value = clean_text(node.get_text(" ", strip=True))
    value = re.sub(r"\s*\([^)]*\)", "", value)
    value = value.replace(", and ", ", ").replace(" and ", ", ")
    return [part.strip(" ;,") for part in value.split(",") if part.strip(" ;,")]


def parse_sosp_schedule_html(payload: bytes, event: Dict[str, Any]) -> Tuple[List[EventPaper], int]:
    """Parse research-paper rows from the official SOSP schedule.

    The schedule is an accepted-program source, not the archival proceedings: PDF,
    abstract, and code metadata are deliberately left empty for editorial enrichment.
    """
    soup = BeautifulSoup(payload, "html.parser")
    publication_date = str(event.get("program_released_date", event["start_date"]))
    schedule_url = str(event.get("program_url", event["official_url"]))
    accepted_url = str(event.get("accepted_papers_url", schedule_url))
    output: List[EventPaper] = []

    for row in soup.select("tr.session-a, tr.session-b"):
        heading = row.select_one(".session-title")
        # Rows without a research-session heading can contain invited talks that
        # are not part of the conference's accepted-paper corpus.
        if heading is None:
            continue
        track = clean_text(heading.get_text(" ", strip=True))
        track = re.sub(r"^Session\s+\S+\s*[–—-]\s*", "", track, flags=re.IGNORECASE)
        for entry in row.select("ul.papers > li"):
            authors_node = entry.find("em")
            if authors_node is None:
                continue
            paper_link = entry.find(
                "a",
                href=lambda value: bool(value and "dl.acm.org/doi/" in str(value)),
            )
            title_parts: List[str] = []
            for child in entry.children:
                if child is authors_node or (isinstance(child, Tag) and child.find("em")):
                    break
                if isinstance(child, Tag) and child.name == "br":
                    break
                if (
                    isinstance(child, Tag)
                    and child.name == "a"
                    and clean_text(child.get_text(" ", strip=True)).lower() == "paper"
                ):
                    continue
                title_parts.append(child.get_text(" ", strip=True) if isinstance(child, Tag) else str(child))
            title = re.sub(r"\s*\[\s*\]\s*$", "", clean_text(" ".join(title_parts))).strip(" ;")
            if not title:
                continue
            slug = normalized_title(title)[:96]
            paper_url = urljoin(schedule_url, str(paper_link.get("href", ""))) if paper_link else accepted_url
            doi = ""
            if paper_link and "/doi/" in paper_url:
                doi = paper_url.split("/doi/", 1)[1].split("?", 1)[0].strip("/")
            source_records = [
                {"source": "SOSP official program", "id": slug, "url": schedule_url},
                {"source": "SOSP accepted papers", "id": slug, "url": accepted_url},
            ]
            if paper_link:
                source_records.append({"source": "ACM Digital Library", "id": doi, "url": paper_url})
            paper = Paper(
                id=f"sosp:{event['id']}:{slug}",
                title=title,
                abstract="",
                url=paper_url,
                pdf_url="",
                published=publication_date,
                updated=publication_date,
                authors=_sosp_authors(authors_node),
                source="SOSP official program",
                source_type="proceedings" if paper_link else "accepted_program",
                doi=doi,
                venue=event["short_name"],
                source_records=source_records,
            )
            output.append(
                EventPaper(
                    paper=paper,
                    event_id=event["id"],
                    track=track,
                    presentation="Research Paper",
                )
            )
    return output, len(output)


def collect_sosp_schedule(event: Dict[str, Any], timeout: int = 90) -> Tuple[List[EventPaper], int]:
    response = requests.get(
        event["program_url"],
        timeout=timeout,
        headers={"User-Agent": "WeeklyPaper/0.2 (+https://github.com/janilbols-w/weekly-paper)"},
    )
    response.raise_for_status()
    return parse_sosp_schedule_html(response.content, event)


def _colm_authors(node: Tag | None) -> List[str]:
    if node is None:
        return []
    value = clean_text(node.get_text(" ", strip=True))
    return [part.strip() for part in value.split("⋅") if part.strip()]


def parse_colm_accepted_html(
    payload: bytes, event: Dict[str, Any]
) -> Tuple[List[EventPaper], int]:
    """Parse the complete official COLM accepted-paper table.

    The table is the authoritative corpus list. It contains titles, authors, and
    poster scheduling metadata but not abstracts or archival paper links.
    """
    soup = BeautifulSoup(payload, "html.parser")
    accepted_url = str(event["accepted_papers_url"])
    publication_date = str(event.get("publication_date", event["start_date"]))
    output: List[EventPaper] = []
    for row in soup.select("table tr"):
        title_node = row.select_one("td strong")
        if title_node is None:
            continue
        title = clean_text(title_node.get_text(" ", strip=True))
        if not title:
            continue
        slug = normalized_title(title)[:96]
        authors_node = row.select_one("td .indented i")
        where_node = row.select_one("td.elc-where")
        track = clean_text(where_node.get_text(" ", strip=True)) if where_node else ""
        paper = Paper(
            id=f"colm:{event['id']}:{slug}",
            title=title,
            abstract="",
            url=accepted_url,
            pdf_url="",
            published=publication_date,
            updated=publication_date,
            authors=_colm_authors(authors_node),
            source="COLM official accepted papers",
            source_type="accepted_program",
            venue=event["short_name"],
            source_records=[
                {"source": "COLM official accepted papers", "id": slug, "url": accepted_url}
            ],
        )
        output.append(
            EventPaper(
                paper=paper,
                event_id=event["id"],
                track=track,
                presentation="Poster",
            )
        )
    return output, len(output)


def parse_colm_calendar_html(payload: bytes, event: Dict[str, Any]) -> Dict[str, str]:
    soup = BeautifulSoup(payload, "html.parser")
    base_url = str(event["official_url"])
    output: Dict[str, str] = {}
    for link in soup.select('a[href^="/virtual/2026/poster/"]'):
        title = clean_text(link.get_text(" ", strip=True))
        href = str(link.get("href", ""))
        if title and href:
            output[normalized_title(title)] = urljoin(base_url, href)
    return output


def parse_colm_orals_html(payload: bytes, event: Dict[str, Any]) -> Dict[str, Dict[str, str]]:
    soup = BeautifulSoup(payload, "html.parser")
    base_url = str(event["official_url"])
    output: Dict[str, Dict[str, str]] = {}
    for card in soup.select(".event-card"):
        title_link = card.select_one("h3.event-title a")
        if title_link is None:
            continue
        title = clean_text(title_link.get_text(" ", strip=True))
        abstract_node = card.select_one(".event-abstract .abstract-text")
        output[normalized_title(title)] = {
            "url": urljoin(base_url, str(title_link.get("href", ""))),
            "abstract": clean_text(abstract_node.get_text(" ", strip=True)) if abstract_node else "",
        }
    return output


def parse_colm_detail_html(payload: bytes) -> str:
    soup = BeautifulSoup(payload, "html.parser")
    node = soup.select_one(".abstract-section .abstract-text-inner")
    return clean_text(node.get_text(" ", strip=True)) if node else ""


def collect_colm_program(event: Dict[str, Any], timeout: int = 90) -> Tuple[List[EventPaper], int]:
    headers = {"User-Agent": "WeeklyPaper/0.2 (+https://github.com/janilbols-w/weekly-paper)"}

    def fetch(url: str) -> bytes:
        response = requests.get(url, timeout=timeout, headers=headers)
        response.raise_for_status()
        return response.content

    papers, total = parse_colm_accepted_html(fetch(event["accepted_papers_url"]), event)
    calendar = parse_colm_calendar_html(fetch(event["program_url"]), event)
    orals = parse_colm_orals_html(fetch(event["orals_url"]), event)

    candidates: List[EventPaper] = []
    for item in papers:
        key = normalized_title(item.paper.title)
        if key in calendar:
            item.paper.url = calendar[key]
            item.paper.source_records.append(
                {"source": "COLM official program", "id": key, "url": calendar[key]}
            )
        oral = orals.get(key)
        if oral:
            item.paper.url = oral["url"]
            item.paper.abstract = oral["abstract"]
            item.presentation = "Oral + Poster"
            continue
        if item.paper.url != event["accepted_papers_url"] and COLM_ABSTRACT_RECALL_RE.search(
            item.paper.title
        ):
            candidates.append(item)

    max_workers = max(1, int(event.get("detail_fetch_workers", 12)))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch, item.paper.url): item for item in candidates}
        for future in as_completed(futures):
            item = futures[future]
            try:
                item.paper.abstract = parse_colm_detail_html(future.result())
            except requests.RequestException:
                # The complete title-level corpus remains usable when an individual
                # detail page is temporarily unavailable.
                continue
    return papers, total
