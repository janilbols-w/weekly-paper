---
title: "FLAMIA: FLAsh MIcroscaling Attention for Fast and Causally Safe Training on Blackwell"
description: "Attention remains a substantial computational cost in Transformer training, particularly at long context lengths."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.03344) · [PDF](https://arxiv.org/pdf/2611.03344)

## 一句话摘要

Attention remains a substantial computational cost in Transformer training, particularly at long context lengths.

## 为什么值得关注

待编辑增强。

## 摘要原文

Attention remains a substantial computational cost in Transformer training, particularly at long context lengths. NVIDIA Blackwell GPUs provide high-throughput low-precision matrix multiplication, but exploiting it in attention requires addressing quantization overhead, causal information leakage through shared scales, and numerical inconsistencies between the forward and backward passes. We present FLAMIA, a family of attention kernels for Blackwell with MXFP8 and mixed NVFP4/FP8 training paths. Our design combines token-block scaling that reuses quantized operands across matrix orientations, targeted safeguards against scale-induced leakage, and consistent forward and backward computations. Fused quantization and architecture-specific kernel optimizations reduce overhead, while document-local scaling and workload-aware scheduling support variable-length documents directly in packed layouts without repacking. Across various causal packed-document workloads, the MXFP8 path accelerates the combined forward and backward attention call, including quantization, by factors of $1.10$--$1.40\times$ on B200 and $1.06$--$1.42\times$ on B300 relative to the fastest evaluated baseline for each workload. We validate training stability and quality preservation on pretraining Llama-style models. These results show how jointly designing quantization, training numerics, and document scheduling translates low-bit hardware throughput into practical attention acceleration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, microscaling, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fedor Velikonivtsev, Mikhail Koltakov, Denis Kuznedelev
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
