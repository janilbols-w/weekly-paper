---
title: "Transforms for LLM Quantization: The Great Inversion and Format Co-Design"
description: "Most competitive 4-bit LLM research pipelines now open the same way: apply a linear, function-preserving transform (rotation, scaling, permutation, non-orthogonal affine) so the outlier mass sits more favorably against the group scales, and only then round."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.25188) · [PDF](https://arxiv.org/pdf/2608.25188)

## 一句话摘要

Most competitive 4-bit LLM research pipelines now open the same way: apply a linear, function-preserving transform (rotation, scaling, permutation, non-orthogonal affine) so the outlier mass sits more favorably against the group scales, and only then round.

## 为什么值得关注

待编辑增强。

## 摘要原文

Most competitive 4-bit LLM research pipelines now open the same way: apply a linear, function-preserving transform (rotation, scaling, permutation, non-orthogonal affine) so the outlier mass sits more favorably against the group scales, and only then round. Yet we are aware of no survey dedicated to this transform stage, and its literature is quietly re-deriving an older theory. We identify and formalize the principle that organizes it, the Great Inversion: allocation-flexible coding rewards energy concentration, whereas the grouped shared-scale quantization a deployed matrix instruction performs rewards within-group flattening. Classical transform coding (1963: decorrelate, allocate bits, quantize) spends different bits per coordinate at a fixed total rate; for a Gaussian source at high rate the Karhunen-Loeve transform's concentration minimizes distortion. A deployed operand tile instead carries one absolute-maximum scale per group and equal bits everywhere, with no allocation; on a uniform grid that objective rewards flattening, approached by Hadamard incoherence. We prove that opposition under within-group majorization: the prescriptions point in opposite directions, each backed by a proof against its own objective, and for a generic spectrum no optimality guarantee transfers. A second axis is the number format: the non-uniform FP4 grid makes flattening buy less, MXFP4's power-of-two block scale still rewards a rotation confined to that block, and NVFP4's mantissa-carrying scale largely removes that pull, so the target pole depends jointly on allocation regime and format. We survey 200 works to a June 2026 cutoff; classify 43 transform methods by structure, data-awareness, searched-versus-constructed, and runtime cost; record, where reported, how they compose with GPTQ rounding; distill a first-choice guide by deployment regime; and close with the open problems it exposes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ehsan Jokar
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
