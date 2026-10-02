---
title: "The Weakest Link: Distilling LLM Reasoning with Worst-Case Constrained Reinforcement Learning"
description: "Distilling the reasoning capabilities of large language models (LLMs) into smaller students is a central challenge for efficient deployment."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.00332) · [PDF](https://arxiv.org/pdf/2610.00332)

## 一句话摘要

Distilling the reasoning capabilities of large language models (LLMs) into smaller students is a central challenge for efficient deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distilling the reasoning capabilities of large language models (LLMs) into smaller students is a central challenge for efficient deployment. Current approaches face a fundamental tension: optimizing purely for verifiable task rewards (e.g., via GRPO) leads to reward hacking, where students arrive at correct final answers through flawed intermediate logic, while regularizing with soft divergence penalties against a teacher (e.g., KL-based distillation) dilutes task performance and, critically, allows the student to compensate for severe logical violations at one step with high teacher agreement at others. We argue that this averaging is fundamentally misaligned with the nature of reasoning: a chain-of-thought is only as valid as its weakest link. Motivated by this observation, we formulate reasoning distillation as a constrained reinforcement learning problem in which the task reward is maximized subject to a worst-case constraint on the teacher log-likelihood along every prefix of the trajectory. To avoid the prohibitive cost of dual Lagrangian solvers and the test-time teacher dependence of state-augmented methods such as Saute, we derive an unaugmented constrained MDP whose reward transformation preserves the hard-constraint semantics, admits a low-variance policy gradient decomposition into single-step and long-term terms, and provably satisfies the worst-case constraint almost surely in the penalty limit. Through extensive experiments on mathematical reasoning and code generation tasks, we demonstrate that our method significantly expands the accuracy-fidelity Pareto front. By matching the high Final Answer Correctness of pure RL and drastically reducing teacher constraint violations, we ultimately achieve the highest rigorous Reasoning Success Rate across all evaluated settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Matthieu Zimmer, Xiaotong Ji, Tu Nguyen, Haitham Bou-Ammar
- 发布：2026-09-29；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
