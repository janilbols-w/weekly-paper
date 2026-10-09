---
title: "DADP: Dynamic Activity-Dependent Pruning, A Reverse Hebbian-Inspired Structural Pruning Method"
description: "Modern neural networks are heavily over-parameterized."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.11853) · [PDF](https://arxiv.org/pdf/2610.11853)

## 一句话摘要

Modern neural networks are heavily over-parameterized.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern neural networks are heavily over-parameterized. This redundancy incurs substantial compute and memory overhead during training and inference. Existing pruning methods rely on post-hoc magnitude thresholds or static initialization heuristics. Consequently, they often require manual per-layer sparsity targets or expensive retraining cycles. We propose Dynamic Activity-Dependent Pruning (DADP), a biologically inspired structural plasticity mechanism. During training, DADP measures connection importance via the accumulated product of pre-synaptic activations and post-synaptic error gradients. Using a single global threshold instead of fixed layer budgets, DADP dynamically allocates sparsity across network depth while naturally inducing neuron- and channel-level pruning. Across MLP, VGG-16, ResNet-18, BiLSTM-CRF, and MiniBERT architectures, DADP matches or outperforms Magnitude, SNIP and RigL, retaining 73.67% accuracy (dense baseline: 76.06%) at 99% sparsity on ResNet-18. Finally, matrix-based Shannon entropy and effective rank measurements confirm that DADP preserves latent feature diversity at extreme sparsities without representation collapse.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bhushan Deshpande
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
