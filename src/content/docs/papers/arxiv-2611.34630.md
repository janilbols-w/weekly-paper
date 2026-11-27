---
title: "A Differential Computing Accelerator for LLM Inference Leveraging Bit-Slice Transition Sparsity"
description: "Large language models (LLMs) have become foundational to modern artificial intelligence."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.34630) · [PDF](https://arxiv.org/pdf/2611.34630)

## 一句话摘要

Large language models (LLMs) have become foundational to modern artificial intelligence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have become foundational to modern artificial intelligence. Driven by scaling laws, their rapid growth poses increasing computational and memory challenges for deployment. To accelerate the general matrix multiplication (GEMM) operations that dominate LLM computation, bit-slice architectures decompose quantized operands along the bit dimension, exposing slice-level sparsity and redundancy. However, existing bit-slice designs primarily exploit sparsity in high-order slices, while dense low-order slices still offer substantial untapped reuse opportunities. We observe that bit-slice vectors (BSVs) are highly clustered in Hamming space, with many BSVs lying only a few bit flips away from a small set of representative patterns. Based on this observation, we propose ISTS, an algorithm-hardware co-designed accelerator that leverages representative BSV patterns as shared Steiner points to reuse partial sums across slices, substantially reducing computation. Specifically, the partial sum of each target BSV can be reconstructed from that of its assigned Steiner point using only a few additions or subtractions. On the algorithmic side, we propose Steiner Absorption Table Construction (SATC), which selects a compact set of Steiner points to absorb BSVs with only a few bidirectional bit flips, while FlipPrune selectively prunes flips to further expand the reusable BSV population. On the hardware side, we design a lightweight accelerator that supports Steiner reuse for static linear layer weights and runtime-generated attention K/V tensors. Comprehensive evaluations show that ISTS achieves average speedups of $3.09\times$, $2.41\times$, $2.18\times$, $1.27\times$, and $1.41\times$ over the state-of-the-art accelerators ANT, BBS, LUT Tensor Core, Transitive Array, and MCBP-BRCR, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yifan Wang, Zetao Guo, You Xiao, Wendi Sun, Song Chen
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
