---
title: "You Only Charge Once 2.0 : A End-to-End Analog Computing-in-Memory Architecture with Reconfigurable Switched Capacitors"
description: "Analog Computing-in-Memory (ACiM) accelerates deep neural networks by keeping weights inside memory arrays and executing dot products in the analog domain."
---

**评分：51/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.11116) · [PDF](https://arxiv.org/pdf/2608.11116)

## 一句话摘要

Analog Computing-in-Memory (ACiM) accelerates deep neural networks by keeping weights inside memory arrays and executing dot products in the analog domain.

## 为什么值得关注

待编辑增强。

## 摘要原文

Analog Computing-in-Memory (ACiM) accelerates deep neural networks by keeping weights inside memory arrays and executing dot products in the analog domain. However, modern ACiM accelerators are often limited by the "ADC wall": analog-to-digital converters consume a large fraction of energy and area, while bit-sliced execution repeatedly invokes these converters. Existing designs reduce this cost with low-resolution readout or time multiplexing, but they either lose output fidelity or introduce serialization overhead. Charge-CIM addresses this bottleneck by using switched-capacitor charge redistribution as a unified computing and conversion substrate. The same capacitor fabric performs input conversion, analog MAC, weighted shift-and-add, and readout quantization, reducing both standalone converter overhead and intermediate ADC invocations. A differential readout path further combines paired partial sums during ADC quantization, providing a highly compact and energy-efficient solution for array integration. With dataflow architecture support, we evaluated Charge-CIM on a suite of DNN benchmarks, from CNNs to Transformer models, and experimental results show that Charge-CIM reduces ADC energy by 91.7% under our evaluation setup and improves energy efficiency by 2.7x and throughput by 2.0x compared to the state-of-the-art charge-domain CIM accelerator.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zihao Xuan, Yewen Li, Jia Chen, Wei Xuan, Xiao Huo, Fengbin Tu
- 发布：2026-08-11；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
