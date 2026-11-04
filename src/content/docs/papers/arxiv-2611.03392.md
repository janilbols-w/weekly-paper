---
title: "TinyML Hits the Memory Wall: A Benchmark of Ten Sub-Watt Edge Devices"
description: "Neural network inference at the edge must fit tight energy budgets."
---

**评分：46/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.03392) · [PDF](https://arxiv.org/pdf/2611.03392)

## 一句话摘要

Neural network inference at the edge must fit tight energy budgets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Neural network inference at the edge must fit tight energy budgets. Existing benchmarks compare few devices, do not report energy on a common basis, and omit the newest microcontrollers with an NPU or the 1 GHz Cortex-M85. Hardware-aware design also ranks networks by MAC count, yet no study has tested whether this proxy holds across accelerators. We benchmark sub-watt edge AI hardware by evaluating four CNNs (MobileNetV3, MCUNetV1, EfficientNet, SqueezeNet) and two tiny transformers (MobileViT-XXS, DeiT-tiny) on ten commercial devices: an in-sensor DSP (Sony IMX500), four MCUs with an NPU (STM32N6, Alif Ensemble E7/E8, GreenWaves GAP9), and five MCUs without an NPU (STM32U5, Apollo510B, ESP32-S3 Xtensa LX7, RA8M2, STM32V8). Four devices are novel (Alif E8, Apollo510B, RA8M2, STM32V8). Measured as energy above idle, the IMX500 (0.13-0.35 mJ) uses 1.3-3x less energy than the STM32N6 (0.31-1.05 mJ) on every model; the GAP9 uses the least on MobileNetV3 and the Alif E7 the least on MCUNetV1 and SqueezeNet. All four use 6-34x less energy than the STM32V8 (1.85-3.98 mJ), and the Alif E7 and IMX500 form the power-performance Pareto front. Latency on all four accelerators scales with memory traffic (bytes of weights and activations, r >= 0.98) and not with MACs, so they are memory-bound, while no MCU without an NPU is. The NPU advantage grows with intensity from 1.4x over a 1 GHz Cortex-M85 on MCUNetV1 to 8.2x on SqueezeNet. MAC count is therefore a misleading cost proxy for sub-watt accelerators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Pietro Bonazzi, Luigi Capogrosso, Ahmet Celik, Rosanna Manzo, Marco Giordano, Szymon Ruci\'nski, Jonathan Hungerbuehler, Michele Magno
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
