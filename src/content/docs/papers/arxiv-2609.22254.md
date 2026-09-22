---
title: "Teacher Should Think Ahead: Adaptive Continuations for Reliable On-Policy Distillation"
description: "On-policy distillation (OPD) is a promising approach for transferring knowledge between language models, where a student receives dense token-level supervision along its own generated trajectories."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.22254) · [PDF](https://arxiv.org/pdf/2609.22254)

## 一句话摘要

On-policy distillation (OPD) is a promising approach for transferring knowledge between language models, where a student receives dense token-level supervision along its own generated trajectories.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) is a promising approach for transferring knowledge between language models, where a student receives dense token-level supervision along its own generated trajectories. However, teacher supervision can be unreliable when conditioned on incomplete or low-quality student prefixes. We identify Teacher Uncertainty Contraction (TUC), a systematic phenomenon whereby the teacher's predictive uncertainty decreases as it continues from a student-generated prefix. We theoretically characterize this trade-off through a variance-bias decomposition of teacher-branch gradients, showing that uncertainty contraction reduces variance while teacher-student path divergence increases bias, thereby favoring a finite continuation. Guided by this insight, we propose Adaptive-Continuations On-Policy Distillation (AC-OPD), which augments informative states along student rollouts with teacher continuations and adaptively selects their effective supervision horizons. Experiments on mathematical reasoning and code generation across model scales demonstrate that AC-OPD consistently improves over standard OPD. Controlled-continuations and matched-budget analyses further validate the adaptive-continuations design, highlighting adaptive teacher continuations as an effective principle for reliable on-policy distillation.The code will be made publicly available upon publication.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jingang Zhou, Yuyi Zhou, Haiyang Guo, Xukai Wang, Shuai Feng, Sirui Gao, Jian Xu, Qingpei Guo, Xu-Yao Zhang
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
