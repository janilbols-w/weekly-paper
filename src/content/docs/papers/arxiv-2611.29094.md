---
title: "HME-PFD: Heterogeneous Mixture-of-Experts Privileged Feature Distillation"
description: "Knowledge distillation (KD) is widely used to transfer knowledge from large teacher models to smaller student models, facilitating efficient serving of machine learning systems."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.29094) · [PDF](https://arxiv.org/pdf/2611.29094)

## 一句话摘要

Knowledge distillation (KD) is widely used to transfer knowledge from large teacher models to smaller student models, facilitating efficient serving of machine learning systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation (KD) is widely used to transfer knowledge from large teacher models to smaller student models, facilitating efficient serving of machine learning systems. In the context of ads recommendation, privileged features distillation (PFD) extends KD by allowing the teacher model to leverage privileged features, i.e., features available only during training, to enhance distillation performance. However, in real-world scenarios, privileged features often have limited coverage and exhibit heterogeneous distributions, resulting in training examples of varying importance for distillation and model learning. We propose Heterogeneous Mixture-of-Experts Privileged Feature Distillation (HME-PFD), a novel approach that incorporates privileged features into the routing module of a Mixture-of-Experts-based student model. Our method introduces both hard-coded and learnable routing modules, enabling the student to dynamically determine expert assignment based on the availability and values of privileged features. This design allows the student model to better handle the heterogeneous data scenario, where privileged features are partially observed, by differentiating between high- and low-signal samples. Extensive experiments on two post-click conversion prediction tasks demonstrate that HME-PFD consistently outperforms baseline methods. Our results show that leveraging privileged features for expert routing in the student model leads to improved model performance, even when privileged features are incomplete or sparse.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wen Xu, Xiaomin Zhang, Yucheng Yang, Danny Liu, Xunlong Gui, Fei Huang, Sha Meng
- 发布：2026-11-21；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
