---
title: "Energy Variation in Training Modern Computer Vision Architectures"
description: "The rapid growth of deep learning has substantially increased the energy consumption associated with model training, making energy efficiency an increasingly relevant design criterion."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.03772) · [PDF](https://arxiv.org/pdf/2610.03772)

## 一句话摘要

The rapid growth of deep learning has substantially increased the energy consumption associated with model training, making energy efficiency an increasingly relevant design criterion.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid growth of deep learning has substantially increased the energy consumption associated with model training, making energy efficiency an increasingly relevant design criterion. This study empirically measures the energy variation of training seven modern computer vision architectures, MobileNetV3-Small, MobileNetV3-Large, EfficientNet-B0, EfficientNet-B1, ViT-B/32, ConvNeXt-Tiny, and ViT-B/16 for the ImageNet-1k classification task, using a homogeneous 10,000-image subset (ImageNet-10k) and a uniform 40-epoch baseline configuration executed on two NVIDIA Tesla P100 GPUs at the Bioinformatics and Computational Biology Center of Colombia (BIOS). Energy was recorded directly via NVML and contrasted with the computational complexity of each model. The results show a Pearson correlation of 0.85 between floating-point operations (GFLOPs) and energy consumption in kWh, indicating that computational complexity is a strong but imperfect predictor of energy expenditure: architectures with comparable GFLOPs exhibited consumption differing by up to 3.1x due to differences in the hardware efficiency of their dominant operations. The EfficientNet variants offered the best balance between classification performance (Val Top-5 up to 97.15%) and energy efficiency (0.457-0.611 kWh), while Vision Transformers exhibited the highest relative energy consumption and lower classification performance under the evaluated configuration. These findings guide architecture selection in energy-constrained computing environments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：David Cortes, Carlos Juiz, Belen Bermejo
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
