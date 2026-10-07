---
title: "FailBench: Evaluating Fault Tolerance Across Distributed Training Architectures"
description: "Distributed deep learning relies on data, pipeline, tensor, and hybrid parallelism, yet fault-tolerance mechanisms are typically evaluated only on the architecture for which they were designed."
---

**评分：54/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.07688) · [PDF](https://arxiv.org/pdf/2610.07688)

## 一句话摘要

Distributed deep learning relies on data, pipeline, tensor, and hybrid parallelism, yet fault-tolerance mechanisms are typically evaluated only on the architecture for which they were designed.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed deep learning relies on data, pipeline, tensor, and hybrid parallelism, yet fault-tolerance mechanisms are typically evaluated only on the architecture for which they were designed. This leaves practitioners with little guidance when choosing mechanisms across architectures. FailBench provides a unified evaluation harness covering seven distributed training architectures, eight crash-fault-tolerance mechanisms and a no-FT baseline, and single, concurrent, and cascading fail-stop failures. We evaluate 142 (architecture, mechanism, trace) combinations on an 8xV100 cluster, with per-rank checkpoint states ranging from 205 MB to 2.7 GB. Three findings emerge. First, no mechanism is universally best: on A2, disk checkpointing has the lowest steady-state overhead (0.5%), in-memory replication restores fastest (~17 ms), and just-in-time checkpointing avoids periodic steady-state checkpoint cost but incurs ~0.9 s upon failure. When process-group re-formation takes seconds, mechanisms differ more in runtime overhead than restore speed. Second, gossip training increases sample throughput by 17.9% after losing a worker, yet shows no detectable improvement in loss progress over a matched no-fault baseline. Third, mechanism cost depends strongly on architecture: in-memory replication overhead ranges from 3.7% to 176%. We translate these findings into a decision framework for selecting fault-tolerance mechanisms and release FailBench as an open artifact.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint, checkpointing, distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Khaled Aljbab, Amine Barrak
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
