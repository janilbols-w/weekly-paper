---
title: "SOCKET: SOft Collision Kernel EsTimator for Sparse Attention"
description: "Exploiting sparsity is key to efficient long-context inference, as attention dominates the cost of autoregressive decoding."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.06283) · [PDF](https://arxiv.org/pdf/2602.06283)

## 一句话摘要

Exploiting sparsity is key to efficient long-context inference, as attention dominates the cost of autoregressive decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Exploiting sparsity is key to efficient long-context inference, as attention dominates the cost of autoregressive decoding. Sparse attention reduces this cost by restricting computation to a subset of tokens, but its effectiveness hinges on fast and accurate token scoring and selection at inference time. Data-agnostic approaches offer an attractive way to perform this selection, but often incur substantial memory overhead to maintain high recall. We revisit Locality-Sensitive Hashing (LSH) and introduce SOCKET, a SOft Collision Kernel EsTimator that replaces hard bucket matches with probabilistic, similarity-aware aggregation. Traditional LSH relies on binary collision signals, providing limited information for ranking tokens and necessitating many hash tables for accurate retrieval. In contrast, soft LSH accumulates graded collision evidence across hash tables, closely preserving the true top-$k$ ordering with significantly less memory. This reframes LSH from a candidate-generation mechanism into a principled scoring kernel for sparse attention. Building on this insight, SOCKET enables efficient token selection without ad hoc voting and matches or outperforms existing sparse attention methods across multiple long-context benchmarks and diverse language models. With a custom set of CUDA/Triton kernels for scoring, selection, and attention, SOCKET achieves up to approximately $1.5\times$ higher throughput than FlashAttention. Code is open-sourced at https://github.com/amarka8/SOCKET.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Sahil Joshi, Agniva Chowdhury, Wyatt Bellinger, Amar Kanakamedala, Ekam Singh, Hoang Anh Duy Le, Aditya Desai, Anshumali Shrivastava
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/amarka8/SOCKET](https://github.com/amarka8/SOCKET)
- 阅读深度：metadata
