---
title: "Vision Transformer Ensembles for Panoramic Street Segmentation"
description: "Semantic segmentation of street panoramas can support detailed descriptions of urban environments, yet small datasets and unequal training costs make model selection difficult."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.06063) · [PDF](https://arxiv.org/pdf/2610.06063)

## 一句话摘要

Semantic segmentation of street panoramas can support detailed descriptions of urban environments, yet small datasets and unequal training costs make model selection difficult.

## 为什么值得关注

待编辑增强。

## 摘要原文

Semantic segmentation of street panoramas can support detailed descriptions of urban environments, yet small datasets and unequal training costs make model selection difficult. This paper presents the system used for a first place submission to the PalmCity challenge in the leaderboard snapshot dated 5 October 2026. Nine pretrained segmentation systems are compared using approximately equal computation budgets. The candidates include DeepLabV3+, SegFormer, UPerNet, Mask2Former, DINOv3 with a linear decoder, and an Encoder only Mask Transformer using DINOv3. The two leading candidates are trained independently with three random seeds and longer budgets. Equal averaging of class probabilities from the three Encoder only Mask Transformer models, evaluated at three image scales with horizontal reflection, produces 60.95% mean intersection over union and 71.16% mean F1 on the 84 image public validation split. The submitted predictions receive 57.08% mean intersection over union and 67.96% mean F1 on the hidden test leaderboard. Producing all 249 test masks takes 251.49 seconds including model initialization and provenance checks on one NVIDIA RTX 5090. Peak allocated GPU memory is 2.70 GiB. The study reports all eligible models, all inference variants, class level errors, source conditions, and reproducibility checks, providing a documented challenge workflow with existing architectures.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yunus Serhat B{\i}\c{c}ak\c{c}{\i}
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
