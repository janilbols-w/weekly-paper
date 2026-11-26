---
title: "Beyond Accuracy: Prefix-Invariant Realizations of Low-Precision Fast Matrix Multiplication"
description: "Fast matrix multiplication saves multiplications through exact cancellation, but rounding sums that mix token rows can leave contributions from later tokens in earlier language model outputs."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.39816) · [PDF](https://arxiv.org/pdf/2609.39816)

## 一句话摘要

Fast matrix multiplication saves multiplications through exact cancellation, but rounding sums that mix token rows can leave contributions from later tokens in earlier language model outputs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fast matrix multiplication saves multiplications through exact cancellation, but rounding sums that mix token rows can leave contributions from later tokens in earlier language model outputs. This threatens prefix invariance, which likelihood scoring and batched inference rely on: an output must depend only on its allowed prefix. On Qwen2.5-14B-Instruct, two fast FP8 realizations repaired to near-bf16 accuracy, and the existing fast kernel FalconGEMM, change answers when only text outside the allowed prefix is replaced: on 4.17--10.00% of OpenBookQA items scored by likelihood and 39.6--51.8% of NQ-open questions answered in a batch. Accuracy thus does not certify prefix invariance, and the stability criteria we analyze cannot tell realizations apart: across all 512 sign variants of two-level Strassen the criteria stay constant while teacher-forced perplexities span a 772.4$\times$ range on the same model. We therefore construct certified realizations of two-level Strassen on bounded integer codes that quantize token rows independently, then mix and cancel exactly before rescaling, using 49 block multiplications instead of 64. Our certificate guarantees bitwise equality to a prescribed row-local classical int8 operator at the same quantization specification, so every certified realization inherits its prefix invariance. Certification thus turns realization choice into a pure cost decision: which certified realization runs can no longer change any output. With optimized kernels, certified realizations run faster than classical int8 on an NVIDIA H20, and in the SGLang serving engine they raise throughput over its FP8 path by 1.2--5.6% on four models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shuxiao Xie, Shuyang Xie, Yuan Cao, Dezhi Ran, Wei Yang, Tao Xie
- 发布：2026-09-30；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
