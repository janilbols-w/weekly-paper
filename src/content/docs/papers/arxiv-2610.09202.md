---
title: "Few Bits, One Law: Toward W2A4KV2"
description: "Extreme low-bit LLM compression is most challenging when weights, activations, and KV caches are quantized together: their distributions differ, and quantization errors interact throughout the network."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.09202) · [PDF](https://arxiv.org/pdf/2610.09202)

## 一句话摘要

Extreme low-bit LLM compression is most challenging when weights, activations, and KV caches are quantized together: their distributions differ, and quantization errors interact throughout the network.

## 为什么值得关注

待编辑增强。

## 摘要原文

Extreme low-bit LLM compression is most challenging when weights, activations, and KV caches are quantized together: their distributions differ, and quantization errors interact throughout the network. We introduce CanonQ, a unified quantization-aware training framework that addresses these challenges by separating source canonicalization from task-aware adaptation. Fixed rotations and energy normalization map heterogeneous tensor sources to canonical coordinates, enabling frozen Gaussian-reference codebooks to be reused across layers and models. Joint training then adapts the network to the coupled errors of weight, activation, and cache quantization within a common scalar/vector interface. We bound frozen-codebook transfer error and local task loss, and derive an exact normalization-aware straight-through Jacobian that links quantization distortion to gradient bias. The strongest gains arise under joint W2A4KV2 compression: across LLaMA3-1B/3B/8B, CanonQ-Omni achieves up to 14.28x lower WikiText-2 perplexity and up to 57.9% higher mean zero-shot accuracy than prior state-of-the-art and representative quantization baselines. The benefits extend to Qwen3-1.7B, code generation, and mathematical reasoning: on instruction-tuned MobileLLM-Pro-1B at W2A16KV16, CanonQ achieves relative improvements of 41.7% in HumanEval pass@1 and 39.1% in GSM8K exact match over the strongest evaluated quantization baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kai Yi, Tarek Elgamal, Sruthikesh Surineni, Vignesh Vivekraja, Soumyadeep Ghosh, Steven Li
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
