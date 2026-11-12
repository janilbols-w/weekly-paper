---
title: "Bootstrapped On-Policy Distillation"
description: "On-policy distillation (OPD) improves language models by distilling teacher predictions on student-generated trajectories, while on-policy self-distillation (OPSD) removes the need for an external teacher by using a reference-conditioned copy of the model as the teacher."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.13680) · [PDF](https://arxiv.org/pdf/2611.13680)

## 一句话摘要

On-policy distillation (OPD) improves language models by distilling teacher predictions on student-generated trajectories, while on-policy self-distillation (OPSD) removes the need for an external teacher by using a reference-conditioned copy of the model as the teacher.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) improves language models by distilling teacher predictions on student-generated trajectories, while on-policy self-distillation (OPSD) removes the need for an external teacher by using a reference-conditioned copy of the model as the teacher. Despite its great early improvements, we find that OPSD does not remain consistently effective under continued training and can eventually suffer substantial performance degradation. We study this training behavior and link the degradation to a growing mismatch between the evolving reference-free student and the frozen privileged teacher. In the early stage of OPSD, the privileged teacher remains closely aligned with the student and provides useful guidance for improving the student's generation trajectories. However, as training progresses, the growing distributional mismatch between the privileged teacher and reference-free student can cause the teacher to provide misleading supervision, ultimately degrading student performance. This phenomenon motivates us to first leverage privileged reference supervision to acquire useful knowledge and then transfer it to a fresh student. We introduce Bootstrapped On-Policy Distillation (BOPD), a two-stage framework that first uses OPSD to internalize task-relevant information from reference-conditioned supervision into an intermediate model, and then distills this reference-free intermediate model into a fresh copy of the initial model. Experiments across models show that BOPD improves mathematical reasoning and code generation beyond both the initial models and the constructed OPSD teachers. These results suggest that privileged reference supervision can be more effectively exploited by first transferring its task-relevant signal into a task-adapted model and then distilling from that model without reference conditioning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yue Wu, Xueyu Zhou, Yangrong Hu, Jian Huang
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
