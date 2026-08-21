---
title: "FlashQuant: Sparse-Dense Fusion for Memory-Efficient Outlier-Aware LLM Inference"
description: "Low-bit quantization reduces the memory footprint and computational cost of large language model (LLM) inference."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2608.15531) · [PDF](https://arxiv.org/pdf/2608.15531)

## 一句话摘要

Low-bit quantization reduces the memory footprint and computational cost of large language model (LLM) inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit quantization reduces the memory footprint and computational cost of large language model (LLM) inference. However, high-magnitude outlier weights can induce substantial quantization errors and degrade model accuracy. Outlier-aware quantization addresses this issue by retaining outliers in high precision while quantizing the remaining weights, resulting in a low-bit dense GEMM path and a high-precision sparse SpMM path. Existing implementations execute these paths in separate GPU kernels, despite their shared activations and outputs, thereby missing opportunities for intra-operator reuse and incurring redundant global-memory accesses. This inefficiency is particularly pronounced in memory-bound decoding workloads. We propose FlashQuant, a content-sharing execution framework for outlier-aware W4A16 decoding. FlashQuant fuses the dense GEMM and sparse outlier SpMM paths into a single GPU kernel, enabling on-chip reuse of activation and output tiles across heterogeneous computations. It introduces three key techniques: sparse-dense tiling, which aligns outlier processing with dense GEMM tiles; Tile-COO outlier encoding, which enables efficient sparse access and reduces shared-memory bank conflicts; and pipelined scheduling, which overlaps computation with data movement. Experiments show that FlashQuant reduces outlier-processing overhead, achieving $2.74\times - 4.18\times$ speedup over cuBLAS BF16 and up to $1.53\times$ speedup over the strongest unfused outlier-aware baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junqing Lin, Jingwei Sun, Zhengding Hu, Guangzhong Sun
- 发布：2026-08-16；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
