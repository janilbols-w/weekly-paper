---
title: "COMPOT: Calibration-Optimized Matrix Procrustes Orthogonalization for Transformers Compression"
description: "Post-training compression of transformer models commonly relies on truncated singular value decomposition (SVD) strategies leading to low-rank approximations of the original model weights."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2602.15200) · [PDF](https://arxiv.org/pdf/2602.15200)

## 一句话摘要

Post-training compression of transformer models commonly relies on truncated singular value decomposition (SVD) strategies leading to low-rank approximations of the original model weights.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training compression of transformer models commonly relies on truncated singular value decomposition (SVD) strategies leading to low-rank approximations of the original model weights. However, the underlying single shared subspace modeling can degrade accuracy even at moderate compression. Sparse dictionary learning provides a more flexible union-of-subspaces representation, but existing approaches often suffer from costly iterative dictionary and coefficient updates. We propose $\textbf{COMPOT}$ ($\textbf{C}$alibration-$\textbf{O}$ptimized $\textbf{M}$atrix $\textbf{P}$rocrustes $\textbf{O}$rthogonalization for $\textbf{T}$ransformers), a training-free compression framework that uses a small calibration dataset to estimate a sparse weight factorization. COMPOT employs orthogonal dictionaries that enable closed-form Procrustes updates for the dictionary and analytical single-step sparse coding for the coefficients, reducing significantly the overall optimization cost. To handle heterogeneous layer sensitivity under a global compression budget, COMPOT further introduces a one-shot dynamic allocation strategy that adaptively redistributes layer-wise compression rates. Extensive experiments across diverse architectures and tasks show that COMPOT consistently delivers a superior quality-compression trade-off over strong low-rank and sparse baselines, while remaining fully compatible with post-training quantization for extreme compression.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Denis Makhov, Dmitriy Shopkhoev, Magauiya Zhussip, Ammar Ali, Baher Mohammad, Stamatios Lefkimmiatis
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
