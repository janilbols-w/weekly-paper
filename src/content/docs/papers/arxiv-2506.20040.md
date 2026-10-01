---
title: "Cross-Layer Discrete Concept Discovery for Interpreting Language Models"
description: "Interpreting language models remains challenging due to the existence of residual stream, which linearly mixes and duplicates features across adjacent layers, causing single-layer analyses to miss this cross-layer structure."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2506.20040) · [PDF](https://arxiv.org/pdf/2506.20040)

## 一句话摘要

Interpreting language models remains challenging due to the existence of residual stream, which linearly mixes and duplicates features across adjacent layers, causing single-layer analyses to miss this cross-layer structure.

## 为什么值得关注

待编辑增强。

## 摘要原文

Interpreting language models remains challenging due to the existence of residual stream, which linearly mixes and duplicates features across adjacent layers, causing single-layer analyses to miss this cross-layer structure. Cross-layer sparse autoencoders (SAEs) address layer mixing but operate in continuous space, where concepts split across many neurons without clear boundaries. We introduce Cross-Layer Vector Quantized-Variational Autoencoder (CLVQ-VAE), a novel framework which maps representations from a lower layer to a higher layer through a discrete vector-quantization bottleneck, collapsing duplicated residual-stream features into compact, interpretable concept vectors. Our approach combines top-k temperature-based sampling with exponential moving average (EMA) codebook updates, providing controlled exploration of the discrete latent space while maintaining codebook diversity. Across both encoder- and decoder-based models on ERASER-Movie, Jigsaw, and AGNews, CLVQ-VAE outperforms clustering, single-layer vector quantized-variational autoencoder (VQ-VAE), and sparse autoencoder (SAE) baselines across three evaluation axes: removing identified concepts drops downstream probe accuracy by up to 93%, LLM judges rank our concepts first in 66.7% of comparisons, and human annotators recover model predictions from our visualizations with 78% accuracy versus 54% for clustering.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ankur Garg, Xuemin Yu, Hassan Sajjad, Samira Ebrahimi Kahou
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
