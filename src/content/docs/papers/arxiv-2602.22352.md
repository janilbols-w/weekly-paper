---
title: "GRAU: A Generic Runtime-Reconfigurable Activation-Requantization Unit for Quantized Neural Network Accelerators"
description: "As neural networks continue to scale, low-precision quantization is widely adopted in edge accelerators, but conventional multi-threshold activation hardware requires 2^n-1 thresholds for n-bit integer outputs, leading to rapidly increasing hardware costs."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2602.22352) · [PDF](https://arxiv.org/pdf/2602.22352)

## 一句话摘要

As neural networks continue to scale, low-precision quantization is widely adopted in edge accelerators, but conventional multi-threshold activation hardware requires 2^n-1 thresholds for n-bit integer outputs, leading to rapidly increasing hardware costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

As neural networks continue to scale, low-precision quantization is widely adopted in edge accelerators, but conventional multi-threshold activation hardware requires 2^n-1 thresholds for n-bit integer outputs, leading to rapidly increasing hardware costs. We propose GRAU, a Generic Runtime-Reconfigurable Activation-Requantization Unit that fuses batch normalization, nonlinear activation, and requantization through piecewise-linear fitting with Power-of-Two slopes. GRAU requires only basic comparators and 1-bit right shifters, while supporting mixed-precision quantization and runtime switching among post-accumulation functions, including modern nonlinear activations such as SiLU and GELU. Compared with multi-threshold activation-requantization units, GRAU reduces LUT consumption by approximately 90% or more while improving hardware efficiency, flexibility, and scalability. We further explore the trade-off between accuracy and hardware cost across different approximation settings and provide an open-source toolchain for GRAU-aware network training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuhao Liu, Salim Ullah, Akash Kumar
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
