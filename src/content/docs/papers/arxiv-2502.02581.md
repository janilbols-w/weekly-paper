---
title: "Themis: Efficient Sparse Model Training Through Fully Sharded Sparse Data Parallelism"
description: "Mixture-of-Experts (MoE) scales large language models cost-effectively, but expert-parallel training suffers severe straggler effects from skewed expert loads."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2502.02581) · [PDF](https://arxiv.org/pdf/2502.02581)

## 一句话摘要

Mixture-of-Experts (MoE) scales large language models cost-effectively, but expert-parallel training suffers severe straggler effects from skewed expert loads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) scales large language models cost-effectively, but expert-parallel training suffers severe straggler effects from skewed expert loads. Current systems frequently rearrange expert placement to mitigate stragglers, inflating memory footprint and migration overhead, potentially negating the benefits of load balancing. We present Fully Sharded Sparse Data Parallelism (FSSDP), a sparse-native MoE training approach that enables in-situ load balancing on every training iteration, overlapping the balancing with computation and eliminating explicit expert rearrangement together with its migration traffic and memory reserves. FSSDP keeps MoE layers sharded and sparsely materializes an ephemeral, load-balancing placement each iteration, with re-materialization to reuse available memory across layers. FSSDP is complemented by heterogeneous sharding to shift memory imbalance from the device level to the layer level, maintaining uniform memory budgets while enabling per-layer placement optimization. We realize FSSDP in Themis with co-designed topology-aware placement algorithms. Across 2 clusters and diverse workloads, Themis achieves 1.26-2.42x speedup over state-of-the-art expert-rearrangement systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: straggler
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yuhao Qing, Guichao Zhu, Lintian Lei, Fanxin Li, Shixiong Zhao, Zekai Sun, Xiuxian Guan, Xusheng Chen, Dong Huang, Ping Luo, Yiming Qiu, Heming Cui
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
