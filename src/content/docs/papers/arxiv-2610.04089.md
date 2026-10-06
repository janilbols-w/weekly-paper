---
title: "Pareto-Dominant Clarification: Post-Training Coding LLMs via PPO-Lagrangian Budget Constraints"
description: "Coding agents operating under ambiguous instructions or user prompts must decide whether to ask clarifying questions or attempt a solution directly."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.04089) · [PDF](https://arxiv.org/pdf/2610.04089)

## 一句话摘要

Coding agents operating under ambiguous instructions or user prompts must decide whether to ask clarifying questions or attempt a solution directly.

## 为什么值得关注

待编辑增强。

## 摘要原文

Coding agents operating under ambiguous instructions or user prompts must decide whether to ask clarifying questions or attempt a solution directly. While clarification from the user may improve the correctness of the agent's solution, each back-and-forth interaction incurs user and system costs, forming an explicit accuracy vs. efficiency tradeoff. Existing works study clarification behavior but do not train policies under enforceable clarification budgets; penalty-based approaches typically require separate coefficient tuning swept across all clarification budget levels. We formulate clarification as a Constrained Markov Decision Process (CMDP) and post-train Qwen2.5-Coder-7B-Instruct with PPO-Lagrangian to optimize coding accuracy, subject to an expected question-budget constraint. Evaluated on HumanEvalComm with a GPT-4o-mini oracle simulator, the resulting policies reveal that untuned clarification behavior is Pareto-inefficient: budget-constrained policies can simultaneously achieve higher accuracy and lower clarification rates than the baseline model. Across budget levels, we observe a log-shaped Pareto frontier with diminishing returns to additional clarification. Gains arise not from simply asking more questions overall, but from improved question targeting and better code generation under ambiguity. Without explicit supervision, trained policies learn to allocate clarification budget non-uniformly, asking more frequently on tougher (multi-degradation) tasks. These results suggest that unconstrained interactive LLM systems may systematically use clarification inefficiently.

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

- 作者：Abhinav Rajput, Acey Vogelstein
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
