---
title: "Dispatch Control for Priority-Based, Multi-Tenant Workflows under Multi-Resource External Rate Limits"
description: "Workflow engines orchestrate pipelines of activities, which often call external APIs, on a fixed pool of worker slots, the threads that run them."
---

**评分：49/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2611.02926) · [PDF](https://arxiv.org/pdf/2611.02926)

## 一句话摘要

Workflow engines orchestrate pipelines of activities, which often call external APIs, on a fixed pool of worker slots, the threads that run them.

## 为什么值得关注

待编辑增强。

## 摘要原文

Workflow engines orchestrate pipelines of activities, which often call external APIs, on a fixed pool of worker slots, the threads that run them. When an API enforces a hard rate limit shared by all tenants and priorities, a throttled call that retries after a backoff keeps its worker slot and starves other tenants. Large Language Model provider APIs are particularly complex: their per-organization caps are low and bind independently on requests and tokens per minute. The operator can neither reconfigure the cap nor observe saturation before a request fails, so classical fair-queuing assumptions do not hold. We present Backpressure, a worker-side admission gate. It checks each call's cost atomically against shared admission state and enforces fairness over requests and tokens. A denied call releases its worker slot and waits on a durable timer, so waiting no longer blocks execution capacity. We compare against a naive retry, the AI gateway LiteLLM, and the built-in throttle of the workflow engine Temporal. On a workload with three priority classes, Backpressure raises fairness (Jain's index over each queue's fraction of its entitled share) from 0.60 to 0.89, where 1.0 is ideal. It also cuts high-priority tail latency roughly 8x. When tokens are the binding limit, all request-based baselines serve every priority equally, whereas Backpressure keeps the priority order and reaches a dominant-resource fairness of ~0.99. Admission costs one round trip to shared state, adds no measurable latency when the cap does not bind, and fails open if shared state is unavailable.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant, tail latency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Stanislav Kosorin, Trever Schirmer, Leonard Wossnig, David Bermbach
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
