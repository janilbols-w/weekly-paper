---
title: "DrugReason: Dynamic Multi-View Reasoning over Knowledge Graph and Language Evidence for Drug Repurposing"
description: "Drug repurposing aims to identify new therapeutic uses for existing compounds and, compared with de novo drug discovery, offers a faster and more cost-effective path to clinical translation."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.06779) · [PDF](https://arxiv.org/pdf/2609.06779)

## 一句话摘要

Drug repurposing aims to identify new therapeutic uses for existing compounds and, compared with de novo drug discovery, offers a faster and more cost-effective path to clinical translation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Drug repurposing aims to identify new therapeutic uses for existing compounds and, compared with de novo drug discovery, offers a faster and more cost-effective path to clinical translation. However, the space of candidate drug-disease pairs is enormous and their underlying relationships often depend on complex multi-hop biological mechanisms, making it difficult to reliably predict which pairs represent true therapeutic relationships. Existing approaches tackle this from two directions: knowledge graph-based methods organize curated biomedical evidence into structured relational networks for grounded multi-hop reasoning, while LLM-based methods leverage pretrained knowledge to generate flexible mechanistic rationales. Yet neither is sufficient alone - KGs are confined to observed graph structure while LLMs lack factual grounding and risk hallucination. To address this gap, we propose DrugReason, a multi-view reasoning framework that integrates grounded KG reasoning with LLM-generated mechanistic inference for drug repurposing. DrugReason adaptively routes diverse reasoning paths to specialized experts conditioned on the query context, while a cross-expert distillation objective enables knowledge sharing without sacrificing expert specialization. Experiments on PharmaDB, DDInter, and DrugBank show that DrugReason improves average performance over strong single-view reasoning baselines and achieves competitive or superior results compared with graph-based alternatives, while providing interpretable routing-based predictions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zijie Liu, Hongxuan Li, Zhen Tan, Jinhao Duan, Baixiang Huang, Zunpeng Liu, Kai Shu, Tianlong Chen
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
