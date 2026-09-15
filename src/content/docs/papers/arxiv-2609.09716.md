---
title: "Scaling E-Commerce Attribute Extraction with Parallel Decoding"
description: "Customers rely on specific product attributes to compare products and make purchasing decisions, but e-commerce catalogs are messy and unstructured, making it difficult to identify which attributes matter most and extract them at scale."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.09716) · [PDF](https://arxiv.org/pdf/2609.09716)

## 一句话摘要

Customers rely on specific product attributes to compare products and make purchasing decisions, but e-commerce catalogs are messy and unstructured, making it difficult to identify which attributes matter most and extract them at scale.

## 为什么值得关注

待编辑增强。

## 摘要原文

Customers rely on specific product attributes to compare products and make purchasing decisions, but e-commerce catalogs are messy and unstructured, making it difficult to identify which attributes matter most and extract them at scale. Standard Attribute Value Extraction (AVE) systems treat all attributes equally, producing large, inconsistent attribute sets that do not reflect the factors consumers use to differentiate products. We introduce a two-stage LLM pipeline that first discovers a compact, ranked schema of purchase-discriminative attributes for each product category, then extracts their values from catalog text using a fine-tuned compact LLM (Qwen3-4B) with Hyper-Parallel Decoding (HPD). This pipeline achieves 85% extraction accuracy, on par with the foundational LLM it was distilled from, while reducing inference costs by 92% over foundational LLMs, enabling production-scale use for product discovery and catalog enrichment. The resulting category-level structured representations effectively constitute automatically constructed product knowledge bases, providing consistent, comparable attributes across varied product categories that can ground downstream knowledge-intensive applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nikhita Vedula, Dushyanta Dhyani, Bryan Wang, Shervin Malmasi
- 发布：2026-09-10；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
