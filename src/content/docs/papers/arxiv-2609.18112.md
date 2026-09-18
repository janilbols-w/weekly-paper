---
title: "Token Latency Fairness: Performance Isolation for Multi-Tenant LLM Serving"
description: "LLM serving is typically offered as a shared, multi-tenant service, where high-demand workloads from one client can cause latency SLO violations for others."
---

**评分：47/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.18112) · [PDF](https://arxiv.org/pdf/2609.18112)

## 一句话摘要

LLM serving is typically offered as a shared, multi-tenant service, where high-demand workloads from one client can cause latency SLO violations for others.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM serving is typically offered as a shared, multi-tenant service, where high-demand workloads from one client can cause latency SLO violations for others. Existing solutions for performance isolation equalize client throughput in the long run, for example through queueing and batching fairness. However, these approaches do not provide latency isolation guarantees; as a result, well-behaved clients can still experience significant degradation to their token-level latencies. In this paper, we present FairInference, which provides the novel {\delta}-token fairness guarantee: for a well-behaved client, if a token is generated in d time units in isolation, it will be generated within d + {\delta} time units in multi-tenant execution, providing strong latency isolation guarantees for LLM serving. To achieve this, FairInference addresses a key challenge of LLM serving: bounding delays from sharing GPU resources without support for fine-grained scheduling or resource allocation. In FairInference, the scheduler enforces per-token deadlines, while bounding the delays from GPU compute sharing and accounting for the additional delays introduced by the shared KV caching in GPU memory. We show that FairInference effectively bounds token-level latency spikes for well-behaved clients and improves overall throughput compared to state-of-the-art LLM serving systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant, slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dev Bali, Soujanya Ponnapalli, Yichuan Wang, Natacha Crooks, Scott Shenker, Matei Zaharia
- 发布：2026-09-16；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
