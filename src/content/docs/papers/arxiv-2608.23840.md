---
title: "ShardMeter: Sharded and Geo-Distributed Training Without the Guesswork"
description: "Training large-scale AI models often outgrows a single data center, demanding sharded, multi-cluster, and decentralized training."
---

**评分：49/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.23840) · [PDF](https://arxiv.org/pdf/2608.23840)

## 一句话摘要

Training large-scale AI models often outgrows a single data center, demanding sharded, multi-cluster, and decentralized training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training large-scale AI models often outgrows a single data center, demanding sharded, multi-cluster, and decentralized training. However, the huge space of resource allocations makes exhaustive benchmarking and manual tuning impractical, while performance depends on tightly coupled factors like model size, GPU memory, batch size, bandwidth, and sharding strategy. We introduce ShardMeter, a lightweight analytical performance model that predicts the end-to-end runtime of transformer-based workloads across arbitrary sharded, distributed, and even decentralized training. Given a model's characteristics and a target hardware topology, ShardMeter estimates per-GPU and per-island throughput, training cost, total wall-clock time, and identifies performance bottlenecks. Our analysis reveals diminishing-return regimes as island size increases, quantifies transitions between compute- and communication-bound scaling, evaluates hyperparameter trade-offs, and models cost-throughput for large-scale decentralized training. ShardMeter exposes these insights to quickly explore the configuration space, choose near-optimal deployment plans, and avoid costly trial and error.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tim Beringer, Patrick Diem, Felix Wolf, Arya Mazaheri
- 发布：2026-08-24；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
