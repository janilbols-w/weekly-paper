---
title: "QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction"
description: "As large language model inference shifts toward lower precision, post-training quantization (PTQ) becomes increasingly brittle, making quantization-aware training (QAT) essential for preserving model quality."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.13966) · [PDF](https://arxiv.org/pdf/2608.13966)

## 一句话摘要

As large language model inference shifts toward lower precision, post-training quantization (PTQ) becomes increasingly brittle, making quantization-aware training (QAT) essential for preserving model quality.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language model inference shifts toward lower precision, post-training quantization (PTQ) becomes increasingly brittle, making quantization-aware training (QAT) essential for preserving model quality. However, QAT computes the loss and surrogate gradients using a lossy reconstruction of latent full-precision weights, while applying updates to the latent weights themselves. This mismatch can lead to suboptimal training trajectories and a higher loss floor. Second-order PTQ methods mitigate a similar gap by minimizing loss-aware reconstruction error, but doing it once for a frozen model can take hours; repeating this process throughout QAT as the weights evolve is impractical. We introduce QUASAR, a QAT method that continuously performs lightweight, loss-aware reconstruction in the training loop to lower the loss floor and improve the resulting low-bit model. At each training step, QUASAR uses the exponential moving average of squared gradients as online saliency estimates, searches over a small set of clipping ranges, and fits affine dequantizers via saliency-weighted least squares. Our analysis shows that the loss-aware reconstruction error is the only reconstruction-dependent term in the QAT convergence bound and controls the loss of the final quantized model, establishing QUASAR's objective as a principled optimization target. QUASAR modifies only the training procedure and supports standard deployment formats, including integer quantization and NVFP4, with no inference-time changes or overhead. Across Qwen3 and Llama-3.1, QUASAR achieves the lowest held-out KL divergence among competitive QAT methods at 2, 3, and 4 bits, reducing KL by at least 10% at 3 and 4 bits and by 29% at 2 bits. At 2 bits, it improves average accuracy across eight tasks by 3.5-4.3 percentage points over strong QAT and PTQ baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vincent Counathe, Ben Athiwaratkun, Christopher De Sa, Tianyi Zhang
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
