---
title: "Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving"
description: "The reasoning and agentic capabilities of LLMs have expanded the range of applications they support, from short interactive exchanges to long, prefix-heavy requests."
---

**评分：45/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.06557) · [PDF](https://arxiv.org/pdf/2608.06557)

## 一句话摘要

The reasoning and agentic capabilities of LLMs have expanded the range of applications they support, from short interactive exchanges to long, prefix-heavy requests.

## 为什么值得关注

待编辑增强。

## 摘要原文

The reasoning and agentic capabilities of LLMs have expanded the range of applications they support, from short interactive exchanges to long, prefix-heavy requests. LLM serving platforms today define response-latency service-level objectives (SLOs), yet requests under the same SLO differ by orders of magnitude in input length, generation length, execution cost, and reusable KV-cache availability, leaving each request with a different amount of latency headroom. This headroom must cover not only execution, but also scheduling and preemption delays and the cost of retrieving KV state from deeper memory tiers. Existing systems manage these decisions independently, despite their combined impact on latency. We present Cascade, an LLM serving system that coordinates these decisions using a per-request latency budget: the difference between a request's SLO and its predicted remaining service time, continuously updated from request characteristics, KV-cache state, and system load. Cascade uses this budget to prioritize requests and to decide how much non-resident KV state to prefetch from deeper tiers, with the remainder fetched on demand or recomputed given the serving system. On production traces across three LLMs, Cascade improves goodput by 10.4x over vLLM and 1.8x over a SLO-aware scheduler, and reduces SLO violations by 76% and 31%, respectively, while remaining fair across heterogeneous requests.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Muhammad Adnan, Rohan Mahapatra, Prashant J. Nair, Daniel Berger, Pantea Zardoshti, Rodrigo Fonseca, Esha Choukse
- 发布：2026-08-10；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
