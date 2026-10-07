---
title: "QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction"
description: "As large language model inference shifts toward lower precision, post-training quantization (PTQ) becomes increasingly brittle, making quantization-aware training (QAT) essential for preserving model quality."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.13966) · [PDF](https://arxiv.org/pdf/2608.13966)

## 一句话摘要

As large language model inference shifts toward lower precision, post-training quantization (PTQ) becomes increasingly brittle, making quantization-aware training (QAT) essential for preserving model quality.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language model inference shifts toward lower precision, post-training quantization (PTQ) becomes increasingly brittle, making quantization-aware training (QAT) essential for preserving model quality. However, QAT has a structural mismatch: gradient updates are applied to latent full-precision weights, while the loss and gradients are computed on lossy reconstructions of those weights. This mismatch can lead to suboptimal training trajectories and a higher loss floor. Second-order PTQ methods address a similar problem by minimizing loss-aware reconstruction error, but applying such expensive reconstruction repeatedly during QAT as the weights evolve is impractical. We introduce QUASAR, a QAT method that brings lightweight, loss-aware reconstruction into the training loop. At each training step, QUASAR reconstructs the latent weights by searching over a small set of clipping ranges and fitting dequantization parameters through saliency-weighted least squares. We use an exponential moving average of squared gradients as the per-parameter saliency signal. Our theoretical analysis shows that optimizing QUASAR's reconstruction objective tightens both the convergence and final-loss bounds of QAT. We evaluate QUASAR across four model families and across INT4, INT3, INT2, and NVFP4 quantization formats. QUASAR consistently achieves lower training and evaluation loss than competitive QAT methods and outperforms QAT and PTQ baselines on downstream benchmarks. At INT2, QUASAR improves average accuracy over the best QAT baseline by 13.3 points with quantization-aware distillation and by 10.9 points with QAT on mathematical reasoning data. Notably, after distillation on only about 600M tokens, QUASAR's INT4 Gemma-4 E4B checkpoint outperforms the corresponding QAT checkpoint released by Google, with 66% lower KL divergence and 1.8 points higher average accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vincent Counathe, Ben Athiwaratkun, Christopher De Sa, Tianyi Zhang
- 发布：2026-08-17；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
