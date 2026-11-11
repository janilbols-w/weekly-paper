---
title: "RecoGEM: A Serving System for Production-Scale Generative Recommendation"
description: "Generative recommendation (GR) is moving industrial recommender systems (RecSys) from scoring candidate items to autoregressively generating item identifiers."
---

**评分：41/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.12296) · [PDF](https://arxiv.org/pdf/2611.12296)

## 一句话摘要

Generative recommendation (GR) is moving industrial recommender systems (RecSys) from scoring candidate items to autoregressively generating item identifiers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Generative recommendation (GR) is moving industrial recommender systems (RecSys) from scoring candidate items to autoregressively generating item identifiers. This shift promises higher recommendation quality, but makes serving substantially harder: each request executes a short sequence of dependent decoding steps that explore a large item space and select promising candidates on the latency-critical path. GR not only creates structural mismatches with conventional RecSys pipelines, but also challenges the architectural and optimization assumptions of LLM serving stacks, making direct adoption of existing systems difficult. We present RecoGEM, our production GR serving system. RecoGEM uses a runtime--engine decoupling architecture to move GR-specific serving responsibilities, such as candidate-state transitions and live artifact updates, to a dedicated runtime. Its execution engine exploits GR's short token sequences, large candidate populations, and predictable step shapes to optimize self-attention, candidate selection, and execution planning. RecoGEM has been deployed for over nine months across our production lines, serving applications with hundreds of millions of users and supporting more than ten GR model families. On our OneModel production workloads, RecoGEM reaches over 1,000 QPS per serving instance with P99 latency below 35 ms and a 2.88$\times$ throughput improvement over representative baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiangrui Yang, Yunfeng Zhao, Jiawei Yang, Fangyu Zhang, Enrui Zhao, Liang Zeng, Cheng Peng, Minhui Xie, Jiaqiang Liu, Xiao Liang, Yiming Qiu
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
