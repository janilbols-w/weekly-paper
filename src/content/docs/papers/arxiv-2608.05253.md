---
title: "Beyond Rotations: AuroOFT for Expressive Quantized Orthogonal Fine-Tuning"
description: "Quantized orthogonal fine-tuning (qoft) enables parameter-efficient adaptation of low-bit language models by learning structured activation rotations before frozen quantized weights."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.05253) · [PDF](https://arxiv.org/pdf/2608.05253)

## 一句话摘要

Quantized orthogonal fine-tuning (qoft) enables parameter-efficient adaptation of low-bit language models by learning structured activation rotations before frozen quantized weights.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantized orthogonal fine-tuning (qoft) enables parameter-efficient adaptation of low-bit language models by learning structured activation rotations before frozen quantized weights. However, its task-specific updates remain constrained to linear orthogonal transformations, limiting input-dependent nonlinear corrections. We introduce AuroOFT, which keeps qoft as a stable quantization-compatible branch while attaching a zero-start gated low-rank nonlinear residual to each adapted linear layer. AuroOFT maps activations into an RMS-normalized compact latent space and uses adaptive nonlinear bases with bounded or token-dependent gating. The zero-initialized up projection makes AuroOFT functionally identical to qoft at initialization, while orthogonality remains a branch-level stability property rather than a property of the combined nonlinear layer. Under matched data, optimization, decoding, and parser protocols, AuroOFT improves Macro-6 over matched qoft by 1.30-2.70% on the 1.5B/3B Qwen2.5 settings, exceeds QLoRA by 6.52-10.62%, and saves 32.3-44.7% trainable parameters relative to QLoRA in representative scales. The small exam-style multiple-choice math set is treated only as a protocol-sensitivity diagnostic. Our code is available at the anonymous repository: https://anonymous.4open.science/r/AuroOFT-F3FD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yue Han, Dianlin Wang
- 发布：2026-08-05；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
