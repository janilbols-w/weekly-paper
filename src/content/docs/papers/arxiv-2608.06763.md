---
title: "CubicQuant: Parametric Non-Uniform Codebooks for High-Throughput LLM Inference with 1-8-Bit Weights"
description: "Weight quantization for large-language-model inference must balance adaptive reconstruction levels with representations regular enough for efficient GPU execution."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.06763) · [PDF](https://arxiv.org/pdf/2608.06763)

## 一句话摘要

Weight quantization for large-language-model inference must balance adaptive reconstruction levels with representations regular enough for efficient GPU execution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Weight quantization for large-language-model inference must balance adaptive reconstruction levels with representations regular enough for efficient GPU execution. Uniform integers constrain each group to a linear grid. Low-bit floating-point formats use a fixed exponent-mantissa structure, while learned codebooks gain flexibility at the cost of irregular decoding and additional metadata. We introduce CubicQuant, a parametric non-uniform scalar format that preserves a dense integer code stream while adapting reconstruction levels within each weight group. A monotonic cubic curve, specified by two shape parameters and one scale, maps uniformly spaced magnitude codes to non-uniform levels. The family spans 1-8-bit weight payloads, contains symmetric uniform integer quantization as an exact special case, and has effective width B + 64/G bits per weight for payload width B and group size G. We derive population distortion under Uniform, Gaussian, and Laplace distributions, formulate continuous and Dynamic-A8-carrier-aware fitting objectives, and describe direct packed-weight GPU execution. For finite groups of G=128 with 15,360 samples per distribution, W4 CubicQuant reduced reconstruction RMSE relative to optimally clipped four-bit uniform integer quantization by 3.90% on Uniform, 13.49% on Gaussian, and 28.14% on Laplace samples. Relative to the best enumerated four-bit finite floating-point format, the reductions were 3.90%, 9.44%, and 6.27%. Preliminary H200 kernel measurements show a workload-dependent crossover: model-dtype execution is faster for narrow GEMV, while Dynamic A8 becomes favorable as row count grows. The results establish the format's representational promise and direct executability; downstream model quality and cross-device end-to-end performance remain open evaluation questions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xuetian Gao
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
