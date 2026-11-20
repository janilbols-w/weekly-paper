---
title: "Global Importance Estimation for KV Cache Eviction"
description: "Memory consumption of the key-value (KV) cache remains a central bottleneck for long-context LLM inference."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2611.24969v1) · [PDF](https://arxiv.org/pdf/2611.24969v1)

## 一句话摘要

Memory consumption of the key-value (KV) cache remains a central bottleneck for long-context LLM inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Memory consumption of the key-value (KV) cache remains a central bottleneck for long-context LLM inference. We introduce PRKV, a training-free KV eviction method that estimates multi-hop global token importance by applying Personalized PageRank over attention-induced transition graphs. This enables importance propagation beyond recency or instantaneous attention, without modifying the model. We benchmark PRKV on long-context understanding, sparse retrieval, and chain-of-thought reasoning tasks using multiple LLM families. Under moderate to aggressive compression ratios, including up to 90%, PRKV achieves competitive task performance against established eviction baselines while reducing peak memory usage with low end-to-end overhead. These results demonstrate that multi-hop global influence estimation yields a favorable accuracy--memory trade-off for scalable long-context inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Seojin Kim, Noseong Park
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
