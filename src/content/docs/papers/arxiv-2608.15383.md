---
title: "Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference"
description: "Sparse mixture-of-experts (MoE) language models reduce arithmetic by activating only a small subset of experts per token, yet deployment still requires storing and moving the full expert bank."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.15383) · [PDF](https://arxiv.org/pdf/2608.15383)

## 一句话摘要

Sparse mixture-of-experts (MoE) language models reduce arithmetic by activating only a small subset of experts per token, yet deployment still requires storing and moving the full expert bank.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse mixture-of-experts (MoE) language models reduce arithmetic by activating only a small subset of experts per token, yet deployment still requires storing and moving the full expert bank. We present ExactMoE, an inference design that applies symmetric group-128 four-bit weight quantization only to routed experts, stores those experts in kernel-native MARLIN form in pinned host memory, and executes all selected experts through a configurable GPU-resident slot cache and fused grouped MoE kernels. The router, attention, embeddings, normalization layers, and language-model head remain in BF16. "Exact" refers to complete expert availability and an unchanged top-k routing procedure: no expert is pruned, substituted, or forced to execute on the CPU. It does not imply numerical identity with the BF16 model. On OLMoE-1B-7B-0924-Instruct, evaluated on a single NVIDIA L4, a 16-slot configuration reduces peak reserved GPU memory from 14.168 to 1.836 GiB (87.04%) while retaining 81.85% of BF16 decode throughput. A fully resident 64-slot configuration reaches 31.923 tokens/s versus 21.662 tokens/s for BF16 while reserving 4.061 GiB. Across 12,450 zero-shot multiple-choice questions, ExactMoE obtains 70.3534% normalized accuracy versus 70.8996% for BF16, retaining 99.23% of the baseline accuracy. In a matched 16-token ablation, fused grouped execution is 1.97x as fast as a sequential W4 reference. These results identify a practical memory-transfer-throughput frontier for complete-expert MoE inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Amjad Saab
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
