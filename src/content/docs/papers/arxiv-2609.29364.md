---
title: "NebulaSD: Many-for-Many Speculative Decoding"
description: "Speculative decoding accelerates Large Language Model (LLM) inference by using a lightweight draft model to propose candidate tokens for parallel verification by a target model."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.29364) · [PDF](https://arxiv.org/pdf/2609.29364)

## 一句话摘要

Speculative decoding accelerates Large Language Model (LLM) inference by using a lightweight draft model to propose candidate tokens for parallel verification by a target model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates Large Language Model (LLM) inference by using a lightweight draft model to propose candidate tokens for parallel verification by a target model. Drafting and verification, however, exhibit different service characteristics and favor different batch configurations, making fixed draft-target coupling inefficient under concurrent workloads. Existing distributed designs can physically separate the two stages, but often retain request or batch affinities that prevent their capacities from being shared globally. We present NebulaSD, a many-for-many, or M-for-N, speculative decoding system that organizes draft and target workers into independently schedulable resource pools and dynamically reconstructs stage-specific batches from shared request pools. Such dynamic reassignment removes fixed worker locality, requiring request states to be made available at newly selected workers without introducing migration stalls. NebulaSD addresses this challenge through worker-triggered batch reconstruction and asynchronous KV-state preparation overlapped with model execution. We evaluate NebulaSD from both system and scaling perspectives, showing that dynamic pooling improves request-round processing rate by 50.4% over a physically disaggregated baseline and 72.6% over co-located execution on a four-GPU deployment while substantially increasing effective GPU utilization. Profile-driven simulations further show approximately proportional compute-side capacity scaling under idealized state movement.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junhao He, Hongyang Du
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
