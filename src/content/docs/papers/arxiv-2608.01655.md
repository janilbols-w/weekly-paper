---
title: "PrefixPlace: Provable Prefix Key-Value Placement for Large Language Model Serving under Heterogeneous Compute and Transfer Costs"
description: "Prefix Key-Value (KV) reuse avoids repeated prefill in Large Language Model (LLM) inference, but local misses require recomputation or replica fetches."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.01655) · [PDF](https://arxiv.org/pdf/2608.01655)

## 一句话摘要

Prefix Key-Value (KV) reuse avoids repeated prefill in Large Language Model (LLM) inference, but local misses require recomputation or replica fetches.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prefix Key-Value (KV) reuse avoids repeated prefill in Large Language Model (LLM) inference, but local misses require recomputation or replica fetches. Their relative cost varies with hardware, prefix depth, KV goodput, and replica location, making hit-rate-based placement suboptimal. To address this issue, we propose an epoch-level planner, PrefixPlace, which assigns prefix-complete targets under memory budgets and profiled demand, compute, and transfer costs. The objective decomposes into local-copy value plus first-replica coverage, and source-dependent costs yield a monotone facility-location objective; each worker update is an additive rooted-tree problem solved exactly in O(nk) time for n chunks and capacity k, giving a fixed-order 1/2-approximation that coordinate refinement and order-diverse starts improve without weakening. T4, L4, and A100 measurements reveal distinct regimes. Across 432 instances with exact optima, PrefixPlace averages 99.84% of optimum and never falls below 98.02%. In Retrieval-Augmented Generation (RAG) replays, it improves materialization-cost saving by 40.3% over vLLM Automatic Prefix Caching (vLLM-APC) and 6.3% over the best offline baseline. On WikiQA, gains are 40.4% and 5.3%. Finally, PrefixPlace solves a 50,000-node, 16-worker placement in 12.3 s on one processor, enabling timely replanning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiyu Wang, Rajkumar Buyya
- 发布：2026-08-03；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
