---
title: "SETAREH Transform: A Sorting-Assisted Haar-Wavelet Sparsification Method for Approximate Inner-Product Computation"
description: "Modern deep learning systems increasingly rely on high-dimensional vector operations, in which large input and parameter vectors are repeatedly stored, transferred, and processed."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.23338) · [PDF](https://arxiv.org/pdf/2610.23338)

## 一句话摘要

Modern deep learning systems increasingly rely on high-dimensional vector operations, in which large input and parameter vectors are repeatedly stored, transferred, and processed.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern deep learning systems increasingly rely on high-dimensional vector operations, in which large input and parameter vectors are repeatedly stored, transferred, and processed. Although substantial research has focused on reducing neural-network model size through pruning, quantization, knowledge distillation, and efficient architectures, the storage, memory-traffic, and communication costs associated with repeatedly presented high-dimensional input vectors remain important practical considerations, particularly in distributed and edge-computing environments. This paper proposes the SETAREH (Sorting-assisted Energy-concentrating Transform for Approximate Representation using Haar wavelets) transform, a Haar-wavelet-based sparsification approach for approximating the inner product between a fixed high-dimensional coefficient vector and successive input vectors. By applying the same sequence of permutations and Haar transforms to both vectors, SETAREH preserves the exact inner product before truncation. It then retains only a subset of the transformed coefficient-input pairs, reducing their representation cost while introducing a controllable approximation error. To evaluate SETAREH, we consider two complementary experimental settings: a synthetic Gaussian-vector baseline and a real apparent-age estimation task using a convolutional neural network on the APPA-REAL dataset. The results show that SETAREH can approximate the evaluated inner products using substantially fewer transformed coefficient-input pairs than the original vector dimension. The findings support its use as a potential structured data-representation method for repeated inner products with fixed weights, while the practical benefit depends on approximation accuracy and the cost of storing or transmitting permutation metadata.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Seyed Kamaledin Setarehdan
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
