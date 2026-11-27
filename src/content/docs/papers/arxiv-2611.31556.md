---
title: "Real-Time AI Acceleration on a 2D Spatial Dataflow Architecture"
description: "Machine Learning (ML) is increasingly being integrated into real-time systems, which makes the timing analysis of ML accelerators necessary."
---

**评分：40/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.31556) · [PDF](https://arxiv.org/pdf/2611.31556)

## 一句话摘要

Machine Learning (ML) is increasingly being integrated into real-time systems, which makes the timing analysis of ML accelerators necessary.

## 为什么值得关注

待编辑增强。

## 摘要原文

Machine Learning (ML) is increasingly being integrated into real-time systems, which makes the timing analysis of ML accelerators necessary. However, the most popular commercial accelerator, the Graphics Processing Unit (GPU), remains difficult to analyze as several aspects of its behavior, including scheduling of threads involved in single-instruction multiple-thread computations and memory access latency, are not fully documented. Spatial dataflow accelerators present an interesting alternative to GPUs, as they inherently support compute and memory partitioning. Data movement and computation locality are explicitly controlled by the programmer. In this work, we consider the Tenstorrent Blackhole, which is based on a commodity RISC-V architecture. It consists of a 2D grid of cores connected by Networks-on-Chip (NoCs), supporting a fully open software runtime. We profile the Blackhole platform and develop a worst-case execution time task model as a Homogeneous Synchronous Dataflow Graph. We extend this model to a preliminary analysis of multi-core workloads by considering NoC-related delays. Finally, we evaluate our model across 12,567 task configurations and workloads. Results show that the estimate derived from our model lies above the observed worst case in every configuration. For single-core workloads, the overhead is less than 100% in most cases, with a maximum of less than 200%, and for multi-core workloads, it is less than 500% using a pessimistic NoC contention analysis. This paper lays the foundations for real-time computing on a promising open accelerator design.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shriram Raja, Anton Njavro, Richard West
- 发布：2026-11-23；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
