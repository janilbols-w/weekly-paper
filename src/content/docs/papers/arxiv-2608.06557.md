---
title: "Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving"
description: "The reasoning and agentic capabilities of large language models have expanded the range of applications they support, from short interactive exchanges to long, compute-heavy requests."
---

**评分：48/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.06557) · [PDF](https://arxiv.org/pdf/2608.06557)

## 一句话摘要

The reasoning and agentic capabilities of large language models have expanded the range of applications they support, from short interactive exchanges to long, compute-heavy requests.

## 为什么值得关注

待编辑增强。

## 摘要原文

The reasoning and agentic capabilities of large language models have expanded the range of applications they support, from short interactive exchanges to long, compute-heavy requests. LLM serving platforms today define response-latency service-level objectives, even though requests within the same service can differ by orders of magnitude in input length, generation length, execution cost, and the availability of reusable KV-cache state. As a result, requests governed by the same service level objective have different urgency: after accounting for the time required to execute them, some have substantial latency headroom while others have almost none. We define this headroom---the difference between a request's service level objective and its predicted remaining service time---as its per-request latency budget. We present Cascade, an LLM serving system that estimates and continuously updates this budget from request characteristics, KV-cache state, and current system load. Unlike prior SLO-aware schedulers that use deadlines to govern request ordering alone, Cascade uses a single per-request budget to jointly coordinate request scheduling and KV-cache management across the memory hierarchy. Its scheduler prioritizes requests with little remaining budget, while its memory manager uses the same budget to decide whether non-resident KV state should be restored or prefetched from a deeper tier, retained in HBM, or recomputed. By directing queueing and data-movement overhead toward requests that can absorb it, Cascade improves SLO-satisfied goodput while preserving fairness across heterogeneous request classes. On production traces across three large language models, Cascade improves goodput by up to2.4x and reduces SLO violations by 40% relative to the default vLLM first-come, first-served scheduler.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: service level objective, slo
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Muhammad Adnan, Rohan Mahapatra, Prashant J. Nair, Daniel Berger, Pantea Zardoshti, Rodrigo Fonseca, Esha Choukse
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
