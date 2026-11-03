---
title: "Trainable Vector Quantization for Large Language Models"
description: "Vector Quantization (VQ) is a rapidly evolving technique for compressing Large Language Model (LLM) weights, reducing memory usage, and speeding up inference."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.41822) · [PDF](https://arxiv.org/pdf/2610.41822)

## 一句话摘要

Vector Quantization (VQ) is a rapidly evolving technique for compressing Large Language Model (LLM) weights, reducing memory usage, and speeding up inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vector Quantization (VQ) is a rapidly evolving technique for compressing Large Language Model (LLM) weights, reducing memory usage, and speeding up inference. However, extreme compression deteriorates model performance, which is challenging to recover due to the discrete nature of VQ parameters. Existing methods employ training-free approaches that are limited to layer-wise reconstruction loss minimization. To address this limitation, we propose TVQ, a novel method that leverages straight-through estimation to enable gradient descent-based optimization of vector-quantized LLMs. By reformulating VQ LLM optimization with trainable latent weights, TVQ enables arbitrary objective minimization. We constitute our approach by applying TVQ in a block-wise knowledge distillation paradigm, which balances quality and training efficiency, and propose several practical solutions to accelerate training. In experiments on modern LLMs, we demonstrate that TVQ is compatible with modern VQ schemes. As a result, TVQ achieves state-of-the-art quality in low-bit post-training quantization settings with a modest training budget and straightforward PyTorch implementation. For instance, TVQ achieves near-lossless 2-bit quantization for LLaMA2-70B with only 1% accuracy drop on popular Question-Answering benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anastasiia Prutianova, Alina Bogdanova, Mikhail Shutov, Dmitrii Poimanov, Anatoly Gorkov, Ilia Zharikov
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
