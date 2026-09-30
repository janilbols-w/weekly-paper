---
title: "LLM-Guided Ontology-Driven Knowledge Graph Construction from Unstructured Text"
description: "Ontology-driven knowledge graph construction from industrial text remains challenging due to the domain specificity of documents, the scarcity of annotated resources, and the complexity of ontology engineering workflows."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.31663) · [PDF](https://arxiv.org/pdf/2609.31663)

## 一句话摘要

Ontology-driven knowledge graph construction from industrial text remains challenging due to the domain specificity of documents, the scarcity of annotated resources, and the complexity of ontology engineering workflows.

## 为什么值得关注

待编辑增强。

## 摘要原文

Ontology-driven knowledge graph construction from industrial text remains challenging due to the domain specificity of documents, the scarcity of annotated resources, and the complexity of ontology engineering workflows. This paper presents and investigates the applicability of an ontology learning pipeline that combines compact open-source Large Language Models (LLMs), reusable prompting strategies, and open knowledge bases to support the extraction, structuring, enrichment, and evaluation of knowledge from textual corpora. The approach is tested and evaluated on a private French corpus of power-grid incident reports, using locally deployable open-source LLMs ranging from 7B to 32B parameters. Starting from unstructured reports, the approach extracts entities and relations, generates RDF triples, constructs related OWL ontology, enriches it using external knowledge sources, assesses the quality of the ontology, and subsequently constructs a populated knowledge graph grounded in the resulting ontology schema. Experiments on 80 manually annotated private reports show that schema-guided prompting significantly improves extraction quality, while quantized models provide an effective trade-off between performance and computational cost. These results demonstrate the feasibility of transforming domain-specific industrial text into ontology-based knowledge graphs using locally deployed open-source LLMs, while supporting the generalization of the extraction process through reusable prompting strategies.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Abdelhadi Belfadel, Maxence Gagnant, Joseph Kattan, Sana Tmar
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
