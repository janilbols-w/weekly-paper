---
title: "SpikeDuet: CPU-Accelerator Co-Execution of Sparse SNNs on Commodity MCUs"
description: "Spiking neural networks (SNNs) expose sparse event activity, but commodity microcontrollers increasingly pair general-purpose processors with dense matrix-vector accelerators whose suitability for sparse inference is unclear."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.24677) · [PDF](https://arxiv.org/pdf/2610.24677)

## 一句话摘要

Spiking neural networks (SNNs) expose sparse event activity, but commodity microcontrollers increasingly pair general-purpose processors with dense matrix-vector accelerators whose suitability for sparse inference is unclear.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking neural networks (SNNs) expose sparse event activity, but commodity microcontrollers increasingly pair general-purpose processors with dense matrix-vector accelerators whose suitability for sparse inference is unclear. We investigate whether the on-chip Matrix Vector Processor (MVP) of the EFR32MG24 can accelerate SNN inference beyond optimized event-driven Cortex-M33 execution. Our automated snnTorch-to-C deployment flow combines hardware-calibrated engine selection, function-preserving neuron reordering that places co-active neurons adjacently for the accelerator, and asynchronous scheduling that overlaps CPU and MVP computation. On physical hardware, heterogeneous execution achieves 1.27--1.87$\times$ speedup and 11--34\% lower energy per inference than optimized sparse Cortex-M33 execution across five evaluated network configurations, while the smallest Braille network remains CPU-optimal. Reordering alone moves Braille-384's dominant hidden layer from the CPU to the MVP, and its benefit persists under asynchronous execution. These results show that activity locality and concurrency between CPU and MVP can jointly improve sparse SNN inference on commodity MCUs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Muhammad Fahd Ibrahim Bhatti, Muhammad Ali Siddiqi
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
