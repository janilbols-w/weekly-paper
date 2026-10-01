---
title: "MoEless: Efficient MoE LLM Serving with Serverless Experts"
description: "Large Language Models (LLMs) increasingly adopt Mixture-of-Experts (MoE) architectures to scale efficiently under stringent resource constraints."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2603.06350) · [PDF](https://arxiv.org/pdf/2603.06350)

## 一句话摘要

Large Language Models (LLMs) increasingly adopt Mixture-of-Experts (MoE) architectures to scale efficiently under stringent resource constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) increasingly adopt Mixture-of-Experts (MoE) architectures to scale efficiently under stringent resource constraints. However, MoE's sparse activation causes severe expert load imbalance, where a few experts become stragglers while others remain underutilized, leading to inflated inference latency and cost. Existing solutions assume static, serverful model deployments, limiting expert elasticity and often incurring costly expert swapping or degraded output quality. We present MoEless, an efficient serverless MoE serving framework that mitigates expert load imbalance via elastic expert execution. MoEless leverages lightweight, layer-aware predictors to estimate incoming expert load distributions and proactively identify stragglers. We design optimized scaling and placement strategies to improve function locality, GPU utilization, and cross-expert load balance. MoEless is prototyped on top of Megatron-LM and deployed on an eight-GPU testbed. Experiments with open-source MoE models and real-world workloads show that MoEless reduces inference latency by 43% and inference cost by 84% compared to state-of-the-art solutions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hanfei Yu, Bei Ouyang, Shwai He, Ang Li, Hao Wang
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
