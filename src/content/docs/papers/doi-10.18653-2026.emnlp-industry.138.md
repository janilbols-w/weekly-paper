---
title: "BIRD-Persona: A Persona-Aware Benchmark for SQL and pandas Analytics Code Generation"
description: "Production text-to-code systems use large language models to turn natural-language analytics requests into executable SQL and pandas code."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2611.28542) · [PDF](https://arxiv.org/pdf/2611.28542)

## 一句话摘要

Production text-to-code systems use large language models to turn natural-language analytics requests into executable SQL and pandas code.

## 为什么值得关注

待编辑增强。

## 摘要原文

Production text-to-code systems use large language models to turn natural-language analytics requests into executable SQL and pandas code. Existing benchmarks cover both tasks but do not isolate when performance diverges between them. We introduce BIRD-Persona, a persona-stratified extension of BIRD-Python that adds novice and expert rewrites to tasks with matched SQL and pandas ground truth, along with schema variants and task-structure annotations. Across 1,534 tasks, nine models, and 245,592 evaluations, SQL outperforms pandas for eight of nine systems. The gap varies by condition: expert, schema-explicit prompts improve both paradigms but help SQL more; schema representations have mixed, model-dependent effects; and selected-column burden widens the gap while subqueries do not. By making user phrasing a controlled benchmark dimension, BIRD-Persona supports persona-aware and paradigm-aware evaluation of natural-language analytics systems. The dataset is available at https://huggingface.co/datasets/optum-cognition-lab/BIRD-Persona.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 6 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Davin Hill, Pawan Chorasiya, Bhawani S. Leelar, Oren Avram, Robert E. Tillman, Tamer Soliman
- 发布：2026-11-21；更新：2026-11-24
- 来源：arXiv RSS；Venue：Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing: Industry Track, pp. 2311-2332 (2026)
- 代码：未发现
- 阅读深度：metadata
