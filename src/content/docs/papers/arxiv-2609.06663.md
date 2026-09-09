---
title: "ECOKV: Geometry-Aware KV Cache Eviction via Complementary Diversity Metrics"
description: "Although multimodal Large Language Models (MLLMs) excel in diverse tasks, their scalability remains limited by the memory and computational overhead of KV cache storage."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.06663) · [PDF](https://arxiv.org/pdf/2609.06663)

## 一句话摘要

Although multimodal Large Language Models (MLLMs) excel in diverse tasks, their scalability remains limited by the memory and computational overhead of KV cache storage.

## 为什么值得关注

待编辑增强。

## 摘要原文

Although multimodal Large Language Models (MLLMs) excel in diverse tasks, their scalability remains limited by the memory and computational overhead of KV cache storage. Recent KV cache eviction approaches incorporate a cosine similarity-based diversity metric with importance metrics to selectively retain critical key-value pairs. However, cosine similarity involves normalization that discards magnitude information, and it often yields uniformly high similarity values across layers due to the anisotropy property of hidden representations. In our study ECOKV, we rigorously deconstruct the capabilities of existing diversity metrics. Moving beyond simple measurement, we propose a geometry-aware composite metric that jointly leverages Euclidean distance and cosine similarity to capture token diversity from complementary perspectives. Furthermore, we use these two metrics to estimate the redundancy level of each attention head, allowing adaptive weighting between diversity and importance scores during token selection. Finally, we demonstrate that the observation window commonly employed to preserve recent tokens can be substantially reduced, thereby allocating more cache capacity to informative tokens and yielding consistent improvements. Extensive experiments demonstrate that ECOKV achieves state-of-the-art performance under various compression ratios and can be seamlessly integrated with existing KV cache eviction methods. We further analyze the relationship between importance and diversity, and examine redundancy patterns across layers and attention heads.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chin Ting Hsu, Yu-Syuan Xu, Ling Zou, Hsien-Kai Kuo, Wen-Huang Cheng
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
