---
title: "Cross-Model Autoscaling for Shared LLM Serving"
description: "Multi-model LLM serving is moving toward shared MaaS clusters, where co-hosted models compete for a fixed GPU budget while each model experiences time-varying demand and must satisfy its own latency SLO."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2609.29160) · [PDF](https://arxiv.org/pdf/2609.29160)

## 一句话摘要

Multi-model LLM serving is moving toward shared MaaS clusters, where co-hosted models compete for a fixed GPU budget while each model experiences time-varying demand and must satisfy its own latency SLO.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-model LLM serving is moving toward shared MaaS clusters, where co-hosted models compete for a fixed GPU budget while each model experiences time-varying demand and must satisfy its own latency SLO. Existing LLM autoscalers remain largely model-local: their signals expose local runtime activity or delayed latency outcomes, and their scale-up or provisioning decisions do not directly determine how shared capacity should be allocated across competing models. We present the Token-service-share Rebalancing Engine (TRE), a control-plane framework for hot-switched multi-model LLM serving. TRE introduces Token Service Share (TSS), a calibrated, demand-normalized signal that estimates effective token service per active or queued request and yields a comparable health score across heterogeneous models and SLO classes. Guided by TSS, TRE coordinates bounded receiver--donor capacity movement under a fixed GPU budget: it separates fast rescue from slower rebalancing and incrementally reallocates active replicas toward models with the largest calibrated service deficits. We implement TRE on a Kubernetes-based hot-switch serving stack without modifying the inference scheduler. Across seven LLM serving traces, TRE reduces P95 end-to-end latency by 11.9--79.0\% and P99 latency by 12.5--72.6\% compared with a state-of-the-art KV-cache-based reactive autoscaler running on the same hot-switch runtime. The gains hold on both targeted stress probes and production-derived conversation/code traces, where TRE reduces P95/P99 latency by 50.8/63.7\% and 79.0/72.6\%, respectively. These results show that effective hot-switched autoscaling requires not only fast replica actuation, but also calibrated service-deficit signals and coordinated cross-model capacity arbitration. Our code and artifacts are available at https://github.com/zxzx9898/Token-service-share_Rebalancing_Engine.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: autoscaling
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xin Zhang, Xianyan Xie, Zhen He, Xijin Yin, Xingtong Lin, Bangbo Liang, Zequn Cheng, Peihao Huang, Guo Chen
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/zxzx9898/Token-service-share_Rebalancing_Engine](https://github.com/zxzx9898/Token-service-share_Rebalancing_Engine)
- 阅读深度：metadata
