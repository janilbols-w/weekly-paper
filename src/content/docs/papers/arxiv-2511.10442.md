---
title: "FastGraph: PCA-Subspace Binned k-Nearest-Neighbor Graph Construction for GPU Geometric Deep Learning"
description: "Dynamic graph neural networks repeatedly construct k-nearest-neighbor graphs in learned latent spaces, making GPU-accelerated graph construction an important operation in scientific point-cloud workloads."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2511.10442) · [PDF](https://arxiv.org/pdf/2511.10442)

## 一句话摘要

Dynamic graph neural networks repeatedly construct k-nearest-neighbor graphs in learned latent spaces, making GPU-accelerated graph construction an important operation in scientific point-cloud workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Dynamic graph neural networks repeatedly construct k-nearest-neighbor graphs in learned latent spaces, making GPU-accelerated graph construction an important operation in scientific point-cloud workloads. We present FastGraph, a PyTorch-integrated primitive for exact kNN graph construction in low-to-moderate-dimensional spaces. FastGraph uses a PCA-subspace cell list: it fits a compact binning coordinate system to the input tensor, uses that subspace for spatial pruning, and evaluates all candidate distances in the original feature space. The data-adaptive orthonormal subspace improves uniform-grid pruning in the d=4-10 range evaluated around the d=4 GravNet operating point. Point data remain GPU-resident, with small host synchronizations for control metadata. The implementation ships with an eager-mode PCA API and an opt-in differentiable GravNetOp integration. On a 5 M-point, single-segment detector-derived HGCAL recHit stress test, FastGraph builds the exact graph in 7.5 s at d=8, k=40, achieving speedups of up to 41x over FAISS-GPU, 19x over cuVS brute force, and 17x over approximate CAGRA while retaining exact neighbor sets under the paper's distance-based convention.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aarush Agarwal, Jan Kieseler, Raymond He, Matteo Cremonesi, Shah Rukh Qasim
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
