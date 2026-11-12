---
title: "Neural Network-Assisted CLEAN for Efficient Multipath Parameter Estimation in MIMO Systems"
description: "High-resolution multipath estimation in wideband multiple-input multiple-output (MIMO) channels requires repeated searches over angle of arrival, angle of departure, and propagation distance."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.13298) · [PDF](https://arxiv.org/pdf/2611.13298)

## 一句话摘要

High-resolution multipath estimation in wideband multiple-input multiple-output (MIMO) channels requires repeated searches over angle of arrival, angle of departure, and propagation distance.

## 为什么值得关注

待编辑增强。

## 摘要原文

High-resolution multipath estimation in wideband multiple-input multiple-output (MIMO) channels requires repeated searches over angle of arrival, angle of departure, and propagation distance. This paper presents neural network-assisted CLEAN (NN-CLEAN), which replaces the multidimensional search at each extraction step with a multi-head classifier while retaining least-squares (LS) estimation of the complex path gain, parametric reconstruction, and residual cancellation. The same classifier is applied to successive residuals, allowing the extraction depth to vary without changing its output structure. With the number of iterations prescribed by the reference multipath-component (MPC) count, off-grid synthetic tests show that NN-CLEAN slightly exceeds grid-search CLEAN (GS-CLEAN) in path accuracy for one and two MPCs, although its accuracy declines more rapidly at larger path counts. For complete three-MPC extraction at a batch size of eight, NN-CLEAN achieves an approximately $27\times$ speedup and a $52$-fold reduction in peak GPU memory relative to GS-CLEAN. Applied without retraining to two-MPC line-of-sight (LOS) and non-line-of-sight (NLOS) Sionna ray-tracing channels within a coded MIMO link, NN-CLEAN substantially reduces channel-reconstruction mean-squared error (MSE) and bit error rate (BER) relative to interpolated LS channel estimation. GS-CLEAN retains an accuracy advantage on these channels, indicating the estimation cost associated with the computational savings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chaofan Deng, Linyu Sun, Jaeho Lee, Zishen Wan, Arijit Raychowdhury
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
