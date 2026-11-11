---
title: "Teacher-Guided Policy Optimization for On-Policy Reasoning Distillation under Large Policy Divergence"
description: "On-policy distillation (OPD) has become a promising paradigm for reasoning-oriented post-training of large language models (LLMs), especially when combined with reinforcement learning from verifiable rewards (RLVR)."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.13230) · [PDF](https://arxiv.org/pdf/2605.13230)

## 一句话摘要

On-policy distillation (OPD) has become a promising paradigm for reasoning-oriented post-training of large language models (LLMs), especially when combined with reinforcement learning from verifiable rewards (RLVR).

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) has become a promising paradigm for reasoning-oriented post-training of large language models (LLMs), especially when combined with reinforcement learning from verifiable rewards (RLVR). Existing OPD methods rely on reverse KL (RKL)-based teacher supervision over trajectories sampled from the student policy. However, we identify a critical limitation: under large teacher--student policy divergence, RL-driven exploration often produces trajectories outside the teacher distribution, resulting in uninformative negative feedback. To address this, we propose Teacher-Guided Policy Optimization (TGPO), an on-policy reasoning distillation method that remains effective under large policy divergence settings. Rather than relying solely on evaluative supervision, TGPO uses teacher to directly guide token level generation conditioning on student-generated contexts; together with RLVR-style trajectory level rewards, TGPO steers exploration toward improved continuations. Experiments on reasoning benchmarks show that TGPO consistently outperforms existing RKL-based OPD methods and remains robust across different teacher models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xinyu Liu, Kechen Jiao, Chunyang Xiao, Runsong Zhao, Junhao Ruan, Bei Li, Jiahao Liu, Qifan Wang, Xin Chen, Jingang Wang, Chenglong Wang, Tong Xiao, JingBo Zhu
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
