---
title: "RouteRelay: Event-Triggered Cross-Layer Route Reuse for Efficient Dynamic Sparse Attention"
description: "Dynamic sparse attention reduces long-context prefill cost by routing each query chunk to a small set of key chunks at every Transformer layer."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.07306) · [PDF](https://arxiv.org/pdf/2609.07306)

## 一句话摘要

Dynamic sparse attention reduces long-context prefill cost by routing each query chunk to a small set of key chunks at every Transformer layer.

## 为什么值得关注

待编辑增强。

## 摘要原文

Dynamic sparse attention reduces long-context prefill cost by routing each query chunk to a small set of key chunks at every Transformer layer. The sparse attention kernel avoids most token interactions, but the router still rebuilds a chunk--chunk score matrix layer after layer, even when the selected routes change little. We introduce RouteRelay, a router-agnostic method that reuses only route metadata across depth while continuing to compute attention with the current layer's queries, keys, and values. Anchor layers perform full routing. Intermediate layers rescore the previous top-$k$ route and a compact sentinel set of near-miss and randomly probed chunks. A query row is rerouted only when a sentinel challenges its weakest selected chunk. We give a top-$k$ stability condition, a probabilistic bound on missed challengers, and a row-selective GPU execution design. In a reproducible empirical evaluation, RouteRelay retains at least 99.99% route recall while rerouting 25.0%, 55.4%, and 78.2% of rows under low, moderate, and high cross-layer drift, respectively. Across routing scales, RouteRelay retains 100.0% recall while evaluating 38.4--51.6% of full-routing score pairs as the key-chunk count grows from 128 to 1024. Its unfused CPU execution remains slower than dense matrix multiplication, exposing row compaction and ledger updates as the main kernel-engineering targets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bin Li, Sisi Liu, Chenyang Hu, Chaoyang Zhang, Wei Li, Hui Song
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
