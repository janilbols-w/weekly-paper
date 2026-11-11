---
title: "Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards Beat Outcome Rewards"
description: "Reinforcement learning with verifiable rewards is increasingly used to improve language model reasoning, yet its effects on sequential decision procedures remain poorly understood."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.12728) · [PDF](https://arxiv.org/pdf/2611.12728)

## 一句话摘要

Reinforcement learning with verifiable rewards is increasingly used to improve language model reasoning, yet its effects on sequential decision procedures remain poorly understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning with verifiable rewards is increasingly used to improve language model reasoning, yet its effects on sequential decision procedures remain poorly understood. We study this problem in clinical multi-turn agents that must decide what information to request, when to stop gathering evidence, and which action to take. We introduce three controlled environments: medication refill triage, acute diagnostic work-up, and dosing titration, each with hidden clinical states, query costs, exact adaptive oracles, and deterministic outcome verifiers. Across these tasks, outcome-only group relative policy optimization often improves aggregate reward while producing undesirable procedures, including premature commitment, one-question collapse, and failures on rare high-risk cases. In diagnostics, assigning dense credit to questions that reduce uncertainty improves held-out value and moderate-case support across three training seeds relative to outcome-only reinforcement learning, without the high-risk seed collapse observed under outcome-only training. Separating exploration from exploitation further increases high-risk support at its best checkpoint, but at the cost of excessive information gathering on low-acuity cases. Additional experiments show that the optimal strength of process credit is task-dependent; that after a supervised warmup that already gathers carefully, reinforcement learning raises aggregate reward by trimming questions while degrading high-risk performance; and that reinforcement learning does not reliably repair rare behavior gaps inherited from biased supervised data. Verifiable final outcomes are therefore insufficient for training reliable multi-turn agents: reward design must account for the procedure used to reach an answer, and evaluation must distinguish adaptive information gathering from reward-exploiting shortcuts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Brendan P. Murphy, Agustina Saenz
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
