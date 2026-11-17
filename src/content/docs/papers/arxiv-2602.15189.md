---
title: "ScrapeGraphAI-100k: Dataset for Schema-Constrained LLM Generation"
description: "Producing output that conforms to a specified JSON schema underlies tool use, structured extraction, and knowledge base construction in modern large language models."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.15189) · [PDF](https://arxiv.org/pdf/2602.15189)

## 一句话摘要

Producing output that conforms to a specified JSON schema underlies tool use, structured extraction, and knowledge base construction in modern large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Producing output that conforms to a specified JSON schema underlies tool use, structured extraction, and knowledge base construction in modern large language models. Despite this centrality, public datasets for the task remain small, synthetic, or text-only, and rarely pair real page content with the prompts and schemas used in practice. We introduce ScrapeGraphAI-100k, 93,695 schema-constrained extraction events collected via opt-out ScrapeGraphAI telemetry in Q2--Q3 2025, deduplicated and balanced by schema from 9M raw events. The corpus spans 25,453 unique schemas, across 15 named languages, with English covering 89% of detected content. Each instance pairs Markdown-converted page content with a prompt, schema, LLM response, and per-example jsonschema-rs structural conformance labels. We characterize structural diversity across the corpus and identify sharp failure thresholds as schema complexity grows. As a case study, a 1.7B student fine-tuned on this data closely tracks the output distribution of its GPT-5-nano teacher, though it still trails a 30B-A3B reference (3.3B active parameters) on schema compliance. We offer this distillation result as preliminary evidence that grounding schema-constrained generation in real practitioner workloads at scale enables training and benchmarking that prior synthetic or text-only corpora could not support. ScrapeGraphAI-100k is publicly available on HuggingFace.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：William Brach, Francesco Zuppichini, Marco Vinciguerra, Lorenzo Padoan
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
