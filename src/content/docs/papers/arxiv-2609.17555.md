---
title: "REQAP: Resilient Weight Packing and Quantization for Edge DNN Acceleration"
description: "Efficient deployment of Deep Neural Networks (DNNs) on edge accelerators requires aggressive model compression while maintaining reliability in fault-prone hardware environments."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.17555) · [PDF](https://arxiv.org/pdf/2609.17555)

## 一句话摘要

Efficient deployment of Deep Neural Networks (DNNs) on edge accelerators requires aggressive model compression while maintaining reliability in fault-prone hardware environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficient deployment of Deep Neural Networks (DNNs) on edge accelerators requires aggressive model compression while maintaining reliability in fault-prone hardware environments. This paper presents a reliability-aware quantized weight packing methodology for systolic-array-based DNN accelerators. A sensitivity-driven mixed-precision quantization framework assigns layer-wise bit-widths according to accuracy impact while enforcing symmetric precision between weights and activations. A deterministic register-level packing strategy consolidates multiple heterogeneous operand pairs into fixed-width register words, enabling SIMD-within-a-register (SWAR) style parallel execution that reduces both memory footprint and execution cycles. To improve resilience against hardware faults, selective bit-level protection replicates the most significant bits (MSBs) of critical layers into unused register space, achieving TMR-style protection with minimal overhead. A systolic-array simulation framework is developed to evaluate the proposed packing and fault-tolerance mechanisms under realistic execution conditions. Simulations in AlexNet, VGG-11, and ResNet-18 demonstrate up to 62% memory reduction and up to 56% reduction in Multiply-Accumulate (MAC) operations, while significantly improving accuracy resilience under fault injection compared to baseline and fully protected models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mahdi Taheri, Samira Nazari, Mubassher Ansari, Ali Azarpeyvand, Mohsen Afsharchi, Maksim Jenihhin, Christian Herglotz
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
