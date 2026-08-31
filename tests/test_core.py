from __future__ import annotations

import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from weekly_paper.dedupe import deduplicate
from weekly_paper.evaluation import evaluate, select_featured
from weekly_paper.event_collectors import parse_acl_anthology_xml, parse_usenix_schedule_html
from weekly_paper.event_pipeline import _in_event_scope, detect_due_events, load_events, run_event
from weekly_paper.models import Paper
from weekly_paper.pipeline import run
from weekly_paper.storage import save_papers
from weekly_paper.taxonomy import load_taxonomy
from weekly_paper.utils import edition_bounds, edition_week_id
from weekly_paper.wecom import split_markdown


ROOT = Path(__file__).resolve().parents[1]


def paper(identifier: str, title: str, abstract: str) -> Paper:
    return Paper(
        id=identifier,
        title=title,
        abstract=abstract,
        url=f"https://example.com/{identifier}",
        pdf_url="",
        published="2026-08-01",
        updated="2026-08-01",
        authors=["A"],
        source="arXiv",
        source_type="preprint",
    )


class CoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.taxonomy = load_taxonomy(str(ROOT / "config" / "taxonomy.yaml"))

    def test_classification_is_three_level(self) -> None:
        value = paper(
            "arxiv:1",
            "Paged KV Cache for LLM Serving",
            "We evaluate prefix caching and paged attention for model serving benchmarks.",
        )
        evaluate(value, self.taxonomy)
        self.assertEqual(value.primary_category["domain_id"], "efficient-inference")
        self.assertEqual(value.primary_category["group_id"], "runtime-memory")
        self.assertEqual(value.primary_category["leaf_id"], "attention-kv-cache")

    def test_short_keyword_does_not_match_inside_word(self) -> None:
        value = paper(
            "arxiv:word-boundary",
            "Forward Mapping for Conversation Memory",
            "A dialogue method based on forward mapping and conversational context.",
        )
        evaluate(value, self.taxonomy)
        self.assertNotEqual(value.primary_category.get("leaf_id"), "network-interconnect")

    def test_generic_compression_is_outside_llm_inference_scope(self) -> None:
        value = paper(
            "arxiv:generic-compression",
            "Codebook Compression for Neuro-Symbolic Memory",
            "A vector symbolic architecture reduces memory use for symbolic reasoning.",
        )
        evaluate(value, self.taxonomy)
        self.assertFalse(value.primary_category)

    def test_deduplicate_merges_sources_by_title(self) -> None:
        first = paper("arxiv:1", "One Serving System", "model serving")
        second = paper("openreview:abc", "One Serving System", "model serving benchmark")
        second.source = "OpenReview"
        second.source_records = [{"source": "OpenReview", "id": "abc"}]
        merged = deduplicate([first, second])
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0].id, "arxiv:1")

    def test_diversity_cap(self) -> None:
        values = []
        for index in range(4):
            value = paper(
                f"arxiv:q{index}",
                f"LLM Quantization {index}",
                "quantization fp8 benchmark for language model inference",
            )
            evaluate(value, self.taxonomy)
            value.score = 90 - index
            values.append(value)
        other = paper(
            "arxiv:s1",
            "Elastic GPU Scheduler for AI Models",
            "gpu scheduling and cluster scheduling benchmark for machine learning",
        )
        evaluate(other, self.taxonomy)
        other.score = 85
        values.append(other)
        selected = select_featured(values, top_n=5, feature_threshold=70, max_same_leaf=2)
        quantized = [item for item in selected if item.primary_category["leaf_id"] == "quantization-low-precision"]
        self.assertLessEqual(len(quantized), 2)

    def test_wecom_split_respects_byte_limit(self) -> None:
        chunks = split_markdown("标题\n" + "中文内容" * 2000, limit=300)
        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(len(chunk.encode("utf-8")) <= 300 for chunk in chunks))

    def test_paper_store_prunes_records_outside_current_dataset(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            save_papers(root, [paper("arxiv:keep", "LLM Serving", "llm serving")])
            self.assertEqual(len(list((root / "data" / "papers").glob("*.json"))), 1)
            save_papers(root, [])
            self.assertEqual(list((root / "data" / "papers").glob("*.json")), [])

    def test_friday_edition_includes_previous_weekend(self) -> None:
        self.assertEqual(edition_week_id("2026-08-01"), "2026-W32")
        self.assertEqual(edition_bounds("2026-W32"), ("2026-08-01", "2026-08-07"))

    def test_fixture_pipeline_generates_week_and_site_data(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in (
                "data/papers",
                "data/weeks",
                "data/state",
                "reports",
                "src/data",
                "public",
                "src/content/docs/papers",
                "src/content/docs/weekly",
                "src/content/docs/topics",
            ):
                (root / relative).mkdir(parents=True, exist_ok=True)
            summary = run(
                root=root,
                config_path=ROOT / "config" / "config.example.yaml",
                taxonomy_path=ROOT / "config" / "taxonomy.yaml",
                reference_date=date(2026, 8, 5),
                fixture_path=ROOT / "tests" / "fixtures" / "papers.json",
                skip_openreview=True,
                skip_pdf=True,
            )
            self.assertEqual(summary["source_errors"], 0)
            self.assertTrue((root / "src" / "data" / "papers.json").exists())
            self.assertTrue((root / "reports" / "2026-W32.md").exists())

    def test_event_detector_uses_event_week_window(self) -> None:
        config = load_events(ROOT / "config" / "events.yaml")
        due = detect_due_events(config, date(2026, 7, 3))
        self.assertIn("acl-2026", {item["id"] for item in due})
        self.assertNotIn("acl-2026", {item["id"] for item in detect_due_events(config, date(2026, 8, 5))})

    def test_event_scope_rejects_generic_code_generation(self) -> None:
        generic = paper(
            "acl:generic",
            "An Agent for Scientific Code Generation",
            "A large language model reduces computational cost for theorem proving.",
        )
        systems = paper(
            "acl:systems",
            "A GPU Kernel Generator",
            "We optimize inference throughput and latency for large language models.",
        )
        self.assertFalse(_in_event_scope(generic))
        self.assertTrue(_in_event_scope(systems))

    def test_acl_xml_parser_extracts_official_paper(self) -> None:
        payload = b"""<collection id='2026.acl'><volume id='long'><paper id='1'>
        <title>Fast <fixed-case>LLM</fixed-case> Serving</title><author><first>Ada</first><last>Lovelace</last></author>
        <abstract>We evaluate speculative decoding for large language model inference.</abstract>
        </paper></volume></collection>"""
        event = {"id": "acl-2026", "short_name": "ACL 2026", "start_date": "2026-07-02", "volumes": ["long"]}
        values, total = parse_acl_anthology_xml(payload, event)
        self.assertEqual(total, 1)
        self.assertEqual(values[0].paper.id, "acl:2026.acl-long.1")
        self.assertEqual(values[0].paper.authors, ["Ada Lovelace"])

        findings = payload.replace(b"id='2026.acl'", b"id='2026.findings'").replace(
            b"id='long'", b"id='acl'"
        )
        values, _ = parse_acl_anthology_xml(findings, {**event, "volumes": ["acl"]})
        self.assertEqual(values[0].paper.id, "acl:2026.findings-acl.1")
        self.assertEqual(values[0].track, "Findings")

    def test_event_fixture_generates_independent_page(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "config" / "event_editorial").mkdir(parents=True)
            summary = run_event(
                root=root,
                config_path=ROOT / "config" / "events.yaml",
                taxonomy_path=ROOT / "config" / "taxonomy.yaml",
                event_id="acl-2026",
                reference_date=date(2026, 8, 5),
                fixture_path=ROOT / "tests" / "fixtures" / "acl-2026-papers.json",
            )
            self.assertGreater(summary["relevant_total"], 0)
            self.assertTrue((root / "src" / "content" / "docs" / "events" / "acl-2026.md").exists())
            index = (root / "src" / "content" / "docs" / "events" / "index.md").read_text()
            self.assertIn("event-status--archived", index)
            self.assertIn("event-status--tracking", index)
            self.assertFalse((root / "data" / "papers").exists())

    def test_parse_usenix_schedule_html(self) -> None:
        payload = b"""
<article class="node node-session view-mode-schedule">
  <h2 class="node-title">Resource-Efficient LLM Serving</h2>
  <article class="node node-paper view-mode-schedule">
    <h2><a href="/conference/osdi26/presentation/example">Example LLM Serving</a></h2>
    <div class="field-name-field-paper-people-text"><p>Alice Smith and Bob Jones, <em>Example University</em><br><em>Awarded Best Paper!</em></p></div>
    <div class="field-name-field-paper-sub-type">Operational Systems Paper</div>
    <div class="field-name-field-paper-description-long"><p>We present an LLM serving system with lower latency and higher throughput.</p></div>
  </article>
  <article class="node node-paper view-mode-schedule">
    <h2><a href="/conference/osdi26/presentation/keynote">Keynote</a></h2>
    <div class="field-name-field-paper-description-long"><p>Not a proceedings paper.</p></div>
  </article>
</article>
"""
        event = {
            "id": "osdi-2026",
            "short_name": "OSDI 2026",
            "start_date": "2026-07-13",
            "publication_date": "2026-07-13",
            "official_url": "https://www.usenix.org/conference/osdi26",
            "pdf_url_template": "https://www.usenix.org/system/files/osdi26-{slug}.pdf",
        }
        values, total = parse_usenix_schedule_html(payload, event)
        self.assertEqual(total, 1)
        self.assertEqual(values[0].paper.id, "usenix:osdi-2026:example")
        self.assertEqual(values[0].paper.authors, ["Alice Smith", "Bob Jones"])
        self.assertEqual(values[0].track, "Resource-Efficient LLM Serving · Operational Systems")
        self.assertEqual(values[0].awards, ["Jay Lepreau Best Paper Award"])
        self.assertEqual(values[0].paper.pdf_url, "https://www.usenix.org/system/files/osdi26-example.pdf")

    def test_official_program_event_generates_briefing_without_papers(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            config_path = root / "events.yaml"
            config_path.write_text(
                """version: 1
events:
  - id: program-2026
    short_name: Program 2026
    name: Program 2026
    domain: ML Systems
    community: Test
    event_type: Workshop
    tier: 1
    start_date: 2026-12-01
    end_date: 2026-12-02
    location: Test City
    official_url: https://example.com
    program_url: https://example.com/program
    collector: official_program
    program_released_date: 2026-08-10
    summary_zh: 官方议程已发布。
    relevance_zh: 与 AI Infra 相关。
    key_programs:
      - {title: Systems Workshop, date: 2026-12-02, url: https://example.com/systems, focus_zh: 调度与显存。}
    sources:
      - {label: Official program, url: https://example.com/program, checked_at: 2026-08-14}
""",
                encoding="utf-8",
            )
            summary = run_event(
                root=root,
                config_path=config_path,
                taxonomy_path=ROOT / "config" / "taxonomy.yaml",
                event_id="program-2026",
                reference_date=date(2026, 8, 14),
                trigger_type="program_released",
            )
            self.assertEqual(summary["corpus_total"], 0)
            self.assertEqual(summary["selected_total"], 0)
            page = (root / "src" / "content" / "docs" / "events" / "program-2026.md").read_text()
            self.assertIn("重点议程 1 项", page)
            self.assertIn("program_released", page)
            self.assertNotIn("## 精选论文", page)


if __name__ == "__main__":
    unittest.main()
