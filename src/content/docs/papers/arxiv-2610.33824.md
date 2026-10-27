---
title: "Adapting DNNs to Embrace Voltage Scaling Induced Errors via Accumulation-Aware Quantization"
description: "The pervasive deployment of Deep Neural Networks (DNNs) across the computing spectrum has brought growing attention to energy efficiency, alongside raw performance."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.33824) · [PDF](https://arxiv.org/pdf/2610.33824)

## 一句话摘要

The pervasive deployment of Deep Neural Networks (DNNs) across the computing spectrum has brought growing attention to energy efficiency, alongside raw performance.

## 为什么值得关注

待编辑增强。

## 摘要原文

The pervasive deployment of Deep Neural Networks (DNNs) across the computing spectrum has brought growing attention to energy efficiency, alongside raw performance. While voltage scaling is a potent knob for power reduction, its application in next-generation nodes is hampered by severe throughput degradation and susceptibility to process variation. This work aims to address these energy-reliability trade-offs by introducing a hardware-software co-design methodology, based on the observation that timing-robust bit ranges within the accumulator of a systolic array vary significantly across different voltage-frequency operating points. At the software level, we propose an Accumulation-Aware Training approach that incorporates this information as a first-order optimization constraint during training. By integrating mixed-precision quantization with unstructured pruning, we effectively constrain the model's weight distribution to avoid activating the hardware's sensitized high-rank carry chains. At the architectural level, we complement this with selective MSB-masking and fine-grained clock-gating to minimize unnecessary dynamic switching activity. Furthermore, we employ a layer-wise Dynamic Frequency Scaling strategy to further adapt to the accumulator's reduced dynamic range, based on the numerical sensitivity of each layer. We experimentally evaluate the proposed solution on a deep scaled 2nm technology node and demonstrate that, when operating at a low-voltage frontier, our co-optimized post-layout architecture delivers substantial energy and energy-delay product gains of 39% and 23% respectively, relative to the nominal voltage implementation, while maintaining accuracy degradation within 1%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Alexis Maras, Panagiotis Chaidos, Georgios Alexandris, Dimitrios Soudris, Sotirios Xydis
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
