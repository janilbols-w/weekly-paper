---
title: "Automated Detection and Structuring of Social Tipping Point Evidence in Climate related Documents: A Modular AI Framework"
description: "The climate literature has grown faster than review teams can read it."
---

**评分：39/100** · AI 基础设施 > 集群与资源系统 > 存储与数据平面

[论文原文](https://arxiv.org/abs/2609.12254) · [PDF](https://arxiv.org/pdf/2609.12254)

## 一句话摘要

The climate literature has grown faster than review teams can read it.

## 为什么值得关注

待编辑增强。

## 摘要原文

The climate literature has grown faster than review teams can read it. That gap matters most for a concept like the environmental social tipping point, the threshold at which a small change triggers rapid, self-reinforcing change in a social system. Evidence of this kind of shift is usually contained in one or two paragraphs within a longer document. As a result, existing text mining tools-which categorize entire documents by topic or highlight isolated claims-leave an expanding set of important evidence without any systematic method for discovery or organization. This paper presents an open and modular transformer-based framework that detects and structures social tipping point evidence at the passage level. The framework joins five components into a single deployable workflow: a DistilBERT boundary splitter for segmentation, an iteratively augmented RoBERTa classifier for detection, a Mistral 7B model that rewrites each detected passage for clarity, a LLaMA 3.2 3B model that rates the passage against five published social tipping point criteria, and a Milvus vector store for semantic retrieval. The system is wrapped in a Streamlit interface backed by MinIO object storage. Evaluated on a 163-passage benchmark labelled by GPT-4.1 and a 51-passage set reviewed by experts, the splitter surpassed three competing methods on a nine-metric composite score (6.137). The tuned RoBERTa model achieved 71.4 percent accuracy with a Cohen's kappa of 0.337 on the full benchmark, and 87.5 percent accuracy with a kappa of 0.742 on passages with labels, outperforming both a climate-focused model and untuned language models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: object storage
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kavindu Perera, Mohammad Abaeiani, Ekaterina Gilman, Lauri Loven, Mourad Oussalah, Tassos Kanellos, Beatrice Gobbo, Dante Adami, Nicol\`o Ferriani, Maximiliano Romero, Pierre Rossel, Marc Bonazountas, Christina Deligianni, Nikos Xyderis, Artur Bogucki, Lampros Argyriou, Prasasthy Balasubramanian
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
