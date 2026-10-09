---
title: "Stochastic Teacher Intervention for Agentic On-Policy Distillation"
description: "On-policy distillation (OPD) efficiently transfers capabilities from a stronger teacher to a student language model through dense token-level supervision on student-generated rollouts and has shown promise on complex tasks such as mathematical reasoning."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.10878) · [PDF](https://arxiv.org/pdf/2610.10878)

## 一句话摘要

On-policy distillation (OPD) efficiently transfers capabilities from a stronger teacher to a student language model through dense token-level supervision on student-generated rollouts and has shown promise on complex tasks such as mathematical reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) efficiently transfers capabilities from a stronger teacher to a student language model through dense token-level supervision on student-generated rollouts and has shown promise on complex tasks such as mathematical reasoning. However, in multi-turn agentic tasks, student decisions shape subsequent observations, causing early errors to accumulate across turns. The resulting trajectories can drift away from the teacher's rollout distribution, making the teacher's token-level supervision less reliable or even counterproductive for OPD training. To address this issue, we introduce STI-OPD, a stochastic teacher intervention framework for multi-turn agentic OPD. During multi-turn interaction, STI-OPD uses teacher intervention guided by teacher-student policy discrepancy to replace the student's proposed action with a teacher-generated one to maximize the acquisition of reliable supervision. We further develop a stochastic intervention strategy, addressing the limitations of previous threshold-based or fixed-schedule approaches, that estimates policy discrepancy using KL divergence and maps it to an intervention probability. By sampling whether to intervene from this probability, STI-OPD adaptively balances teacher control with student exploration. To learn from the resulting mixed-policy trajectories, we introduce an Importance-Weighted Reverse KL objective that corrects the token sampling mismatch between teacher-generated responses and the student policy to preserve the original OPD objective. Across tool-integrated reasoning and long-horizon interaction, STI-OPD outperforms the strongest prior OPD baseline on every evaluated benchmark and student size. Ablations further show that both discrepancy-guided intervention and importance weighting contribute to these gains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junnan Liu, Linhao Luo, Zhijun Chen, Qianren Mao, Thuy-Trang Vu, Gholamreza Haffari
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
