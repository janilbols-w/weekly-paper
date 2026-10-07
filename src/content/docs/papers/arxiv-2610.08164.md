---
title: "Align, Then Correct: Training-Free Two-Stage Low-Rank Compensation for Extremely Quantized Large Language Models"
description: "Low-rank quantization error compensation (LQEC) recovers the accuracy lost under aggressive weight quantization by attaching a closed-form rank-$r$ adapter beside each frozen quantized weight, without any training."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.08164) · [PDF](https://arxiv.org/pdf/2610.08164)

## 一句话摘要

Low-rank quantization error compensation (LQEC) recovers the accuracy lost under aggressive weight quantization by attaching a closed-form rank-$r$ adapter beside each frozen quantized weight, without any training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-rank quantization error compensation (LQEC) recovers the accuracy lost under aggressive weight quantization by attaching a closed-form rank-$r$ adapter beside each frozen quantized weight, without any training. We show that existing compensators are limited by two shared simplifications. They calibrate symmetrically, evaluating the full-precision and compensated weights on the same activation, which yields a compensation target that is inherently high-rank -- so a fixed rank budget captures only a small fraction of it. And they minimize only the second-order term of the loss, although the compensated model is not stationary: a first-order descent direction larger than the applied compensation itself remains in every layer, and no reconstruction objective can absorb it. We propose a two-stage closed-form framework that removes both simplifications. Stage 1 aligns each layer's output with the full-precision model under a Fisher-weighted asymmetric objective, concentrating the rank budget on a rank-compressible target. Stage 2 re-measures statistics on the compensated model and applies a rank-constrained natural-gradient step that absorbs the remaining first-order signal. Every adapter is the result of a single truncated SVD; backward passes serve only to collect statistics. At 2 bits under QuIP#, our method reduces WikiText-2 perplexity from 12.43 to 10.26 on Qwen3-8B and from 21.11 to 13.22 on Qwen3-4B. On the held-out C4 corpus, it recovers 51% and 84% of the gap to FP16, versus 31% and 63% for the strongest baseline, with consistent gains in the seven-task zero-shot average, at higher bit-widths, and under a distinct quantizer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Seobin Song, Geonho Lee, Janghwan Lee, Jungwook Choi
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
