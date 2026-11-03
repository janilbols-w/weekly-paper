---
title: "Vision Transformer Ensembles for Panoramic Street Segmentation"
description: "Semantic segmentation of street panoramas can support detailed descriptions of urban environments, yet small datasets and unequal training costs make model selection difficult."
---

**评分：39/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2610.06063) · [PDF](https://arxiv.org/pdf/2610.06063)

## 一句话摘要

Semantic segmentation of street panoramas can support detailed descriptions of urban environments, yet small datasets and unequal training costs make model selection difficult.

## 为什么值得关注

待编辑增强。

## 摘要原文

Semantic segmentation of street panoramas can support detailed descriptions of urban environments, yet small datasets and unequal training costs make model selection difficult. This paper documents the two stages of a submission to the PalmCity challenge. In the first stage, nine pretrained segmentation systems are compared using approximately equal computation budgets, and the two leading candidates are trained with three random seeds. An equal probability average of three Encoder only Mask Transformer models with DINOv3 features, evaluated at three image scales with horizontal reflection, reaches 60.95% mean intersection over union on the 84 image validation split and 57.08% on the hidden test leaderboard, first in the snapshot of 5 October 2026. In the second stage, color and crop augmentation, rare class sampling, larger inputs, further architectures, and post processing are tested under the same update budget, and candidates are compared through a paired image bootstrap with selection rules fixed before the results. Training at 768 by 1536 and 896 by 1792 pixels gives the largest gains. The selected ensemble of four models scores 64.53% on validation when trained on the training images alone. Retrained on the training and validation images, it receives 61.54% mean intersection over union and 71.93% mean F1 on the hidden test leaderboard, first among five entries in the snapshot of 30 October 2026. Segment Anything voting, instance mask overlays, and ensembles with other architectures all reduce the validation score. Because the validation images guided many choices and the final models were trained on them, the validation scores are optimistic and the test score is the only independent measurement. The study reports all runs, comparisons, costs, and limits, and releases the code and models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: all reduce
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yunus Serhat B{\i}\c{c}ak\c{c}{\i}
- 发布：2026-10-06；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
