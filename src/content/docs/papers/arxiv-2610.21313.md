---
title: "PSA: A Pruning-Friendly Sparse-Aware Accelerator for Efficient Sparse Convolution in SNNs"
description: "Spiking neural networks (SNNs) are promising for energy-efficient artificial intelligence due to their event-driven sparse computation, and neuron pruning can further reduce redundant operations."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.21313) · [PDF](https://arxiv.org/pdf/2610.21313)

## 一句话摘要

Spiking neural networks (SNNs) are promising for energy-efficient artificial intelligence due to their event-driven sparse computation, and neuron pruning can further reduce redundant operations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking neural networks (SNNs) are promising for energy-efficient artificial intelligence due to their event-driven sparse computation, and neuron pruning can further reduce redundant operations. However, in practical hardware accelerators, spike sparsity and pruning-induced sparsity produce highly irregular sparse workloads that are difficult to execute efficiently. Existing approaches do not jointly support sparse-input execution, low-overhead sparse convolution lowering and pruning-friendly execution. This paper presents PSA, a Pruning-friendly Sparse-aware Accelerator for efficient sparse convolution in SNNs. PSA features a Sparse-Aware Merge-Accumulation (SAMA) dataflow that aligns sparse spike indices and converts irregular activations into continuous computation streams for efficient sparse convolution execution. It further introduces a Sparse Implicit Group-wise im2col (SIG-im2col) convolution lowering mechanism that converts sparse convolution into SpMM on-chip with low mapping cost and memory overhead. In addition, PSA integrates a lightweight pruning-friendly gating mechanism to directly support pruned SNNs. Results on ResNet-18/CIFAR-10 show that PSA achieves a 4.45x improvement in energy efficiency and an 18.52x reduction in energy-delay product (EDP) over the dense baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Sanhe Fu, Kainan Wang, Bo Wang, Aili Wang
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
