---
title: "SIPO: Unifying Reinforcement Learning with On-Policy Self-Distillation"
description: "Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for improving large language models (LLMs) on various tasks, yet its sparse outcome rewards lack token-level credit assignment for intermediate steps."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.36742) · [PDF](https://arxiv.org/pdf/2609.36742)

## 一句话摘要

Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for improving large language models (LLMs) on various tasks, yet its sparse outcome rewards lack token-level credit assignment for intermediate steps.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for improving large language models (LLMs) on various tasks, yet its sparse outcome rewards lack token-level credit assignment for intermediate steps. To address this, on-policy self-distillation (OPSD) leverages a self-teacher with privileged context to provide additional dense learning signals. However, because the self-teacher is often overconfident and imposes excessive penalties on long reasoning trajectories, OPSD frequently struggles in practice. To mitigate this, we propose self-instructing policy optimization (SIPO) with a contrastive self-teacher to provide dense credit. At each iteration, SIPO samples multiple rollouts per prompt from the current policy, scores them with environment rewards, and constructs two teacher contexts for each rollout by pairing the reference answer with mistakes made within the group. The model then re-evaluates its own responses under both contexts, using the difference between the two teacher log-probabilities as token-level feedback, so that biases shared by both contexts are expected to largely cancel. The resulting objective yields a token-level advantage for every rollout: the reward still sets the main direction of each update while the self-teacher redistributes credit across tokens. Even in groups where every rollout fails and group-relative advantages vanish, SIPO still provides a learning signal. By preserving direct optimization of the task reward while providing dense, token-level feedback, this approach bridges reinforcement learning and on-policy self-distillation. Extensive experiments across multiple reasoning and code-generation benchmarks demonstrate that SIPO outperforms both RLVR and OPSD baselines without an external teacher or additional generation.

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

- 作者：Zhenrui Yue, Huimin Zeng, Yueqi Wang, Yaokun Liu, Fengran Mo, Jinghan Zhang, Mung Yao Jia, Gyuseok Lee, Yang Zhang, Na Wei, Dong Wang
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
