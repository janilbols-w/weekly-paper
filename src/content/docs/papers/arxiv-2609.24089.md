---
title: "FlashBoB: I/O-Efficient Exact Backward-over-Backward for Softmax Attention"
description: "Transformer models built on the attention mechanism have become a central building block in modern deep learning, yet softmax attention remains a major bottleneck for long-context workloads."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.24089) · [PDF](https://arxiv.org/pdf/2609.24089)

## 一句话摘要

Transformer models built on the attention mechanism have become a central building block in modern deep learning, yet softmax attention remains a major bottleneck for long-context workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer models built on the attention mechanism have become a central building block in modern deep learning, yet softmax attention remains a major bottleneck for long-context workloads. While FlashAttention makes the forward and first backward passes I/O-efficient, it does not support backward-over-backward (BoB), which enables exact differentiation through the backward pass for applications such as second-order optimization, test-time training, gradient-based memory, and meta-learning. Existing BoB implementations either materialize large intermediate tensors or exhaust GPU memory at long sequence lengths. We present FlashBoB, an exact, I/O-efficient algorithm for BoB in softmax attention that keeps computation within on-chip tiles and avoids all $N \times N$ intermediate tensors, where $N$ is the sequence length. The key insight is a hierarchical affine structure in the softmax double backward: two row-wise scalars determine all outputs through affine transformations. This yields a two-pass schedule with bounded on-chip static random-access memory (SRAM) usage and minimal off-chip high-bandwidth memory (HBM) traffic. FlashBoB achieves $\Theta(N^2 d^2/M)$ HBM traffic ($d$ is the head dimension and $M$ is the memory size) and, within the standard FlashAttention-style score-recomputation model, matches the inherited large-cache lower bound for exact forward attention. Empirically, it scales exact attention BoB to $N=262\text{K}$ on a single A100 80GB GPU, where prior PyTorch exact baselines fail by $N=16\text{K}$, and is up to $6.3\times$ faster than FlashBack. These results make exact second-order attention practical at long-context sequence lengths where prior implementations cannot run efficiently.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anthony Givans, Michael Crawshaw, Mingrui Liu
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
