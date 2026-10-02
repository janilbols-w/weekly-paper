---
title: "CrossGMN: Graph Metanetworks for Cross-Architecture Weight-Space Transformations"
description: "Weight-space networks operate directly on parameters of other neural networks, enabling tasks such as predicting model properties, editing trained models, and generating weights."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.01649) · [PDF](https://arxiv.org/pdf/2610.01649)

## 一句话摘要

Weight-space networks operate directly on parameters of other neural networks, enabling tasks such as predicting model properties, editing trained models, and generating weights.

## 为什么值得关注

待编辑增强。

## 摘要原文

Weight-space networks operate directly on parameters of other neural networks, enabling tasks such as predicting model properties, editing trained models, and generating weights. Weight-space symmetries such as neuron permutations make equivariance a key design principle. However, existing equivariant weight-space architectures have primarily been studied for transformations that preserve the network architecture. In contrast, many practical transformations, including model compression and upscaling, map a trained source network into a target network with a different architecture. In this setting, the source and target permutation symmetries act on different parameter spaces, making equivariance less straightforward to formulate. Our key idea for addressing this mismatch is to reformulate cross-architecture operators with two inputs: a trained source network and an initialization of the target network. This lets us define equivariant cross-architecture operators that refine the initialization of the target network using information from the source network, while being invariant to source-network permutations and equivariant to target-network permutations. Based on this formulation, we introduce CrossGMN, a graph metanetwork that jointly processes both networks through symmetry-preserving cross-network message passing. We prove CrossGMN is universal for continuous cross-architecture operators on compact sets under a general-position assumption. We evaluate CrossGMN for model compression, predicting a smaller network's parameters to accelerate subsequent knowledge distillation. Across 2-D and 3-D INRs and image classification with MLPs, CNNs, and Vision Transformers, CrossGMN speeds up distillation by up to 8.89x, transfers across datasets without retraining (3.78x), and a single model can accelerate compression from heterogeneous source architectures into a common target architecture.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Adir Dayan, Yam Eitan, Haggai Maron
- 发布：2026-10-01；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
