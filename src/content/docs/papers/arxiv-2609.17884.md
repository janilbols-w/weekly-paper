---
title: "The Unbearable Weight: Scaling Models and Methods for UAV Audio Classification"
description: "As unmanned aerial vehicles (UAVs) become increasingly prevalent in consumer and defense settings, classifying them reliably from limited, modality-specific data is an urgent challenge."
---

**评分：38/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.17884) · [PDF](https://arxiv.org/pdf/2609.17884)

## 一句话摘要

As unmanned aerial vehicles (UAVs) become increasingly prevalent in consumer and defense settings, classifying them reliably from limited, modality-specific data is an urgent challenge.

## 为什么值得关注

待编辑增强。

## 摘要原文

As unmanned aerial vehicles (UAVs) become increasingly prevalent in consumer and defense settings, classifying them reliably from limited, modality-specific data is an urgent challenge. The dominant approach, large pretrained networks fully fine-tuned on task data, carries a substantial computational and memory weight that is hard to bear in resource-constrained UAV deployments, where edge inference and rapid retraining for emerging platforms are both required. This paper systematically scales across both model architectures and fine-tuning methods for UAV audio classification, asking when that weight is justified and when lighter alternatives prevail. Using a custom dataset of 3,100 audio clips spanning 31 drone classes, we evaluate transformer (ViT, AST) and convolutional (custom CNN, ResNet-18/152, MobileNet-V3-S/L, EfficientNet-B0/B7) backbones under full fine-tuning, classifier-only fine-tuning, and four parameter-efficient fine-tuning (PEFT) methods: SSF, IA3, OFT, and selective batch-norm tuning. All configurations are evaluated with 5-fold cross-validation across accuracy, training time, trainable-parameter share, and inference-time memory footprint. Selective batch-norm fine-tuning of EfficientNet-B7 with three-fold augmentations achieves the highest validation accuracy (97.65% +- 0.30) while updating under 0.5% of model parameters. Across the sweep, lightweight CNNs consistently outperform transformers on both accuracy and efficiency. For UAV audio classification under data scarcity, scaling the method outperforms scaling the model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: edge inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Andrew P. Berg, Qian Zhang, Mia Y. Wang
- 发布：2026-09-15；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
