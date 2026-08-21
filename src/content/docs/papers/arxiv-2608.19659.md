---
title: "FleetSieve: Decision-Critical Profiling for SLO-Aware LLM Fleet Configuration"
description: "Choosing tensor-parallel (TP) degrees and replica counts for an LLM serving fleet is difficult because performance is not monotonic in TP and the feasible choice can change with load."
---

**评分：40/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.19659) · [PDF](https://arxiv.org/pdf/2608.19659)

## 一句话摘要

Choosing tensor-parallel (TP) degrees and replica counts for an LLM serving fleet is difficult because performance is not monotonic in TP and the feasible choice can change with load.

## 为什么值得关注

待编辑增强。

## 摘要原文

Choosing tensor-parallel (TP) degrees and replica counts for an LLM serving fleet is difficult because performance is not monotonic in TP and the feasible choice can change with load. Exhaustive profiling resolves this uncertainty, but measures many configurations that do not affect the final resource allocation. We present FleetSieve, which selects measurements according to their expected effect on a resource-coupled, SLO-aware fleet decision. FleetSieve models capacity and tail latency jointly, compares conservative and optimistic allocations, and stops when their remaining decision gap is below a specified tolerance. On a fixed H100 measurement grid for a 31B-parameter open-weight model, FleetSieve reaches the oracle aggregate decision using 22,200 GPU-seconds, 6.9% less than uniform random profiling in the fixed comparison. Across 200 random reveal orders, its mean saving over random profiling is 5.4% (95% bootstrap CI: 3.5-7.2%). The fixed-comparison saving is 21.5% for Chat, while FleetSieve does not use the fewest GPU-seconds for Code. Joint capacity and tail modeling also avoids selecting a configuration whose 46.4-second completion p99 violates a 30-second SLO. In a 16-GPU allocation, an incorrect sparse-profile decision loses up to 1.93 requests/s and 12.4 percentage points of max-min fulfillment. Boundary repeats and BurstGPT measurements support the observed load-dependent tail-latency mechanism.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo, tail latency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Huang Cheng, Scott Zhang, Aubert Li
- 发布：2026-08-21；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
