---
title: "Reverse-KL Policy Distillation: Statistical Guarantees and Limits"
description: "Reverse Kullback-Leibler (KL) distillation has shown empirical promise for training language models, but its statistical guarantees and limits remain poorly understood."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.30844) · [PDF](https://arxiv.org/pdf/2610.30844)

## 一句话摘要

Reverse Kullback-Leibler (KL) distillation has shown empirical promise for training language models, but its statistical guarantees and limits remain poorly understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reverse Kullback-Leibler (KL) distillation has shown empirical promise for training language models, but its statistical guarantees and limits remain poorly understood. In particular, the effects of two design choices remain unclear: Does access to the teacher's full action distribution provide an advantage over observing only the probability it assigns to the sampled action? Must training trajectories come from the student (online distillation), or can teacher-generated trajectories (offline distillation) suffice? Our work takes a first step toward understanding the theory underlying these questions. We study the sample complexity of online reverse-KL distillation under two feedback models: the teacher reveals either its full action distribution or only the probability of the student-generated action. We establish minimax bounds for the former and show that substantially more data may be required for the latter. In contrast, offline reverse-KL distillation can attain the same minimax rate whether the teacher reveals its full distribution or only its probability of the teacher-generated action. The key distinction is that teacher-generated actions themselves reveal the teacher's preferences, while queries at student-selected actions can leave those preferences unobserved. This highlights an additional statistical challenge for online distillation compared to offline distillation. These statistical guarantees do not follow simply from optimizing standard distillation objectives: our lower bounds show that common online objectives can fail when candidates are evaluated only on past student-generated trajectories. We develop trajectory-loss and importance-ratio truncation techniques together with policy-space learning to achieve optimal online distillation guarantees.

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

- 作者：Haolin Liu, Chen-Yu Wei, Julian Zimmert
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
