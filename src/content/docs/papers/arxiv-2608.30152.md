---
title: "Converse and Collision-Based Achievability for Node Localization with Hybrid Distance-Spectral Graph Positional Encodings"
description: "Graph positional encodings are widely used in graph neural networks and graph Transformers, yet it remains unclear when the code itself can identify nodes."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.30152) · [PDF](https://arxiv.org/pdf/2608.30152)

## 一句话摘要

Graph positional encodings are widely used in graph neural networks and graph Transformers, yet it remains unclear when the code itself can identify nodes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Graph positional encodings are widely used in graph neural networks and graph Transformers, yet it remains unclear when the code itself can identify nodes. We study a hybrid distance-spectral encoding that combines anchor-distance profiles with quantized low-frequency Laplacian-energy coordinates. Treating the encoding as an observation map yields a simplex-refined converse, an exact collision factorization \(\kappa_H=\kappa_D\kappa_{S|D}\), and the collision information \(I_H=-\log\kappa_D-\log\kappa_{S|D}\). On random regular graphs, the criterion is made explicit through a bounded-correlation Gaussian-wave surrogate; for actual Laplacian-energy coordinates, we give the distance-conditioned spectral collision condition sufficient for conditional actual-coordinate achievability. Experiments show that \(I_H/\log n\) calibrates localization success, and PE-only structural task probes on Universal Dependencies trees show that hybrid encodings better recover syntactic-tree geometry than distance-only or spectral-only baselines.

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

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zimo Yan, Yifan Li, Hao Li, Zheng Xie, Chang Liu, Zheming Tu, Yuan Wang
- 发布：2026-08-31；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
