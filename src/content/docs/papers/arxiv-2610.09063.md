---
title: "Multi-Label Topic Assignment via LLM Distillation: A Comparative Analysis of Generative vs. Discriminative Student Models"
description: "Multi-label topic assignment for user-generated content (UGC) -- including product reviews and buyer-seller conversations -- poses unique scalability challenges in large-scale e-commerce due to informal language, extreme label sparsity, and rapidly evolving taxonomies."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.09063) · [PDF](https://arxiv.org/pdf/2610.09063)

## 一句话摘要

Multi-label topic assignment for user-generated content (UGC) -- including product reviews and buyer-seller conversations -- poses unique scalability challenges in large-scale e-commerce due to informal language, extreme label sparsity, and rapidly evolving taxonomies.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-label topic assignment for user-generated content (UGC) -- including product reviews and buyer-seller conversations -- poses unique scalability challenges in large-scale e-commerce due to informal language, extreme label sparsity, and rapidly evolving taxonomies. While utilizing Large Language Models (LLMs) as labeling oracles to distill ground-truth data has emerged as an industry standard to bypass prohibitive manual annotation costs, determining the optimal, low-latency architecture for the resulting student models remains an open challenge. To address this, we conduct a comprehensive evaluation across Small Language Model (SLM) parameter scales (1B, 4B, and 8B) and architectural paradigms (causal generative versus bidirectional discriminative). Comparing generative text-to-label classifiers against discriminative baselines (DeBERTa-V3 and ModernBERT), our analysis reveals a crucial data-dependent trade-off: while discriminative models outperform ultra-lightweight generative models on structured product reviews, even the smallest 1B generative model surpasses discriminative baselines on complex, multi-turn conversational data. Furthermore, generative models maintain robust performance under massive label-set expansion (up to 112 topics) and severe long-tail distributions, whereas discriminative baselines suffer a 35% drop in Macro-F1 at scale. Finally, we detail the successful production deployment of these optimized models across both product review and conversational domains, demonstrating strict latency compliance and tangible business impact at a global marketplace scale.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sourabh Kasliwal, Shubhranshu Singh
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
