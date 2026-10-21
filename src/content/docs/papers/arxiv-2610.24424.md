---
title: "Toward a Universal Local Speech Feature Extractor Through Distillation"
description: "Self-supervised speech models commonly consist of a set of convolutional neural network (CNN) layers used as a local feature extractor, followed by transformer layers."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.24424) · [PDF](https://arxiv.org/pdf/2610.24424)

## 一句话摘要

Self-supervised speech models commonly consist of a set of convolutional neural network (CNN) layers used as a local feature extractor, followed by transformer layers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-supervised speech models commonly consist of a set of convolutional neural network (CNN) layers used as a local feature extractor, followed by transformer layers. The CNN layers are computationally demanding, and are also similar across models and resemble the much simpler mel spectral features. We hypothesize that the CNN layers can be replaced by a simple, universal model. To test this hypothesis, we learn a two-layer feature extractor via distillation from one or more teacher models (HuBERT, data2vec, and WavLM). Experiments on SUPERB(-SG) benchmark tasks show that our model largely retains the performance of the teacher models and can also be used in an unseen model (wav2vec 2.0). Our feature extractor requires only 3% of the MACs of the CNNs, resulting in a $>$20% overall inference runtime reduction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jessica Yang, Marcelo Beramendi Caballero, Ju-Chieh Chou, Karen Livescu
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
