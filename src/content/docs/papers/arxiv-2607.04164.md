---
title: "BrownoutMoE: Learning Structure-Aware Expert Grouping for Adaptive Mixture-of-Experts Model Serving"
description: "Mixture-of-Experts (MoE) large language models (LLMs) are increasingly served on multi-GPU clusters in cloud data centers, where inference must stay accurate and responsive under bursty demand."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2607.04164) · [PDF](https://arxiv.org/pdf/2607.04164)

## 一句话摘要

Mixture-of-Experts (MoE) large language models (LLMs) are increasingly served on multi-GPU clusters in cloud data centers, where inference must stay accurate and responsive under bursty demand.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) large language models (LLMs) are increasingly served on multi-GPU clusters in cloud data centers, where inference must stay accurate and responsive under bursty demand. Expert access in MoE inference is highly imbalanced: a few hot experts process most tokens, whereas many cold experts fragment kernels and leave GPU parallelism underused. Existing serving systems optimize runtime execution but keep the original expert organization. We propose BrownoutMoE, a structure-aware serving framework inspired by the brownout paradigm in cloud computing. It learns layer-wise expert grouping offline with reinforcement learning, using the post-distillation error as the reward. Grouping-consistent distillation trains one united expert per group, and an online controller adjusts how often united experts replace cold experts under latency objectives. On eight A100 GPUs, BrownoutMoE reduces accuracy degradation by up to 71.4% relative to index-order grouping, improves unfused throughput by up to 2.24x over vLLM, and lowers saturated decode latency by 38%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yi Ding, Minxian Xu, Zhengxin Fang, Kejiang Ye, Chengzhong Xu
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
