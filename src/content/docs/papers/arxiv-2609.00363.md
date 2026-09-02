---
title: "Deterministic LLM Inference Across GPU Kernels: Power-of-Two INT8 Quantization Scales and the Limits of Tolerance-Based Conformance"
description: "Conformance suites for quantized GEMM kernels ask whether two implementations agree within a tolerance."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.00363) · [PDF](https://arxiv.org/pdf/2609.00363)

## 一句话摘要

Conformance suites for quantized GEMM kernels ask whether two implementations agree within a tolerance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Conformance suites for quantized GEMM kernels ask whether two implementations agree within a tolerance. We measure what such a suite can detect. Injecting nine faults into a reference INT8 pipeline over 8,232 layer--fault--regime cells of Qwen3-1.7B, we find that every one of five epilogue faults -- scale precision, double rounding, multiplication order, output truncation, fused ordering -- moves the output by at most a single bfloat16 spacing, and by exactly one whenever it moves it at all, across 5,880 cells. A tolerance of one spacing is therefore blind to the entire class by construction: four of the five faults are detected by no check in the suite, and the fifth only under power-of-two scales. Faults that violate the accumulator's exactness preconditions, or that break operand sharing, are detected without exception, and a null fault never fires. What a tolerance-based suite of this shape establishes is therefore narrower than interchangeability: that the preconditions hold, that operands are shared, and that differences stay within one spacing. The power-of-two constraint that exposes the one detected fault is also deployable. Requantizing every weight scale to its nearest power of two makes CUTLASS and Triton agree bitwise at every linear layer (196/196 and 252/252, against 8/196 and 10/252 under the checkpoints' own scales) and yields byte-identical generated token sequences at 1.7B, 8B and 14B (8/8 prompts, against 0/8 at all three). Observed perplexity point estimates are +0.32%, -0.28% and +0.48%; the 90% intervals cover zero at the two smaller sizes but not at 14B, reaching +0.71% and +0.76%. A previously reported +157% perplexity for this intervention was an artifact of a probe that rewrote scales without requantizing the weights; separating the effects attributes 99.8% of it to the resulting weight--scale mismatch rather than to the power-of-two constraint itself.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Teng-Ruei Chen
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
