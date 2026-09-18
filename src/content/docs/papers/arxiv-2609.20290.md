---
title: "TinyCNN: A 193K-Parameter Network for On-Device Plant Disease Detection, with a Cross-Dataset Robustness Diagnosis"
description: "Detecting crop disease early is central to sustainable agriculture and food security under United Nations Sustainable Development Goal 2 (Zero Hunger), and is especially urgent in resource-constrained regions where expert diagnosis is scarce but low-cost mobile devices are widespread."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.20290) · [PDF](https://arxiv.org/pdf/2609.20290)

## 一句话摘要

Detecting crop disease early is central to sustainable agriculture and food security under United Nations Sustainable Development Goal 2 (Zero Hunger), and is especially urgent in resource-constrained regions where expert diagnosis is scarce but low-cost mobile devices are widespread.

## 为什么值得关注

待编辑增强。

## 摘要原文

Detecting crop disease early is central to sustainable agriculture and food security under United Nations Sustainable Development Goal 2 (Zero Hunger), and is especially urgent in resource-constrained regions where expert diagnosis is scarce but low-cost mobile devices are widespread. This paper presents TinyCNN, a lightweight convolutional neural network for on-device plant disease classification. TinyCNN uses depthwise separable convolution blocks and contains only 193,190 trainable parameters with 110.05M MACs for a 224x224 input image. On the 38-class PlantVillage benchmark, TinyCNN achieves 98.88% test accuracy and 98.03% macro-F1 while being approximately 58x smaller than ResNet18 and 11.8x smaller than a MobileNetV2 teacher, directly reducing the energy, memory, and cost footprint of inference in line with Green AI principles. The paper further analyzes vanilla knowledge distillation as a sustainable model-compression strategy; an ablation over alpha in {0.3, 0.5, 0.7} and T in {2, 4} selects alpha=0.3, T=4, producing a distilled TinyCNN with 98.81% test accuracy. Finally, cross-dataset evaluation from PlantVillage to PlantDoc reveals a substantial robustness gap under real-world conditions, which a Grad-CAM analysis attributes to off-leaf, background-driven attention consistent with shortcut learning. TinyCNN is thus an energy-efficient, deployable building block for sustainable agricultural intelligence, while field robustness remains the key barrier to durable real-world impact.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ngoc-Bao Ho-Lam, Thai-Anh Nguyen
- 发布：2026-09-18；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
