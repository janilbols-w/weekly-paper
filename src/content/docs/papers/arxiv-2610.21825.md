---
title: "Compiling Multi-Threshold Operators for Quantized Non-Monotonic and Fine-Granular Activations in Custom-Tailored DNN Accelerators"
description: "Aggressive quantization of neural networks can expose activation functions as bottlenecks for efficient hardware acceleration."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.21825) · [PDF](https://arxiv.org/pdf/2610.21825)

## 一句话摘要

Aggressive quantization of neural networks can expose activation functions as bottlenecks for efficient hardware acceleration.

## 为什么值得关注

待编辑增强。

## 摘要原文

Aggressive quantization of neural networks can expose activation functions as bottlenecks for efficient hardware acceleration. Implementing quantized activations as multi-threshold operations has been shown to be a promising optimization, allowing for efficient hardware implementation of few-bit activations. However, current implementations are limited to monotonically increasing functions, quantization schemes with one-dimensional (per-channel) granularity and a small set of predefined activation-quantizer combinations. We formalize the multi-threshold representation to extend it to non-monotonic functions and fine-granular parameters, i.e., multi-dimensional thresholds. For automated conversion of quantized function compositions into threshold representation, we propose a systematic approach via algebraic rules integrated into the ONNX-based compiler infrastructure. We experimentally validate our solution on a selection of monotonic and non-monotonic functions by extending the binary search based multi-threshold operator that is integrated into the FINN framework for end-to-end synthesis of custom-tailored FPGA accelerators. The cost of hardware support for non-monotonicity and fine-granularity is characterized in comparison to an alternative approach utilizing existing operators via graph-level decomposition. We compare our method to prior work as well as the approach taken by the hls4ml framework. As an outlook, we demonstrate the prospects of using the multi-threshold representation during the training of a neural network as a form of quantization aware training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Christoph Berganski, Felix Jentzsch, Marco Platzner
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
