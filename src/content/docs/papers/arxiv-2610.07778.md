---
title: "Towards One-for-All Foundation Model for Attributed Graph Clustering"
description: "Attributed graph clustering aims to discover node groups by jointly exploiting node attributes and graph topology, yet its unsupervised nature makes model selection and adaptation inherently difficult."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.07778) · [PDF](https://arxiv.org/pdf/2610.07778)

## 一句话摘要

Attributed graph clustering aims to discover node groups by jointly exploiting node attributes and graph topology, yet its unsupervised nature makes model selection and adaptation inherently difficult.

## 为什么值得关注

待编辑增强。

## 摘要原文

Attributed graph clustering aims to discover node groups by jointly exploiting node attributes and graph topology, yet its unsupervised nature makes model selection and adaptation inherently difficult. Existing methods typically train and tune a separate model for each input graph, leading to costly and fragile pipelines that often fail to transfer across graphs with different feature spaces, structural patterns, and attribute-structure correlations. In this paper, we study a one-for-all alternative: can a single model be trained once and directly applied to diverse attributed graphs without graph-specific training, fine-tuning, or hyperparameter search? We propose OFAG, a foundation model for attributed graph clustering. Building upon Prior-data Fitted Networks, OFAG learns a reusable clustering inference strategy from synthetic attributed graphs generated under broad priors over latent clusters, node attributes, and graph structures. To handle incompatible feature spaces across graphs, OFAG adopts a dimension-agnostic signal-wise graph encoder that treats each feature channel as a graph signal and models its response to shared graph filters. The model is trained with a hyperspherical clustering objective, producing clustering-friendly node representations in a single forward pass at inference time. On ten datasets, one frozen OFAG model achieves the best mean performance and average rank across NMI, ACC, ARI, and F1, while completing all ten datasets in 12.43 minutes total---over 6* faster than the second-fastest baseline and nearly 28* faster than the second-best on clustering quality. Our code and pretrained checkpoint are available at https://github.com/Cloudy1225/OFAG, allowing practitioners to directly apply OFAG to their own attributed graph datasets without additional training or tuning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yunhui Liu, Xudong Jin, Kang Zhang, Danshuo An, Yu Xing, Te Song, Jia Liu, Tieke He
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Cloudy1225/OFAG](https://github.com/Cloudy1225/OFAG)
- 阅读深度：metadata
