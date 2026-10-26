---
title: "Heterogeneous Agent Collaborative Reinforcement Learning"
description: "We introduce Heterogeneous Agent Collaborative Reinforcement Learning (HACRL), a new Reinforcement Learning from Verifiable Reward (RLVR) problem that addresses the inefficiencies of isolated multi-agent on-policy optimization."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.02604) · [PDF](https://arxiv.org/pdf/2603.02604)

## 一句话摘要

We introduce Heterogeneous Agent Collaborative Reinforcement Learning (HACRL), a new Reinforcement Learning from Verifiable Reward (RLVR) problem that addresses the inefficiencies of isolated multi-agent on-policy optimization.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce Heterogeneous Agent Collaborative Reinforcement Learning (HACRL), a new Reinforcement Learning from Verifiable Reward (RLVR) problem that addresses the inefficiencies of isolated multi-agent on-policy optimization. HACRL enables collaborative optimization with independent execution: heterogeneous agents share verified rollouts during training to mutually improve, while operating independently at inference time. Unlike LLM-based multi-agent reinforcement learning (MARL), HACRL does not require coordinated deployment, and unlike on-/off-policy distillation, it enables bidirectional mutual learning among heterogeneous agents rather than one-directional homogeneous teacher-to-student transfer. Building on this problem, we propose HACPO, a collaborative RL algorithm that enables principled rollout sharing to maximize sample utilization and cross-agent knowledge transfer. To mitigate capability discrepancies and policy distribution shifts, HACPO introduces four tailored mechanisms with theoretical guarantees on unbiased advantage estimation. Extensive experiments across diverse heterogeneous model combinations and reasoning benchmarks show that HACPO consistently improves all participating agents, outperforming GSPO with double rollouts by an average of 3.6% while using only half the rollout cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhixia Zhang, Zixuan Huang, Gongxun Li, Huaiyang Wang, Chengyi Yuan, Xin Xia, Deqing Wang, Fuzhen Zhuang, Shuai Ma, Ning Ding, Yaodong Yang, Jianxin Li, Yikun Ban
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
