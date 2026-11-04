---
title: "Token-as-a-Utility: A Model-Agnostic Architecture for Metering and Provisioning AI Inference Services"
description: "Token-based subscriptions are emerging as a commercial model for large language model inference, but extending them into interoperable utility services requires comparable consumption accounting."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.01371) · [PDF](https://arxiv.org/pdf/2611.01371)

## 一句话摘要

Token-based subscriptions are emerging as a commercial model for large language model inference, but extending them into interoperable utility services requires comparable consumption accounting.

## 为什么值得关注

待编辑增强。

## 摘要原文

Token-based subscriptions are emerging as a commercial model for large language model inference, but extending them into interoperable utility services requires comparable consumption accounting. Raw token counts do not consistently measure inference resource use because demand varies with model architecture, context length, tokenisation, and concurrent serving conditions. This paper presents Token-as-a-Utility, a model-agnostic architecture integrating inference metering, service-level-aware provisioning, and inter-operator settlement. We prove that, under batched serving, no per-request meter can be additive, independent of co-resident traffic, and exactly cost-reflective at once. This motivates separating provisioned capacity, metered consumption, and contracted quality into distinct service products. Consumption is expressed in Reference Inference Units (RIUs) derived from prefill and decode demand, while occupancy-indexed operator ratings recover shared serving costs without altering the common unit. Versioned inference records support auditing and re-rating across operators; software-enforced capacity leases and quality-constrained routing enable provisioning on shared accelerators. The resource model is measured on three NVIDIA RTX 5000 Ada GPUs, and multi-tenant behaviour is evaluated with a trace-driven model calibrated to them. For the reference model, occupancy-indexed rating limits statement energy error to 9% under measured traffic, compared with up to 70.5% under fixed-occupancy rating. In calibrated multi-tenant experiments, tenant mispricing decreases from 7.36 times under flat token counting to 2.39 times with RIUs and 1.06 times after occupancy-based reconciliation. These findings demonstrate how portable inference accounting can be combined with load-dependent cost recovery and contract-based provisioning to support heterogeneous inference services across operators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: heterogeneous inference
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yichiet Aun, Soung-Yue Liew, Yu Liang Lai, Jing Jie Tan, Dong Chen, Purnomo Husnul Khotimah
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
