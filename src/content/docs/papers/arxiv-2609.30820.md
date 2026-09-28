---
title: "Quantizing Looped Transformers: Feedback Exposure and Calibration Blindness"
description: "Looped transformers reuse weights across recurrence steps, making low-bit quantization especially attractive."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.30820) · [PDF](https://arxiv.org/pdf/2609.30820)

## 一句话摘要

Looped transformers reuse weights across recurrence steps, making low-bit quantization especially attractive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped transformers reuse weights across recurrence steps, making low-bit quantization especially attractive. We identify two distinct failure modes of standard post-training quantization. On Huginn-3.5B, per-channel INT4 fails primarily at the non-residual loop-entry adapter, while quantizing the residual core is much less damaging. We call this feedback exposure: a quantized layer perturbs the recurrent state without an identity path, and the resulting error is fed back at later steps. Controlled experiments on linear filters and Mamba state-space models show that feedback exposure also occurs outside transformers. Grouped INT4 reveals a separate failure, calibration blindness: our one-step GPTQ baseline builds its Hessian from step-0 activations, leaving input directions used later in the recurrence nearly unweighted. Across nine checkpoints from seven looped architectures, one-step GPTQ is worse than round-to-nearest (RTN) on the primary task metric for five checkpoints. Accumulating the GPTQ Hessian across recurrence steps outperforms both one-step GPTQ and RTN on all nine checkpoints and recovers bf16-level accuracy on Huginn. These results separate two questions for PTQ on looped models: where quantization error enters the recurrence, and which states calibration sees.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nux Li
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
