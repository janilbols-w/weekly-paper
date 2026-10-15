---
title: "STISA: A 0.16 GOPS/W/PE Single-Shot Inference FPGA-based SNN Accelerator with Algorithm and Hardware Co-Design"
description: "Spiking neural networks (SNNs) offer great potential for low-power intelligent computing owing to their event-driven nature, yet their deployment is limited by high inference latency and inefficient hardware utilization caused by temporal dependencies."
---

**评分：46/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.19973) · [PDF](https://arxiv.org/pdf/2610.19973)

## 一句话摘要

Spiking neural networks (SNNs) offer great potential for low-power intelligent computing owing to their event-driven nature, yet their deployment is limited by high inference latency and inefficient hardware utilization caused by temporal dependencies.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking neural networks (SNNs) offer great potential for low-power intelligent computing owing to their event-driven nature, yet their deployment is limited by high inference latency and inefficient hardware utilization caused by temporal dependencies. Existing accelerators struggle to balance timesteps, accuracy, and energy efficiency, while hardware-oriented timestep compression remains underexplored. To address these challenges, this work presents STISA, a unified algorithm-hardware co-design framework featuring: (i) a Temporal Splitter Compression (TSC) technique with a Temporal Split Structure (TSS) to reduce temporal redundancy while preserving network dynamics; (ii) a hardware-efficient spatiotemporal parallelism scheme, which co-optimizes dataflow and architecture through a Temporal-Prioritized Output-Stationary (TPOS) mapping and a flexible Block-Mux Streaming (BMS) architecture; and (iii) a joint TSC-TPOS-BMS co-optimization framework featuring a bandwidth-aware resource allocation strategy to achieve balanced accuracy, latency, and energy efficiency across diverse network architectures. On the algorithmic side, TSC reduces synaptic operations by 24.44%-51.71% while achieving competitive accuracies of 96.38%, 81.10%, 68.51%, and 82.40% on CIFAR-10, CIFAR-100, ImageNet, and DVS-CIFAR10, respectively. On the hardware side, FPGA prototypes deliver up to 7.99 speedup, 30.4% power reduction, and 30.1% LUT reduction. Compared with state-of-the-art SNN accelerators, STISA achieves 0.16 GOPS/W/PE, demonstrating its scalability and superior energy efficiency for real-time SNN inference under constrained hardware resources.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kainan Wang, Chengyi Yang, Lei Liu, Chengting Yu, Yee Sin Ang, Bo Wang, Aili Wang
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
