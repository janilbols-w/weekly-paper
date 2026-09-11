---
title: "KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints"
description: "LLM serving systems already reuse KV caches, but only when the reused text sits at the very start of the prompt."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.10266) · [PDF](https://arxiv.org/pdf/2609.10266)

## 一句话摘要

LLM serving systems already reuse KV caches, but only when the reused text sits at the very start of the prompt.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM serving systems already reuse KV caches, but only when the reused text sits at the very start of the prompt. Two growing workloads break this condition: a retrieval-augmented generation server assembles a different set of retrieved chunks for every query, and a multi-agent coordinator reads reports written by other agents. Reused inside a new prompt, a cache carries the wrong positions and never attended to the other sources. The cache may also have been written by a different checkpoint of the same model family, which changes the stored values. Repair methods for such caches have appeared in three separate communities, each measured on its own terms, and existing benchmarks test only exact-prefix reuse, where nothing is lost. KVShareArena benchmarks KV-cache reuse across prompt contexts and model checkpoints on retrieved chunks and agent reports. It scores every method by the fraction of the gap it recovers between no cache and full recomputation, and charges compute, memory, and per-request latency with the cache in hand, reporting the one-time cost of building a cache separately. We find that correcting positions, which needs no recomputation, is enough until a question needs several sources at once. There, only methods that pay, by re-encoding part of the cache or by training, recover half to two thirds of the gap; unrepaired caches can be worse than no cache. Cache-compression methods that are harmless on a single prompt fall significantly behind position correction on freshly written agent reports. These patterns hold across three model boards. When a different checkpoint wrote the cache, training-free methods are barely affected, while an adapter trained on one checkpoint's caches loses quality. Harness, frozen querysets, and cost accounting ship as a pip package with an automated submission workflow and a public leaderboard.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xi Shi, Qian Lou
- 发布：2026-09-09；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
