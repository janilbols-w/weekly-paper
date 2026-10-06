---
title: "Beyond Masked Sparsity: SNACK Enables Truly Sparse Neural Networks on GPU"
description: "Deep neural networks continue to grow in parameter count, driving up training and inference cost on GPUs."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.04093) · [PDF](https://arxiv.org/pdf/2610.04093)

## 一句话摘要

Deep neural networks continue to grow in parameter count, driving up training and inference cost on GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep neural networks continue to grow in parameter count, driving up training and inference cost on GPUs. Sparse neural networks and Dynamic Sparse Training (DST) promise to reduce these costs, but most implementations rely on binary masks over dense tensors and recover little of the theoretical compute, memory, or energy savings. We propose SNACK, a truly sparse GPU layer that stores and computes only non-zero connections. SNACK exposes a simple PyTorch API for restructuring connections and backpropagating gradients entirely in the sparse paradigm, and ships SNACK-COO, a custom COO-format SpMM CUDA kernel with a batch-to-Streaming-Multiprocessor mapping tuned for the small-batch, high-sparsity regime typical of large-model training and single-stream inference. At the kernel level, SNACK is up to 7x faster than the masked dense baseline (Dense+Mask) and competitive with cuSPARSE, Sputnik, and FlashSparse at 95% sparsity. At 90% sparsity, a single SNACK layer accelerates training by 8x and 3.7x, and inference by 4x and 2x, over Dense+Mask and fully dense layers, respectively, while using 72% less memory than dense and substantially less energy. End-to-end, SNACK reduces GPT-2 peak training memory by up to 40% and graph-style inference latency by 4.8x over Dense+Mask at 99% sparsity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jafar Badour, Maurice van Keulen, Elena Mocanu
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
