---
title: "RAMP: Recurrent Adaptive Mixed Precision for Efficient Prefill in Recurrent-Depth Language Models"
description: "Recurrent-depth language models improve inference-time reasoning by repeatedly applying a shared network to refine internal representations, but the additional recurrent computation also increases inference cost."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.13041) · [PDF](https://arxiv.org/pdf/2610.13041)

## 一句话摘要

Recurrent-depth language models improve inference-time reasoning by repeatedly applying a shared network to refine internal representations, but the additional recurrent computation also increases inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recurrent-depth language models improve inference-time reasoning by repeatedly applying a shared network to refine internal representations, but the additional recurrent computation also increases inference cost. This overhead is particularly pronounced during long-context prefill, where the full input sequence is repeatedly processed across recurrent depth. Weight-and-activation quantization offers a natural way to accelerate this computation through lower-precision arithmetic, yet repeatedly applying quantized computation introduces numerical perturbations that accumulate along the recurrent trajectory. We systematically analyze how such errors propagate across recurrent depth and show that quantization errors introduced earlier are attenuated by more subsequent recurrent steps and therefore have a smaller effect on the final representation. Matched-budget experiments strongly support this prediction, showing that placing quantized computation earlier in recurrent depth consistently yields the best fidelity. Based on this insight, we introduce RAMP (Recurrent Adaptive Mixed Precision), which performs early recurrent refinement using low-precision weight-and-activation computation and restores high precision for terminal refinement. Across context lengths up to 4K, RAMP preserves near-full-precision prefill quality while achieving up to 1.16x end-to-end first-prefill speedup on an NVIDIA H100, corresponding to a 13.9% latency reduction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixed precision, quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ke Wan, Chen Chen
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
