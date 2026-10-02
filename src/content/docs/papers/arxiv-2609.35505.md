---
title: "An RL View of OPD: Least Square Policy Distillation for Sample-Efficient LLM Reasoning"
description: "We study on-policy distillation (OPD) through the lens of reinforcement learning, establishing a connection between the reverse-KL objective in OPD and KL-regularized policy optimization."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.35505) · [PDF](https://arxiv.org/pdf/2609.35505)

## 一句话摘要

We study on-policy distillation (OPD) through the lens of reinforcement learning, establishing a connection between the reverse-KL objective in OPD and KL-regularized policy optimization.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study on-policy distillation (OPD) through the lens of reinforcement learning, establishing a connection between the reverse-KL objective in OPD and KL-regularized policy optimization. Building on this connection, we introduce Least-Square Policy Distillation (LSPD), an RL-inspired framework that brings optimistic exploration and off-policy data reuse from value-based RL into policy distillation. LSPD preserves policy diversity through exploration while improving rollout efficiency by repeatedly learning from previously collected trajectories. Our theoretical analysis connects LSPD to optimistic value-based learning and shows that its idealized formulation achieves a sharp $\tilde{\mathcal O}(\log K)$ regret bound under online exploration. Empirically, LSPD consistently outperforms existing distillation baselines across six mathematical reasoning benchmarks and diverse teacher-student settings, with average gains of +1.59 points in Avg@16. Remarkably, through Pass@k evaluations up to k=64, we found that LSPD better preserves policy diversity by achieving stronger performance as k grows. Its fully off-policy variant achieves comparable performance to vanilla OPD using only the first 25% of rollout batches. Together, these results provide an RL perspective on OPD that offers both a principled interpretation and a practical route toward more effective and rollout-efficient language model distillation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shangzhe Li, Yuxiao Yang, Tianrun Yu, Kaixiang Zhao, Xiaoyun Wang, Taylor W. Killian, Weitong Zhang
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/UNCSciML/LSPD](https://github.com/UNCSciML/LSPD)
- 阅读深度：metadata
