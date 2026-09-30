---
title: "P^2O: Joint Policy and Prompt Optimization"
description: "Reinforcement Learning with Verifiable Rewards (RLVR) enhances Large Language Model (LLM) reasoning but is suffer from advantage collapse: when all rollouts of a query receive identical rewards, the group variance vanishes, most damagingly on hard samples, where scaling rollout budgets yields little."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.21877) · [PDF](https://arxiv.org/pdf/2603.21877)

## 一句话摘要

Reinforcement Learning with Verifiable Rewards (RLVR) enhances Large Language Model (LLM) reasoning but is suffer from advantage collapse: when all rollouts of a query receive identical rewards, the group variance vanishes, most damagingly on hard samples, where scaling rollout budgets yields little.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement Learning with Verifiable Rewards (RLVR) enhances Large Language Model (LLM) reasoning but is suffer from advantage collapse: when all rollouts of a query receive identical rewards, the group variance vanishes, most damagingly on hard samples, where scaling rollout budgets yields little. We introduce Joint Policy and Prompt Optimization (P O) to mitigate this collapse by alternating continuous policy updates with discrete prompt evolution. P O mines hard samples with a success-rate threshold, evolves reasoning prompts for them with GEPA, and internalizes the elicited trajectories via context distillation, which optimizes each trajectory under the original query and thus removes inference-time prompting, with a Context Ratio Mask (CRM) filtering out extreme likelihood ratios. P O restores critical advantage signals and surpasses the GRPO baseline by up to 8.2 points in average accuracy on six held-out benchmarks across all training datasets and backbones, while also outperforming DAPO and other baselines. The gains are especially pronounced on hard benchmarks, reaching up to 16.3 points above GRPO on average across AIME24 and AIME25. Our findings expose the limits of standard exploration in sparse-reward environments, illuminating the potential of unifying evolutionary algorithms with reinforcement learning. This integration of discrete semantic search and continuous parameter updates provides a self-reinforcing framework that facilitates more effective LLM alignment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xinyu Lu, Kaiqi Zhang, Jinglin Yang, Boxi Cao, Yaojie Lu, Hongyu Lin, Min He, Xianpei Han, Le Sun
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
