---
title: "Partition-Aware Scheduling for Mobile Heterogeneous Inference Co-Execution"
description: "Modern mobile inference runs on heterogeneous platforms combining mobile GPUs with multiple CPU core clusters."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.14213) · [PDF](https://arxiv.org/pdf/2609.14213)

## 一句话摘要

Modern mobile inference runs on heterogeneous platforms combining mobile GPUs with multiple CPU core clusters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern mobile inference runs on heterogeneous platforms combining mobile GPUs with multiple CPU core clusters. Existing optimizations typically exploit either inter-operator parallelism, by assigning entire operators to CPU cores or to the GPU, or intra-operator parallelism, by partitioning each operator for CPU-GPU co-execution. We consider these two forms of parallelism together, to improve inference latency of tasks that can be represented by a static DAG of operators with predefined input/output tensor shapes (e.g., CNNs or vision transformers). We define the problem of partition-aware DAG scheduling for mobile heterogeneous inference, illustrating that the best strategy depends on the structure of the inference DAG, thus motivating a joint formulation capturing operator partition choices, device assignment, and execution order. We propose an online iterative search framework, which decomposes large DAGs into stages, focuses search on critical operators, and uses latency predictors to estimate partitioned execution without exhaustive profiling. Across representative mobile inference workloads, our approach achieves latency close to an offline solution while keeping scheduling overhead to a fraction of the model initialization cost, allowing platform-specific scheduling at deployment time.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: heterogeneous inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhuojin Li, Marco Paolieri, Leana Golubchik
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
