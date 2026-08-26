---
title: "Deep Feature Pyramid Convolutional Networks with In-Place Activated Batch Normalization for Automated Skin Lesion Boundary Segmentation"
description: "Segmentation of skin lesion boundaries in dermoscopic imaging is an important prerequisite step for computer-aided diagnosis of malignant melanoma, but remains challenging due to fuzzy margins, occluding artifacts such as hair and blood vessels, low contrast, and high inter-patient variability."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/1812.00877) · [PDF](https://arxiv.org/pdf/1812.00877)

## 一句话摘要

Segmentation of skin lesion boundaries in dermoscopic imaging is an important prerequisite step for computer-aided diagnosis of malignant melanoma, but remains challenging due to fuzzy margins, occluding artifacts such as hair and blood vessels, low contrast, and high inter-patient variability.

## 为什么值得关注

待编辑增强。

## 摘要原文

Segmentation of skin lesion boundaries in dermoscopic imaging is an important prerequisite step for computer-aided diagnosis of malignant melanoma, but remains challenging due to fuzzy margins, occluding artifacts such as hair and blood vessels, low contrast, and high inter-patient variability. This work presents a memory-efficient deep convolutional neural network framework for lesion boundary segmentation, developed for the ISIC 2018 Challenge (Task 1: Lesion Boundary Segmentation). A U-Net-style encoder-decoder architecture is adapted using Wide ResNet38 and Dual Path Network (DPN) backbones with a Feature Pyramid Network (FPN) decoder, pretrained on ImageNet. In-Place Activated Batch Normalization (InPlace-ABN) reduces memory consumption during training, allowing higher-capacity ensembling under standard GPU memory constraints, combined with five-fold cross-validation, extensive augmentation, snapshot ensembling, and test-time augmentation. The best-performing model achieves a Thresholded Jaccard score of 0.752 on the ISIC 2018 Challenge evaluation, with single-model configurations scoring between 0.700 and 0.750; InPlace-ABN reduces memory consumption by approximately 25%. To contextualize this result against current practice, a simplified single-model U-Net baseline retrained in 2026 using standard modern tooling is also reported, achieving a Dice score of 0.8443 (IoU 0.7608, Thresholded Jaccard 0.6680), which highlights the substantial contribution of ensembling and pretraining to the original result. This work does not claim state-of-the-art segmentation accuracy; rather, it documents a memory-efficient training approach that enables higher-capacity ensembling under constrained GPU resources, a practical consideration for training high-capacity segmentation models in settings with limited computational budgets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Glib Kechyn
- 发布：2026-08-26；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
