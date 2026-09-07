---
title: "Distill Globally, Adapt Locally: Reasoning Distillation and Product-Type Test-Time Training for Scalable Trade-Up Recommendation"
description: "Trade-up recommendation identifies higher-quality alternatives that preserve a customer's purchase intent while offering upgraded benefits."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.05363) · [PDF](https://arxiv.org/pdf/2609.05363)

## 一句话摘要

Trade-up recommendation identifies higher-quality alternatives that preserve a customer's purchase intent while offering upgraded benefits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Trade-up recommendation identifies higher-quality alternatives that preserve a customer's purchase intent while offering upgraded benefits. Large language models (LLMs) can reason about such distinctions, but applying them directly to hundreds of millions of product pairs is operationally impractical. We introduce a two-level framework that distills LLM reasoning into an efficient non-generative student and adapts its decision boundary to product-type-specific trade-up criteria. At Level 1, a retrieval-augmented few-shot LLM teacher generates structured relation labels and natural-language rationales. These rationales supervise a compact embedding-pair classifier through alignment and contrastive objectives; at inference, the student uses only two precomputed 768-dimensional product embeddings, with no LLM calls or text generation. On a fixed human-annotated benchmark of 8,352 pairs, a 15.5M-parameter four-class reasoning-distilled student achieves AUC 0.924 (95% CI [0.918, 0.929]), compared with 0.912 for the four-class label-only student. At Level 2, product-type test-time training (PT-TTT) uses few-shot demonstrations to optimize lightweight category-specific adapters over the frozen student. PT-TTT improves AUC from 0.924 to 0.941 and average precision from 0.920 to 0.940. On a 100K-pair proxy catalog, the distilled student on a single eight-GPU machine is approximately 5,000x faster and 10,000x lower in estimated cost than direct LLM inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Siliang Liu, Mohammad Ghasemi, Sapan Patel, Amin Banitalebi-Dehkordi
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
