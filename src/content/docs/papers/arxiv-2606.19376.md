---
title: "Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees"
description: "Inference costs for large language model (LLM) applications are rapidly growing, driven by surging demand and rising infrastructure cost."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2606.19376) · [PDF](https://arxiv.org/pdf/2606.19376)

## 一句话摘要

Inference costs for large language model (LLM) applications are rapidly growing, driven by surging demand and rising infrastructure cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Inference costs for large language model (LLM) applications are rapidly growing, driven by surging demand and rising infrastructure cost. Users expect high-quality responses, and in commercial settings this is formally codified in Service Level Agreements (SLAs), creating a fundamental tension between cost and quality. Recent progress on cost-aware LLM request routing has shown potential to resolve this tension, but existing approaches rely on complete feedback signals, offline training, extensive per-workload tuning, and most lack SLA guarantees or inference-time adaptivity. We introduce SLARouter, an online routing algorithm that learns a cost-optimal policy from the sparse, one-sided user feedback available in production systems. SLARouter provides theoretical guarantees for both cost optimality and strict SLA compliance. Experiments across a wide range of LLM benchmarks show that SLARouter satisfies SLA constraints without the need for per-benchmark tuning, reducing operating cost by up to 2.2x over existing baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: request routing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Herbert Woisetschl\"ager, Arastun Mammadli, Ryan Zhang, Shiqiang Wang
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
