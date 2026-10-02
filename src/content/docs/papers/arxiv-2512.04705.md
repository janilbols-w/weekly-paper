---
title: "Hardware-Algorithm Co-Optimization of Early-Exit Neural Networks for Multi-Core Edge Accelerators"
description: "The deployment of Early-Exiting Neural Networks (EENNs) on edge accelerators requires optimizing not only the network architecture but also its hardware deployment."
---

**评分：48/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2512.04705) · [PDF](https://arxiv.org/pdf/2512.04705)

## 一句话摘要

The deployment of Early-Exiting Neural Networks (EENNs) on edge accelerators requires optimizing not only the network architecture but also its hardware deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

The deployment of Early-Exiting Neural Networks (EENNs) on edge accelerators requires optimizing not only the network architecture but also its hardware deployment. Exit configuration, quantization, and hardware workload mapping interact in non-trivial ways, influencing memory traffic, accelerator utilization, and ultimately the energy-latency trade-off. This work presents a hardware-aware co-design framework for EENNs that jointly optimizes exit configuration, quantization-aware training, and multi-core hardware mapping within a unified NAS process. Leveraging analytical design space exploration, the framework identifies efficient workload mappings for each candidate architecture while providing accurate latency and energy estimates during the search. We further formulate EENN deployment as a constrained multi-objective optimization problem balancing predictive accuracy, energy-latency product, exit overhead, and dynamic inference efficiency. Experimental results on CIFAR-10 demonstrate that the proposed framework achieves over a 50\% reduction in energy-latency product compared with static baselines under 8-bit quantization. These results demonstrate that jointly optimizing architecture and deployment is essential for realizing the full efficiency potential of dynamic inference on heterogeneous edge accelerators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator, hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Alaa Zniber, Arne Symons, Ouassim Karrakchou, Marian Verhelst, Mounir Ghogho
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
