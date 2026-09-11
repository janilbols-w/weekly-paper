---
title: "RDQ: Residual Distribution Quantization for Large Language Models"
description: "Post-training quantization (PTQ) of large language models degrades sharply below 4-bit precision."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.10137) · [PDF](https://arxiv.org/pdf/2607.10137)

## 一句话摘要

Post-training quantization (PTQ) of large language models degrades sharply below 4-bit precision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) of large language models degrades sharply below 4-bit precision. We identify the root cause as residual stream distributional drift: quantization noise injected at each transformer layer accumulates in the shared residual representation, causing KL divergence from the FP16 baseline to grow super-linearly with depth (Pearson r=0.999 with log-perplexity, p<0.001, confirmed across all tested methods and bit-widths). We discover that 84% of LLaMA-3-8B layers exhibit non-Gaussian residual distributions (KS test, p<=0.05), and that per-layer residual stream variance grows 6,548x across depth. We propose RDQ (Residual Distribution Quantization), a PTQ framework whose central contribution is Cascaded Error Compensation (CEC): a sequential calibration procedure that captures the actual drifted activations each layer receives (computed by running calibration data through already-quantized upstream layers) and fits per-channel AWQ-style scales against those drifted inputs, with scales folded into preceding RMSNorm weights for exact mathematical equivalence at zero inference overhead. RDQ achieves state-of-the-art results on all three tested architectures: LLaMA-3-8B: 7.55 / 5.62 PPL (W3/W4); Qwen-2.5-7B: 7.46 / 6.38 PPL; Mistral-7B: 6.88 / 5.73 PPL. RDQ beats the best published baseline (LeanQuant/SpinQuant) at every model and bit-width combination, with gains up to -46.4% vs. RTN at W3A16 on LLaMA-3-8B. All output is standard group-128 asymmetric quantization, deployable on Qualcomm AIMET, GGUF, and any standard inference stack at zero runtime overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Prateek Singh
- 发布：2026-09-11；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
