---
title: "Subspace Node Pruning"
description: "Node pruning is the art of removing computational units such as neurons, filters, attention heads, or even entire layers to significantly reduce inference time while retaining network performance."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2405.17506) · [PDF](https://arxiv.org/pdf/2405.17506)

## 一句话摘要

Node pruning is the art of removing computational units such as neurons, filters, attention heads, or even entire layers to significantly reduce inference time while retaining network performance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Node pruning is the art of removing computational units such as neurons, filters, attention heads, or even entire layers to significantly reduce inference time while retaining network performance. In this work, we show that a broad family of importance measures, from activation-based to Fisher-based, share a common quadratic form. Through a lower-triangular change of basis, this form yields a pruning subspace in which entire nodes can be removed while the impact of the lost units is simultaneously recovered via linear least squares. Furthermore, the importance measures within our subspace are decoupled and additive through an orthogonalization of the layer activations, allowing multi-node pruning within layers without interference between importance scores. Our method, Subspace Node Pruning (SNP), outperforms the compared baselines on VGG-16 and ResNet-50 on ImageNet. On OPT-125M and LLaMA-2 7B, SNP matches the state-of-the-art LLM Surgeon at a 40-shot schedule and outperforms it whenever fewer shots are used, all without any retraining after pruning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Joshua Offergeld, John Chidiac, Marcel van Gerven, Nasir Ahmad
- 发布：2026-11-04；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
