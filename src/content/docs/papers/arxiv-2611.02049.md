---
title: "Reinforcement Learning in High-Energy Physics: A Survey from Accelerator Control to Theory Exploration"
description: "Reinforcement learning (RL) is a machine learning paradigm in which an agent learns a decision-making policy by interacting with an environment, guided by a scalar reward rather than explicit supervision."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.02049) · [PDF](https://arxiv.org/pdf/2611.02049)

## 一句话摘要

Reinforcement learning (RL) is a machine learning paradigm in which an agent learns a decision-making policy by interacting with an environment, guided by a scalar reward rather than explicit supervision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) is a machine learning paradigm in which an agent learns a decision-making policy by interacting with an environment, guided by a scalar reward rather than explicit supervision. Supervised and unsupervised learning have become indispensable tools in high-energy physics (HEP), but they learn from fixed datasets, whereas many HEP tasks are closed-loop decisions: the data an algorithm observes depend on its choices, the feedback is sparse or delayed, and the objective is often measured on a real machine or in a stochastic simulation, not by a differentiable model. This survey reviews the application of RL to such tasks: accelerator control and feedback, data quality monitoring, jet grooming, clustering, and representation, charged particle tracking, beyond-the-Standard-Model (BSM) and string model building, detector design, trigger control, analysis, and formal quantum field theory computation. It provides a self-contained introduction to the underlying RL methods, from model-free and model-based to multi-agent, offline, inverse, and bandit approaches, reviews each domain against its traditional methods, and summarizes the head-to-head comparisons. The applications range from policies deployed on real accelerators and evaluated on recorded collision data to exploratory studies in formal theory. RL is most advantageous for repeated tasks with a fast simulator, decisions inside fast control loops, operation under faults and corrupted measurements, physics-based rewards in place of labels, and sequential discrete constructions with a reusable policy, while Bayesian optimization, genetic algorithms, and differentiable methods remain competitive elsewhere. We conclude with the open challenges that recur across domains, including reward design, sim-to-real transfer, safety, the lack of shared benchmarks, and the statistical validity of policy-driven decisions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Luca Anzalone
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
