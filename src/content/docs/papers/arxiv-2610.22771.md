---
title: "Cross-Precision Transfer, Non-Local Context, and Capacity-Readout Boundaries of Scale Calibration in Low-Bit LLMs"
description: "Low-bit post-training quantization freezes integer codes and zero points, leaving groupwise scales as a compact adaptation interface."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.22771) · [PDF](https://arxiv.org/pdf/2610.22771)

## 一句话摘要

Low-bit post-training quantization freezes integer codes and zero points, leaving groupwise scales as a compact adaptation interface.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit post-training quantization freezes integer codes and zero points, leaving groupwise scales as a compact adaptation interface. We study cross-precision transfer, non-local context, optimizer capacity, and readout behavior on Qwen3-1.7B and Llama-3.2-3B. First, transferring relative scale gains between floating-point and INT3 Qwen models with zero recipient training retains 76.9%-90.5% of self-calibration NLL reductions on fresh WikiText and C4, alongside resolved own-source preferences. Group permutation destroys transfer, and norm-matched layer withdrawal degrades all 16 layer-domain comparisons. A Llama control with identical initial tensors at all calibrated projections isolates preferences induced by surrounding network context. Second, expanding Llama calibration from 4 to 196 projections (0.79M to 22.02M scales) makes learning rate 0.01 win a 50-step training-loss pilot. Continuing to 200 steps memorizes the 28-block WikiText pool, inflates unseen perplexity by 2.06-2.28 times relative to 4-site calibration, and degrades mixed-action PIQA accuracy; learning rate 0.001 prevents memorization and restores accuracy. Third, across 24 Qwen ARC readout endpoints, advancing from 200 to 600 steps worsens INT3 teacher KL on plain-text readouts yet improves it under chat wrapping. Cross-fitted four-parameter static option bias explains 71.4%-75.4% of quantized Chat-Space score-shift SSE, versus less than 2.3% on floating point. Subtracting this bias raises INT3 chat teacher agreement from 33.3%-33.9% to 56.6%-57.5% and cuts KL from 4.15-4.42 to 1.18-1.24 nats.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xu Cao, Wenxuan Xiao
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
