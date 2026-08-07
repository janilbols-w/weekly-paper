---
title: "A Time-Multiplexed Spiking Neural Network Accelerator with Pipelined Readout for FPGA Inference"
description: "Spiking Neural Networks (SNNs) provide a power-efficient neuromorphic alternative to traditional artificial neural networks by processing information through discrete temporal events."
---

**评分：49/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.00595) · [PDF](https://arxiv.org/pdf/2608.00595)

## 一句话摘要

Spiking Neural Networks (SNNs) provide a power-efficient neuromorphic alternative to traditional artificial neural networks by processing information through discrete temporal events.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking Neural Networks (SNNs) provide a power-efficient neuromorphic alternative to traditional artificial neural networks by processing information through discrete temporal events. This paper presents the design and Field-Programmable Gate Array (FPGA) implementation of an inference-only SNN accelerator optimized for MNIST digit classification. To address the physical routing constraints and timing bottlenecks inherent in low-cost devices, we propose an optimized hardware microarchitecture featuring a time-multiplexed 1-bit spike-feeding mechanism governed by a finite state machine (FSM), localized distributed memory for weight storage, and an integer-based Leaky Integrate-and-Fire (LIF) neuron model with register widths selected to prevent overflow. In addition, a multi-cycle pipelined argmax and tie-breaker readout module eliminates the dominant combinational critical path. Implemented on an entry-level AMD Artix-7 FPGA (XC7A200T) using a 784-64-10 network topology, the proposed pipelined architecture increases the maximum operating frequency (Fmax) from 13.3 MHz to 167 MHz. Hardware evaluation demonstrates a sequential processing latency of 82 {\mu}s per image, enabling a 1,000-sample VHDL simulation batch to be completed in 0.082 s. Vivado post-implementation vector-based power analysis estimates the total on-chip power consumption at 0.336 W and the energy efficiency at approximately 36,300 samples per joule. These results demonstrate that the proposed microarchitecture provides a resource-efficient solution for real-time neuromorphic edge inference, provided that the network size remains within the practical limits of time-multiplexed execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator, edge inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Reza Ansari, Maciej Wielgosz
- 发布：2026-08-01；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
