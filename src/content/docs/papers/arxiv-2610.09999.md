---
title: "ReSAFT: An Efficient Stuck-at Fault-Tolerant Scheme for ReRAM-based Process-in-Memory Accelerators"
description: "Analog ReRAM-based process-in-memory (PIM) accelerators provide high parallelism and energy efficiency for deep convolutional neural networks (CNNs) inference."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.09999) · [PDF](https://arxiv.org/pdf/2610.09999)

## 一句话摘要

Analog ReRAM-based process-in-memory (PIM) accelerators provide high parallelism and energy efficiency for deep convolutional neural networks (CNNs) inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Analog ReRAM-based process-in-memory (PIM) accelerators provide high parallelism and energy efficiency for deep convolutional neural networks (CNNs) inference. However, their susceptibility to permanent faults, such as stuck-at high (SaH) and stuck-at low (SaL) resistance states, poses a major challenge by permanently corrupting the CNN weights mapped to conductance values of ReRAM cells and degrading inference accuracy, which leads to system unreliability in safety-critical applications. In this paper, we propose a fault-tolerant scheme for analog ReRAM-based PIM accelerators to tackle stuck-at faults (SAFs) with minimal redundancy overhead to recover classification accuracy degradation. The proposed scheme contains a redundancy-based hardware solution alongside fault-aware mapping method for ensuring reliable analog computation in ReRAM crossbar. We analyze the impact of varying number of redundant rows and columns on accuracy and design metrics. Subsequently, a multi-objective optimization (MOO) problem is formulated and solved to efficiently determine the number of redundant rows and columns, considering trade-offs among various design metrics. Furthermore, a fault-aware weight mapping is proposed for dual-crossbar structures to further compensate for the accuracy degradation caused by SAFs. Simulation results show that, for the SimpleNet model using the MNIST dataset, the inference accuracy is recovered by approximately 22.39%, on average, across four configurations of optimal solutions, each offering a trade-off between reliability and area, energy consumption, and latency overheads. The mean-time-tofailure (MTTF) improves by about 61x on average compared to the baseline. These selected configurations also reduce energy and area overheads by 32%, on average, in comparison to row-only and column-only configurations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aniseh Dorostkar, Hamed Farbeh, Hamid R. Zarandi
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
