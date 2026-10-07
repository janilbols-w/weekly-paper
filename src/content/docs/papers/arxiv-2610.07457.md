---
title: "AlignQuant: Tile-Aligned Mixed-Precision Quantization for Efficient LLM Generation"
description: "Fine-grained mixed-precision quantization promises efficient large language model inference, but local precision choices can conflict with regular GPU storage and computation units."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.07457) · [PDF](https://arxiv.org/pdf/2610.07457)

## 一句话摘要

Fine-grained mixed-precision quantization promises efficient large language model inference, but local precision choices can conflict with regular GPU storage and computation units.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fine-grained mixed-precision quantization promises efficient large language model inference, but local precision choices can conflict with regular GPU storage and computation units. This precision-boundary mismatch limits the translation of compression into practical acceleration. We introduce AlignQuant, a post-training quantization method that uses GPU-compatible two-dimensional weight tiles as the common unit of precision allocation, compact storage, and execution. This shared partition lets precision follow sensitivity within output channels. Joint prefill/decode calibration scores precision reductions using projection-output perturbations weighted by language-model loss gradients under quantized activations. Phase-normalized scores prioritize higher precision for tiles important to either phase under a model-wide weight-storage budget. Each tile stores one selected representation, while phase-specialized kernels reuse the packed model and expand lower-bit weights for INT8 computation with 8-bit activations. Across four LLMs spanning 3B to 14B parameters, AlignQuant achieves up to $2.50\times$ generation speedup over BF16 while preserving model quality. Evaluations further cover three GPUs and contexts up to 64K tokens. These results show that local precision flexibility and regular GPU execution can coexist through a shared tile unit. The implementation is available at https://github.com/HanzhiZhang-Ulrica/AlignQuant.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hanzhi Zhang, Qiao Zhang, Qinglei Cao, Heng Fan, Yan Huang, Kewei Sha, Yunhe Feng
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/HanzhiZhang-Ulrica/AlignQuant](https://github.com/HanzhiZhang-Ulrica/AlignQuant)
- 阅读深度：metadata
