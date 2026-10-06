---
title: "MercerFlow: Flow Matching in a Kernel-Induced Latent Space for Probabilistic Forecasting"
description: "Recent work has shown that probabilistic flow matching for time series forecasting benefits from a data-matched prior."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.06039) · [PDF](https://arxiv.org/pdf/2610.06039)

## 一句话摘要

Recent work has shown that probabilistic flow matching for time series forecasting benefits from a data-matched prior.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent work has shown that probabilistic flow matching for time series forecasting benefits from a data-matched prior. The resulting prior introduces local correlations, which a sequential architecture usually absorbs: a recurrent neural network (RNN), a structured state-space model (S4), or a Transformer. However, such a backbone costs GPU memory and time per epoch. A cheaper alternative is MLP-based latent-space flow matching: embed the time series via an invertible map to a single latent vector and learn the flow there, so a tabular MLP can treat the series as a set of features. The relationship between the prior and the choice of linear latent map is understudied in conditional flow matching (CFM) forecasting, yet we found it strongly affects performance. Fixed transforms such as Fourier or discrete cosine (DCT) are only well-conditioned for Ornstein--Uhlenbeck priors, while a principal-component (PCA) map fit to the data is a strong but training-set-dependent reference sensitive to train--test shift. Instead, we propose to use the Mercer eigenbasis of the prior kernel: it diagonalises the centred covariance exactly, decouples from training data, and adapts to non-stationary and periodic priors. On five GluonTS benchmarks (ETTh1, ETTh2, Weather, Electricity, Traffic) under a shared protocol with TSFlow, the resulting MLP matches or beats it on CRPS at about $4.7\times$ less training memory and $3.5\times$--$4.4\times$ less time per epoch.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ilya Kuleshov, Egor Serov, Alexey Zaytsev
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
