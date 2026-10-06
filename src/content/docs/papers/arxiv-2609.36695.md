---
title: "Know Thyself, Teach Thyself: Internal Information Flow for Selective Self-Distillation"
description: "Self-distillation turns knowledge distillation into a closed learning loop and offers a path toward recursive self-improvement."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.36695) · [PDF](https://arxiv.org/pdf/2609.36695)

## 一句话摘要

Self-distillation turns knowledge distillation into a closed learning loop and offers a path toward recursive self-improvement.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-distillation turns knowledge distillation into a closed learning loop and offers a path toward recursive self-improvement. Without an external teacher, however, the model must determine both what information can improve its supervision and which induced changes should be learned. Existing methods typically improve teacher-generated data or select training examples in isolation, leaving the information transferred between these stages unmeasured. We introduce InFlow, a retrieval-guided on-policy self-distillation framework that models this process as potential-to-realized information flow. InFlow first retrieves potentially informative sources using certainty-calibrated hidden-state trajectories, then measures their realized effect through the Jensen--Shannon divergence between the teacher's initial and retrieval-conditioned answer beliefs. Examples with larger belief shifts are selected for on-policy distillation. Our analysis formalizes the information optimized by retrieval and selection and relates the answer-level shift to the teacher--student distillation gap. Across four open-weight language models and three knowledge domains, InFlow achieves the strongest cross-model average among the compared selection methods, with ablations supporting both stages of the framework. Our code is available at https://github.com/1240148048/INFLOW.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Rui Wang, Ruijie Wang, Bo Chen, Jiangxuan Long, Yingyu Liang
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/1240148048/INFLOW](https://github.com/1240148048/INFLOW)
- 阅读深度：metadata
