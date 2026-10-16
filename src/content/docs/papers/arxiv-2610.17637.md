---
title: "Mixed Precision Scaling Laws for Quantized Pretraining"
description: "Since scaling laws were introduced for modern LLMs (Kaplan et al., 2020), several works have extended them to account for quantization, tracking the emerging low-precision data types supported on AI accelerators."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.17637v1) · [PDF](https://arxiv.org/pdf/2610.17637v1)

## 一句话摘要

Since scaling laws were introduced for modern LLMs (Kaplan et al., 2020), several works have extended them to account for quantization, tracking the emerging low-precision data types supported on AI accelerators.

## 为什么值得关注

待编辑增强。

## 摘要原文

Since scaling laws were introduced for modern LLMs (Kaplan et al., 2020), several works have extended them to account for quantization, tracking the emerging low-precision data types supported on AI accelerators. We develop a more accurate scaling law for quantized pretraining with mixed precision across the forward and backward passes, grounded in optimization theory and validated empirically. Our formulation separates the effects of quantization on model capacity and on optimization efficiency, and explicitly models the persistent optimization error from forward and backward quantization identified through convergence analysis. To select the regimes for fitting and evaluating our law, we first decompose existing 4-bit training recipes into their forward and backward components, isolating those that most affect loss. Our Qwen3 experiments under selected 4-bit regimes, together with published Llama-style experiments, show that our law predicts loss with up to $11\times$ lower MSE than existing laws as model size and token count scale. Finally, we extend our law to layer-wise mixed precision and identify the optimal quantized-pretraining recipe, i.e., model size, training tokens, and per-layer forward/backward precision, under a hardware-aware compute budget. Unlike prior precision scaling laws, our law predicts that the optimal precision increases with the compute budget.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixed precision, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jinuk Kim, Rajarshi Saha, Muhammed Fatih Balin, Youngsuk Park
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
