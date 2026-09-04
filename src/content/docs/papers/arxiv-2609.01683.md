---
title: "FORGE: Forward-Only Test-Time Adaptation for Integer-Only Vision Models on Microcontrollers"
description: "Vision models deployed on microcontrollers (MCUs) are quantized to integer-only arithmetic and run in inference-only runtimes that do not carry the machinery backpropagation needs: the standard tool for adapting a model to the distribution shift (sensor noise, blur, lighting) it meets in the field."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2609.01683v1) · [PDF](https://arxiv.org/pdf/2609.01683v1)

## 一句话摘要

Vision models deployed on microcontrollers (MCUs) are quantized to integer-only arithmetic and run in inference-only runtimes that do not carry the machinery backpropagation needs: the standard tool for adapting a model to the distribution shift (sensor noise, blur, lighting) it meets in the field.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision models deployed on microcontrollers (MCUs) are quantized to integer-only arithmetic and run in inference-only runtimes that do not carry the machinery backpropagation needs: the standard tool for adapting a model to the distribution shift (sensor noise, blur, lighting) it meets in the field. Existing forward-only test-time adaptation (TTA) methods either run only on server- or edge-GPU-class models (not true microcontroller integer execution), or require the batch-normalization (BN) layers that integer deployment fuses away. We present a forward-only TTA method that operates on deployed, BN-folded, integer-only convolutional networks. The key observation is that fusing BN into the preceding convolution, a mandatory step for integer inference, destroys the statistics that normalization-based adaptation relies on. We restore adaptation by re-normalizing each folded convolution's per-channel output to its clean training statistics, using only forward-pass estimates. The method (i) recovers most of gradient-based TENT's accuracy gain (+20.9 vs. +24.9 points) and matches forward-only BN adaptation, while being the only method that runs on a folded integer-only model; (ii) needs to adapt only 3 of 21 layers (selected without seeing the test corruptions) to recover 93% of the benefit; (iii) survives single-sample streaming with a batch-size-scaled momentum; and (iv) generalizes across three datasets (up to 200 classes) and two architectures. We validate bit-exact int8 convolution execution and deploy on an ESP32-S3, where, measured with a Nordic PPK2 power profiler, the forward-only adaptation (a lightweight fp32 recalibration around the int8 convolutions) costs only 8.3 mJ (6.8% of inference energy) and 21.9 ms on the deployed SIMD-optimized model: forward-only adaptation is cheap on a real microcontroller.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 6 |

## 证据与限制

- taxonomy keywords: int8, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Muhammad Rehan, Haider Ali, Muhammad Ali Munir, Moaz Amjad
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv；Venue：Transactions on Machine Learning Research, 2026
- 代码：[https://github.com/Rehan000/forge-tta](https://github.com/Rehan000/forge-tta)
- 阅读深度：metadata
