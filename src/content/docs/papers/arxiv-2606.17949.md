---
title: "RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving"
description: "Current heterogeneous LLM serving clusters decouple request scheduling into two independent tiers: learned model routers select a model based on the prompt without visibility into instance-level load, while load balancers assign requests to an instance of that chosen model without cross-model quality or cost awareness."
---

**评分：55/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2606.17949) · [PDF](https://arxiv.org/pdf/2606.17949)

## 一句话摘要

Current heterogeneous LLM serving clusters decouple request scheduling into two independent tiers: learned model routers select a model based on the prompt without visibility into instance-level load, while load balancers assign requests to an instance of that chosen model without cross-model quality or cost awareness.

## 为什么值得关注

待编辑增强。

## 摘要原文

Current heterogeneous LLM serving clusters decouple request scheduling into two independent tiers: learned model routers select a model based on the prompt without visibility into instance-level load, while load balancers assign requests to an instance of that chosen model without cross-model quality or cost awareness. This decoupled hierarchy induces conflicting objectives and severely restricts the global optimization space. For example, a quality-oriented router may stubbornly direct 55% of requests to a 72B model regardless of growing queues, inflating mean latency by 2.4$\times$ under high load. Conversely, a cost-minimizing router over-allocates traffic to the cheapest model, leaving capable instances underutilized and capping aggregate cluster throughput. This paper presents RouteBalance, a serving scheduler that unifies model routing and instance dispatching into a single decision. RouteBalance dynamically batches incoming requests into short, load-adaptive rounds. In each round, it amortizes quality and response-length estimation across candidate models, takes a single snapshot of all instance loads, and solves a normalized assignment problem balancing quality, cost, and estimated latency. On a 28-GPU heterogeneous cluster spanning four Qwen model sizes and diverse GPU architectures, RouteBalance Pareto-dominates 231 of 246 baseline configurations across quality, latency, and cost simultaneously. These baselines comprise combinations of two learned routers with four downstream dispatchers, as well as five standalone dispatchers. At iso-quality, per-rate median reductions across baselines are 23--60% in mean E2E latency and 26--37% in serving cost. Code: https://github.com/AKafakA/route-balance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing, model routing
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Wei Da, Evangelia Kalyvianaki
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/AKafakA/route-balance](https://github.com/AKafakA/route-balance)
- 阅读深度：metadata
