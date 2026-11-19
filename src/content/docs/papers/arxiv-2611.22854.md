---
title: "WATERFALL: Workflow for Adaptive Training with Evolutionary Reward Formulation and Automated Learning Loops"
description: "Reward design remains a central bottleneck in reinforcement learning (RL), particularly in sparse-reward, long-horizon and partially observable settings requiring dependency chaining, memory, and deceptive affordance disambiguation."
---

**评分：42/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2611.22854) · [PDF](https://arxiv.org/pdf/2611.22854)

## 一句话摘要

Reward design remains a central bottleneck in reinforcement learning (RL), particularly in sparse-reward, long-horizon and partially observable settings requiring dependency chaining, memory, and deceptive affordance disambiguation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reward design remains a central bottleneck in reinforcement learning (RL), particularly in sparse-reward, long-horizon and partially observable settings requiring dependency chaining, memory, and deceptive affordance disambiguation. While recent foundation-model approaches reduce manual reward engineering, most assume goal-conditioning, task descriptions, expert demonstrations, or ground-truth metrics. These assumptions are problematic in partially observable environments, where task-relevant objectives, affordances, and dynamics must be discovered through interaction rather than disclosed a priori. We formalise this problem setting by introducing WATERFALL, an iterative population-based workflow for automated reward discovery under the strict observability constraints inherent in POMDP environments. WATERFALL achieves this by (i) synthesising diverse programmatic reward candidates via persona-conditioned generation, (ii) evaluating candidate behaviour from raw visual rollouts utilising a Swiss-system evolutionary tournament judged by vision-language models to identify elites, and (iii) leveraging longitudinal assessment histories to iteratively mutate, escalate, or prune candidates. We evaluate WATERFALL across fully observable and reveal-gated partially observable environments ranging from discrete to continuous, comparing against sparse-reward RL, intrinsic-motivation and foundation-model reward-synthesis baselines. Our results indicate that WATERFALL discovers and refines reward programs without access to privileged information, outperforming baselines that retain their native information advantages, most clearly in the POMDP regime. Extensive ablations substantiate that visual evidence, tournament-based selection, and iterative refinement are jointly important. Enforcing this contract is what separates autonomous reward discovery from benchmark-privileged reward shaping.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Eleftherios Triantafyllidis, Filippos Christianos, Zhibin Li, Bernd Bickel
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
