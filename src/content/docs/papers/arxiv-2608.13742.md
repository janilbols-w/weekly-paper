---
title: "Does ISO-Grounded NFR Specification Improve LLM Code Generation? A Comparison of Rich and Structured Interventions against a Natural-Language Baseline"
description: "In LLM-based code generation, Non-Functional Requirements (NFRs) are often specified as terse one-line phrases."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.13742) · [PDF](https://arxiv.org/pdf/2608.13742)

## 一句话摘要

In LLM-based code generation, Non-Functional Requirements (NFRs) are often specified as terse one-line phrases.

## 为什么值得关注

待编辑增强。

## 摘要原文

In LLM-based code generation, Non-Functional Requirements (NFRs) are often specified as terse one-line phrases. We ask whether grounding those specifications in ISO/IEC 25010 Quality Model, either as rich natural-language prose (NL-rich) or as structured JSON (Structured), improves code generated on HumanEval/HumanEval-ET compared to a RobuNFR-style one-line baseline (NL-simple). We evaluate four NFRs (performance, error handling, code smell, readability) with ten prompt variations per condition under a fixed model snapshot and paired non-parametric analysis. Primary finding: ISO-grounded enrichment improves static quality proxies (unreadability density falls across all four NFRs (e.g., Performance 0.88 -> 0.69 for NL-rich)) and reduces sensitivity to prompt wording, but does not reliably improve functional correctness; for error handling, extended-test pass rate decreases, suggesting tension between defensive coding patterns and exact-output benchmarks. Secondary finding: when ISO content is held constant, NL-rich and Structured differ negligibly in correctness (|delta| <= 0.023), indicating that semantic content matters more than JSON-vs-prose format. Practitioners should invest in standard-grounded NFR content rather than serialization form. A fully traceable replication package is provided.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jo\`ao Pedro Monteiro Pereira, Vinicius Cardoso Garcia
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
