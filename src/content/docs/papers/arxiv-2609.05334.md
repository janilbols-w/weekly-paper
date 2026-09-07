---
title: "Lightweight Vision Transformer Compression for On-Device Plant Disease Detection in Resource-Constrained Agricultural Field Conditions"
description: "Chilli (Capsicum annuum) is one of India's most economically significant crops, yet its productivity is persistently threatened by diseases that are difficult to identify without expert intervention."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.05334) · [PDF](https://arxiv.org/pdf/2609.05334)

## 一句话摘要

Chilli (Capsicum annuum) is one of India's most economically significant crops, yet its productivity is persistently threatened by diseases that are difficult to identify without expert intervention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Chilli (Capsicum annuum) is one of India's most economically significant crops, yet its productivity is persistently threatened by diseases that are difficult to identify without expert intervention. While Vision Transformers (ViTs) have achieved high classification accuracy, their large computational footprint makes deployment on resource constrained devices challenging. Existing compression approaches typically address pruning, quantization, and knowledge distillation in isolation, leaving the potential benefits and interactions of their combined application insufficiently explored. We propose a unified Vision Transformer compression framework that combines Hessian-Balanced Adaptive Block Pruning (H-BAC), guided by second-order sensitivity estimation, with quantization and attention-based knowledge distillation. To systematically identify the most effective configuration within each compression family, each technique is first evaluated independently through controlled ablation studies, after which the best-performing components are integrated into a sequential deployment pipeline tailored to real-world agricultural constraints. On a chilli 3-class village-split dataset with a genuine cross-village, cross-device out-of-distribution test split, the resulting compressed models match or exceed the 95.13% FP32 baseline's accuracy, alongside 74-98% model size reduction, and the fully integrated compression pipeline achieves a 54.5x size reduction (327.42 MB to 6.01 MB) at 95.13 +/- 2.32% accuracy across four tested configurations. A direct comparison further reveals that, on this dataset, a directly-trained student of the same final size, without pruning or distillation, reaches comparable accuracy of 94.87%, at the same 6.01 MB INT8 size, indicating where H-BAC and knowledge distillation are, and are not yet shown to be, worth their computational cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mahadev Sunil Kumar, Bhavika Gondi, Desaisetty Venkata Satya Sai Swapnith, Gangireddy Rahul Jogi, Sudheesh Manalil, Arnab Raha, Amitava Mukherjee, Parthasarathy Seethapathy, G. Gopakumar
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
