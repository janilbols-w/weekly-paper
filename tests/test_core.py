from __future__ import annotations

import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from weekly_paper.dedupe import deduplicate
from weekly_paper.evaluation import evaluate, select_featured
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


if __name__ == "__main__":
    unittest.main()
