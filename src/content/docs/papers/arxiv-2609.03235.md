---
title: "SGD-KV: Summarization Guided KV Cache Compression"
description: "Large language models (LLMs) face severe memory bottlenecks in long-context inference due to the linearly growing size of key-value (KV) caches."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.03235) · [PDF](https://arxiv.org/pdf/2609.03235)

## 一句话摘要

Large language models (LLMs) face severe memory bottlenecks in long-context inference due to the linearly growing size of key-value (KV) caches.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) face severe memory bottlenecks in long-context inference due to the linearly growing size of key-value (KV) caches. Existing KV cache compression techniques typically rely on simple heuristics, overlooking the distinct functional roles of different attention heads. We present SGD-KV (Summarization-Guided KV Cache Compression), a head-aware framework that leverages a novel chunk-summarization diagnostic task to systematically identify and prioritize attention heads specialized in hierarchical information aggregation. Experiments on Qwen2.5-7B-1M and Qwen3-32B across diverse long-context benchmarks demonstrate that SGD-KV achieves state-of-the-art performance with contexts up to 1M tokens, while reducing KV cache memory usage by up to 75%. Our findings show that strategically allocating the KV cache budget based on the summarization score distribution of attention heads yields a superior efficiency-accuracy trade-off for long-context inference.

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

- 作者：Zeyu Liu, Woomin Song, Xuandi Fu, Sai Muralidhar Jayanthi, Vivek Govindan, Aram Galstyan, Sravan Babu Bodapati, Srikanth Ronanki
- 发布：2026-09-03；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
