---
title: "LocalProp: Neuro-Localized Memory-Efficient Backpropagation"
description: "The current deep learning training paradigm employs end-to-end backpropagation, regardless of the training stage, i.e."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.32517) · [PDF](https://arxiv.org/pdf/2609.32517)

## 一句话摘要

The current deep learning training paradigm employs end-to-end backpropagation, regardless of the training stage, i.e.

## 为什么值得关注

待编辑增强。

## 摘要原文

The current deep learning training paradigm employs end-to-end backpropagation, regardless of the training stage, i.e. pre-training or fine-tuning. However, backpropagating through the entire model is neither biologically plausible nor memory efficient, since learning inside the brain is highly localized. Therefore, we propose LocalProp, a training procedure that locally updates the weights of a model. Our neuro-localized weight updates follow the "pre-training then fine-tuning" paradigm, where the pre-training is based on I-JEPA. After locally updating the weights, a pruning operation is performed, followed by a short final fine-tuning phase. Pruning helps by sending the learning signal from higher blocks to lower blocks. We perform experiments on several datasets, including large-scale benchmarks such as ImageNet, and empirically show that LocalProp reaches good performance at a fraction of GPU peak memory. By varying the number of jointly optimized blocks, we identify gradient-propagation span as a practical control over the accuracy-memory trade-off.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Diana-Nicoleta Grigore, Iuliana Georgescu, Radu Tudor Ionescu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
