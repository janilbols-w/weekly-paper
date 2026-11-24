---
title: "Model Carving: Training Transformers That Optimize Their Own Topology"
description: "Machine learning has largely kept separate the choice of architecture and the process of training."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.27962) · [PDF](https://arxiv.org/pdf/2611.27962)

## 一句话摘要

Machine learning has largely kept separate the choice of architecture and the process of training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Machine learning has largely kept separate the choice of architecture and the process of training. A classic Transformer, for instance, trains a fixed set of attention and MLP sublayers at every layer, in the same order, and optimizes the weights within. This uniformity is a convention rather than a principled design choice, and it is likely suboptimal: the best architecture for a given task may be smaller, more efficient, and far from uniform. We believe that, ideally, training itself should shape the model's topology. To this end, we introduce Model Carving, which learns both a Transformer's weights and its architecture in a single run. By applying learnable, scalar gates to each sublayer, we allow the training loss to remove the model's own components during training -- freeing a smaller heterogeneous network inside. We evaluate Model Carving by pre-training standard Transformers from 140M to 2.7B parameters and looped Transformers from 140M to 1.3B. At equal training compute, carved models reach a lower validation loss than dense models trained with up to 1.7 times more compute. Furthermore, carved models also outperform size-matched models produced by pruning or distillation, suggesting that the best way to obtain small models for edge devices is to carve them during training, not to compress a large one afterwards. This advantage both grows with scale and carries over to downstream tasks such as few-shot evaluation and generation. Because the removed sublayers no longer run, carved models also cost up to 34% fewer FLOPs per token and decode up to 1.6 times faster without cost in quality. Our results show that architecture, like weights, should be learned and not fixed in advance, and that inside every large transformer is a smaller, faster, stronger one waiting to be carved out.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kaden Zheng, Pratyusha Sharma
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
