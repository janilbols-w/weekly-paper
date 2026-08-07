---
title: "LEAP: Lean Environment-Feedback via Adaptive Pruning for Code RL in GPU Kernel Generation"
description: "Post-training large language models (LLMs) via reinforcement learning (RL) has significantly advanced code generation capabilities."
---

**评分：53/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2608.01804) · [PDF](https://arxiv.org/pdf/2608.01804)

## 一句话摘要

Post-training large language models (LLMs) via reinforcement learning (RL) has significantly advanced code generation capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training large language models (LLMs) via reinforcement learning (RL) has significantly advanced code generation capabilities. To bypass the heavy memory footprint of critic networks, current state-of-the-art frameworks leverage critic-free paradigms like Group Relative Policy Optimization (GRPO) tied to rule-based verification sandboxes. However, applying these frameworks to low-level systems programming, such as CUDA kernel generation-presents severe challenges: binary pass/fail rewards introduce severe signal sparsity, while multi-turn environmental feedback loops suffer from prohibitive compilation latencies and reward dilution across trajectories. In this work, we introduce LEAP (Lean Environment-Feedback via Adaptive Pruning), a scalable and computationally efficient multi-turn RL framework optimized for low-level hardware accelerator alignment. LEAP features Difficulty-Conditioned Pruning (DCP), a dynamic gating mechanism that adaptively cuts off simple and overly catastrophic tasks from multi-turn expansion, focusing resource-heavy compilation and hardware exploration exclusively on high-value, complex tasks. To fully operationalize these paths without manual hyperparameter engineering, we propose a Rank-Based Reward formulation. By deriving scale-free relative advantages from pairwise tournament outcomes within the GRPO rollout group, our method inherently penalizes token inefficiency on simple prompts while maximizing learning gradients on challenging distributions. Empirical evaluations show that LEAP achieves superior first-turn proficiency and robust multi-turn debugging resilience while converging faster than unpruned multi-turn baselines, establishing a practical paradigm for low-level code RL.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: cuda kernel, gpu kernel, kernel generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tankun Li, Zhi Chen, Yaohua Tang
- 发布：2026-08-03；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
