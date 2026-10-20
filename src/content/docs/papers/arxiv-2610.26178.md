---
title: "GeoTrain: Energy-Aware Automatic Parallelism for Foundation Model Training on Heterogeneous Geo-Distributed Resources"
description: "Training foundation models at the frontier typically requires large-scale dedicated and centralized clusters with fast interconnects - infrastructure that is prohibitively expensive and generally accessible only to well-resourced organizations."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.26178) · [PDF](https://arxiv.org/pdf/2610.26178)

## 一句话摘要

Training foundation models at the frontier typically requires large-scale dedicated and centralized clusters with fast interconnects - infrastructure that is prohibitively expensive and generally accessible only to well-resourced organizations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training foundation models at the frontier typically requires large-scale dedicated and centralized clusters with fast interconnects - infrastructure that is prohibitively expensive and generally accessible only to well-resourced organizations. Decentralized training over pooled, geographically distributed GPUs offers an alternative, but introduces substantial heterogeneity in compute, memory, power, and network performance. Existing distributed training systems are primarily designed for clusters with fast, low-latency interconnects and typically use all available GPUs when configuring parallel training. In geo-distributed environments, however, slower devices and weak network links can become bottlenecks, while optimizing solely for throughput overlooks significant energy cost. We present GeoTrain, an automatic parallelism system that jointly optimizes training performance and energy consumption for heterogeneous geo-distributed GPU environments. GeoTrain simultaneously selects GPUs, partitions model layers, and determines pipeline configurations while accounting for heterogeneous compute, memory, power, and network constraints. To efficiently explore this large combinatorial search space, GeoTrain employs an optimized memetic algorithm with specialized genetic operators and local search. Experiments with decoder-only Transformer models on real-world and simulated heterogeneous topologies demonstrate that GeoTrain reduces iteration time and energy consumption by up to $61.4\%$ and $11.7\%$, respectively, over the existing state-of-the-art approaches. It also finds the exact optimum on verifiable instances and scales beyond exact methods as the number of GPUs increases, while exposing favorable energy-time trade-offs, including cases where its time-optimal distributed training plan is both faster and more energy-efficient than the baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bui-Khanh Hoang, TianZhang He, Mohammad Goudarzi
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
