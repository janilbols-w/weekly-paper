---
title: "Vortex: Bridging Extreme Compression and Efficient LLM Inference"
description: "Extreme compression techniques, including vector quantization (VQ) and input-dependent sparsity, can significantly reduce the memory footprint of large language models (LLMs)."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.12208) · [PDF](https://arxiv.org/pdf/2609.12208)

## 一句话摘要

Extreme compression techniques, including vector quantization (VQ) and input-dependent sparsity, can significantly reduce the memory footprint of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Extreme compression techniques, including vector quantization (VQ) and input-dependent sparsity, can significantly reduce the memory footprint of large language models (LLMs). However, a key challenge remains in translating such compression into practical efficiency. On conventional systolic-array-based accelerators, VQ incurs high dequantization overhead, while the irregular patterns of input-dependent sparsity are difficult to exploit. In this study, we address these challenges with Vortex, an architecture compatible with systolic-array-based accelerators with minimal hardware overhead, bridging the gap between extreme compression and efficient inference. Vortex adopts a bi-flow execution strategy that efficiently supports vector-quantized models across both prefill and decoding workloads, and we further optimize it through systematic design space exploration. On the algorithm side, we propose codebook-wise contextual sparsity to align with VQ execution. Across end-to-end workloads, Vortex achieves $8.03\times$--$23.7\times$ speedup and $5.68\times$--$12.5\times$ energy reduction over state-of-the-art accelerators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haoxuan Shan, Cong Guo, Bowen Duan, Chiyue Wei, Feng Cheng, Yuzhe Fu, Yintao He, Hai "Helen" Li, Yiran Chen
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
