---
title: "Adaptive multi-resolution Gaussian processes: Scalable exact inference with naturally data-sparse covariance matrices"
description: "Gaussian processes constitute a cornerstone of probabilistic machine learning, yet scaling them to large datasets typically forces a trade-off between computational efficiency and model fidelity."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.30348) · [PDF](https://arxiv.org/pdf/2609.30348)

## 一句话摘要

Gaussian processes constitute a cornerstone of probabilistic machine learning, yet scaling them to large datasets typically forces a trade-off between computational efficiency and model fidelity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Gaussian processes constitute a cornerstone of probabilistic machine learning, yet scaling them to large datasets typically forces a trade-off between computational efficiency and model fidelity. This work bridges this gap by presenting an adaptive multi-resolution Gaussian process framework that is both scalable and exact. Our key innovation is constructing a naturally data-sparse covariance matrix with adaptive multi-resolution basis functions. These basis functions are directly anchored to samples, eliminating the need for auxiliary points. By shrinking the support domains of multi-resolution basis, the matrix block sizes are limited, guaranteeing sparsity. The inverse of the data-sparse covariance matrix is computed exactly and efficiently via the sparse Cholesky inverse algorithm. To further improve predictive uncertainties, we construct an augmented basis function. Theoretical analysis and numerical experiments demonstrate that our model achieves exact inference with $\mathcal{O}(n \log^2 n)$ training cost and $\mathcal{O}(\log^d n)$ prediction cost, establishing a principled framework for scalable and high-fidelity Gaussian process regression.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yanchuang Cao, Jun Liu, Tengchao Yu, Heng Yong
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
