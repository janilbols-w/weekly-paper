---
title: "CurveFP: Rational-Radix Logarithmic Datatypes with Closed Products for Language Models"
description: "Low-precision datatypes reduce language-model cost, but most formats optimize scalar fidelity while leaving the arithmetic induced by their products unchanged."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.10010) · [PDF](https://arxiv.org/pdf/2608.10010)

## 一句话摘要

Low-precision datatypes reduce language-model cost, but most formats optimize scalar fidelity while leaving the arithmetic induced by their products unchanged.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-precision datatypes reduce language-model cost, but most formats optimize scalar fidelity while leaving the arithmetic induced by their products unchanged. We introduce CurveFP, a closed-product codebook family that distributes quantized magnitudes across interleaved logarithmic curves under compact block scales. A rational radix tunes dynamic range against local resolution, while uniform curve indices make every nonzero product algebraically closed. Product formation becomes an exact sign XOR and integer-index update, and a derived finite phase count determines the accumulation schedule. We instantiate this algebra as CurveFP eight E4C3/E5C2 for training and CurveFP seven E3C3 for compact deployment. In evaluation, CurveFP seven beats tensor-wise FP8 perplexity on four 7B--9B models with one fewer element bit and stays within 1.32\% of native quality. CurveFP eight lowers operand NMSE in all 36 paired forward and backward GEMM comparisons. Across three matched 128.3M-parameter triplets, every mode completes 3B-token pretraining per seed; CurveFP eight reaches mean BF16-inference perplexity 22.5366 versus 22.5407 for FP8 and incurs a lower format-induced penalty in all three seeds. A 36-cell downstream matrix finds lower WikiText-103 perplexity for the CurveFP eight-trained checkpoints in all 12 seed-format comparisons, with mixed PG-19 and task deltas. Together, these results establish CurveFP as an arithmetic co-design that combines FP8-class numerical behavior, seven-bit inference, and a substantially simpler product path.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ye Qiao
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
