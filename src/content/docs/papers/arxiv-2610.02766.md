---
title: "Exact Memory-Time Optimization for Prefix-Cached Language Model Serving"
description: "Retaining language-model prefix states trades recomputation against storage time."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.02766) · [PDF](https://arxiv.org/pdf/2610.02766)

## 一句话摘要

Retaining language-model prefix states trades recomputation against storage time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retaining language-model prefix states trades recomputation against storage time. Optimizing each cached block independently can overcount savings: a resident block is usable only when the required preceding prefix is also available. We introduce Prefix-Certificate Retention (PCR), an exact finite-trace formulation for static, grouped, reset-on-access timeouts. Usable-prefix rewards become nodes whose prerequisites are timeout thresholds and preceding hit certificates. The resulting maximum-weight closure reduces to one minimum cut, with graph size linear in the number of block lookups and timeout choices. A breakpoint theorem extends the construction to all nonnegative timeouts without discretization error. We also derive a linear-time-in-grid-size dynamic program for ordered timeouts and bounds that certify the cost of this restriction. Exhaustive small-instance checks and chronological replay of 39,632 public Mooncake requests validate the formulation. On the fixed grid, ordered timeouts attain the unrestricted training optimum in 118 of 120 trace-grouping-price cases. Heterogeneous retention improves several held-out memory-time tradeoffs, but finer training optimization does not uniformly improve transfer. The contribution is a tractable optimization model and an auditable benchmark for retention policies; the experiments measure usable prefix blocks and storage time, not GPU latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shivam Gupta
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
