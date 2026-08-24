---
title: "AIRL-S: Unifying Reinforcement Learning and Search-Based Test-Time Scaling via Adversarial Inverse Reinforcement Learning"
description: "Test-time scaling strategies for Large Language Models predominantly rely on either reinforcement learning with sparse outcome rewards or search-based methods guided by static Process Reward Models."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2508.14313) · [PDF](https://arxiv.org/pdf/2508.14313)

## 一句话摘要

Test-time scaling strategies for Large Language Models predominantly rely on either reinforcement learning with sparse outcome rewards or search-based methods guided by static Process Reward Models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Test-time scaling strategies for Large Language Models predominantly rely on either reinforcement learning with sparse outcome rewards or search-based methods guided by static Process Reward Models. However, outcome-based RL often suffers from training instability and sample inefficiency, while static PRMs require expensive step-wise supervision and are susceptible to reward hacking due to distributional shifts. In this paper, we introduce AIRL-S, a unified framework that integrates Adversarial Inverse Reinforcement Learning with Group Relative Policy Optimization. By inferring a dense, step-wise reward model directly from reference trajectories, AIRL-S eliminates the dependency on labeled process data and uses the same learned PRM as both a training signal and a verifier for search-based TTS. Extensive evaluations across eight benchmarks in mathematics, science, and code generation demonstrate that our policy model improves average performance by 9\% over the base model, matching GPT-4o. We further analyze how the AIRL and GRPO objectives complement each other and how the learned PRM transfers across generators and search algorithms, establishing a robust and cost-effective methodology for scaling test-time computation in complex reasoning tasks.

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

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Can Jin, Yang Zhou, Qixin Zhang, Hongwu Peng, Di Zhang, Zihan Dong, Marco Pavone, Ligong Han, Zhang-Wei Hong, Tong Che, Dimitris N. Metaxas
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
