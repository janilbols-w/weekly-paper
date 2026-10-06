---
title: "StagQ: Constraint-Driven Multi-Precision Weight Quantization for LLMs"
description: "Serving a large language model (LLM) across a fleet of deployments requires several weight-precision operating points."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.05977) · [PDF](https://arxiv.org/pdf/2610.05977)

## 一句话摘要

Serving a large language model (LLM) across a fleet of deployments requires several weight-precision operating points.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving a large language model (LLM) across a fleet of deployments requires several weight-precision operating points. Multi-precision formats serve them all from one stream whose prefixes are valid lower-precision codes, instead of storing multiple copies. We present StagQ, a multi-precision weight format whose main stream is a 2-bit group-wise affine base followed by a configurable number of 1-bit refinement planes on a dyadic step schedule. Every supported precision is a readable prefix, decoded by an affine map derived from metadata shared across all precisions, with no per-weight lookup. A sparse side record, filled both before and after the grid is fitted, holds out the few weights the grid serves worst. We report two configurations of the encoder. At two bits the cheaper one leads the strongest multi-precision baseline on Llama-3.1-8B, Phi-4, and OLMo-2-7B by 3.1 to 7.0 MMLU points, at a slightly lower logical rate. At three bits it leads on Llama-3.1-8B, leads on Phi-4 at a higher rate, and ties on OLMo-2-7B. At four bits it ties on all three, at a higher rate. In a batch-one matrix-vector product on an NVIDIA A100 GPU, timed on synthetic weights, our kernel is faster than the two baseline kernels in most shape-precision cases.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhe Wei, Mengqi Guo, Yuan Yuan, Jiunn Bin Lim, Boyi Pan, Michael Bi Mi
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
