---
title: "Deep Microcompression: Structured Pruning and Bit-packed Quantization for Microcontrollers"
description: "This paper introduces Deep Microcompression (DMC), a hardware-aware pipeline for deep learning inference on bare-metal microcontrollers."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.05081) · [PDF](https://arxiv.org/pdf/2609.05081)

## 一句话摘要

This paper introduces Deep Microcompression (DMC), a hardware-aware pipeline for deep learning inference on bare-metal microcontrollers.

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper introduces Deep Microcompression (DMC), a hardware-aware pipeline for deep learning inference on bare-metal microcontrollers. DMC integrates structured pruning, quantization-aware training, and fixed-length bit-packing to achieve a 55.8$\times$ weight compression ratio on LeNet-5 (98.77\% accuracy), generating a dependency-free C library with deterministic latency. On the RP2040 (Cortex-M0+), DMC reduces binary size by 3$\times$ versus TensorFlow Lite while matching its accuracy. Critically, DMC enables the first documented deployment of a standard CNN on the ATmega328P, a device constrained to 2KB SRAM, previously considered infeasible for CNN inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Opegbemi Matthias Busoye, Tolulope Matthew Busoye, Eghonghon-aye Eigbe
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
