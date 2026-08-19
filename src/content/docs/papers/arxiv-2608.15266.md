---
title: "BrainLinear: A Linear Model for Brain Network Analysis in Sparse Tangent Subspaces"
description: "Functional connectome analysis examines brain-region interactions to understand and identify disorders such as autism spectrum disorder and Alzheimer's disease."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.15266) · [PDF](https://arxiv.org/pdf/2608.15266)

## 一句话摘要

Functional connectome analysis examines brain-region interactions to understand and identify disorders such as autism spectrum disorder and Alzheimer's disease.

## 为什么值得关注

待编辑增强。

## 摘要原文

Functional connectome analysis examines brain-region interactions to understand and identify disorders such as autism spectrum disorder and Alzheimer's disease. Existing methods typically use GNNs and Transformers to model the full functional connectivity matrix. However, processing tens of thousands of connections introduces redundancy and noise, increases computational cost, and limits connection-level interpretability. This raises a central question: do we really need complex interaction modeling, or is identifying a small set of disease-relevant connectivity patterns sufficient? To answer this question, we propose BrainLinear, a lightweight geometry-aware framework for mining disease-discriminative connectome patterns. BrainLinear first maps each functional connectivity matrix to a shared tangent space centered at the Fr\'echet mean of the training set, capturing subject-specific deviations while respecting matrix geometry. It then scores each ROI-pair tangent direction by its classification contribution and disease--control difference, retaining Top-$K$ directions as a compact representation. Finally, a shallow multilayer perceptron performs classification on the selected representation. Experiments on ABIDE and ADNI show that BrainLinear matches or exceeds strong GNN and Transformer baselines at a fraction of their cost: it improves AUC and ACC over the best baseline for each metric by up to $3.54$ and $1.39$ percentage points, while reducing runtime and peak GPU memory by $84.0\%$ and $68.4\%$ relative to the closest baseline in AUC. The selected directions are directionally consistent with between-group displacements and organized across major functional systems, supporting connection-level interpretation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sijing Wu, Dongyuan Li, Miaoting Huang, Weiwei Ye, Ying Zhang, Feng Xia, Renhe Jiang
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
