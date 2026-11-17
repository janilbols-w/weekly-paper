---
title: "Fuse-All MoE Inference Kernel with Load Balancing on TPUs"
description: "Mixture-of-Experts (MoE) architectures activate only a subset of experts for each token, allowing large language models (LLMs) to scale parameter capacity without a proportional increase in computation per token."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2611.17857) · [PDF](https://arxiv.org/pdf/2611.17857)

## 一句话摘要

Mixture-of-Experts (MoE) architectures activate only a subset of experts for each token, allowing large language models (LLMs) to scale parameter capacity without a proportional increase in computation per token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) architectures activate only a subset of experts for each token, allowing large language models (LLMs) to scale parameter capacity without a proportional increase in computation per token. However, intermediate data movement and uneven expert loads limit the efficiency of MoE inference on TPUs. To address these bottlenecks, we introduce Fuse-All MoE, a TPU kernel design that jointly optimizes expert computation, output communication, and load balancing. The kernel fuses token collection, expert projections, gated activation, and output writes, retaining expert computation intermediates on chip. Fixed token-slot destinations allow scheduling and expert placement to change while preserving routing semantics. In prefill-decode (PD) disaggregated serving, Fuse-All MoE balances EP16 prefill workloads through scheduling and expert redistribution, while symmetric EP8TP2 shares active expert computation between the two TensorCore devices within each chip during decode. Our experiments show that Fuse-All MoE reduces kernel runtime for a measured skewed EP16 prefill workload from 2.3x to 1.09x the same fixed reference time for a balanced workload. Across 32-512 decode tokens, symmetric EP8TP2 reduces kernel latency by up to 21.3% relative to fused EP16. With accompanying serving stack optimizations, the integrated system improves serving throughput by up to 34.5% over the Megablox EP16 baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rupeng Liu, Bangsheng Tang, Zongwei Zhou, Chengji Yao, Yejin Lee
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
