---
title: "Pacing Branch Parallelism in LLM Serving"
description: "Recent methods expose intra-request parallelism in LLM outputs, allowing independent branches to decode concurrently."
---

**评分：51/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2605.06914) · [PDF](https://arxiv.org/pdf/2605.06914)

## 一句话摘要

Recent methods expose intra-request parallelism in LLM outputs, allowing independent branches to decode concurrently.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent methods expose intra-request parallelism in LLM outputs, allowing independent branches to decode concurrently. Existing serving systems execute these branches eagerly or under fixed caps. We show that both are brittle: eager admission inflates the shared decode step, degrading co-batched requests in serial stages, while conservative fixed caps forgo the throughput that motivated exposing branches in the first place. We call the excess step latency caused by admitted branches the \emph{branch externality} and show that the safe width depends on batch composition, context lengths, and accumulated slack, all of which change continuously over a workload trace. We introduce PACE, a per-step admission controller that treats extra branches as opportunistic width, admitted only when the predicted branch externality fits within the batch's current slack budget. Per-step regulation is practical because branch-level scheduling decouples compute from memory: branches share the request's prefix KV, so expanding or contracting width requires no memory reclamation. On Qwen3-32B, PACE improves goodput by $1.77\times$ over serving without branch parallelism and by $1.48\times$ over eager admission while maintaining 99\% SLO attainment. Comparable gains ($1.72$--$2.15\times$) hold on five additional dense and mixture-of-experts models with up to 671B parameters. Code is available at https://github.com/Swapnil-Gandhi/PACE

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Swapnil Gandhi, Siva Kumar Sastry Hari, William J. Dally, Christos Kozyrakis
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Swapnil-Gandhi/PACE](https://github.com/Swapnil-Gandhi/PACE)
- 阅读深度：metadata
