---
title: "ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning via Outcome Reward Densifying"
description: "Reinforcement learning (RL) has become one of the primary paradigms for reasoning enhancement of large language models (LLMs)."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.04648) · [PDF](https://arxiv.org/pdf/2609.04648)

## 一句话摘要

Reinforcement learning (RL) has become one of the primary paradigms for reasoning enhancement of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) has become one of the primary paradigms for reasoning enhancement of large language models (LLMs). In particular, Group Relative Policy Optimization (GRPO) and related algorithms have demonstrated strong performance with outcome-level rewards. However, these methods depend solely on the final answer, without feedback regarding which intermediate steps contribute to success or failure. As task complexity and reasoning trajectory length increase, such sparse final-answer rewards become increasingly insufficient. To address this limitation, we introduce ConsensusBench, a novel dataset designed to provide rule-based process-level signals. We posit that a correct final answer relies on a small set of intermediate conclusions throughout the reasoning process, which can be seen as a verifiable sub-outcome. We identify these sub-outcomes by filtering correct trajectories from N rollouts and clustering semantically equivalent intermediate statements. We call these clustered statements as Consensus Nodes. By integrating a rule-based process reward derived from these nodes into GRPO-style algorithms, we develop a new reinforcement learning signal named ConsensusPR. It directly reduces the reward sparsity of outcome reward across long reasoning trajectories. To facilitate systematic process-level evaluation, we introduce three metrics to our benchmark: Final Answer Accuracy (Acc), Node Coverage Rate (NCR), and Tokens per Node (TPN). Experiments across AIME 2024, AIME 2025, GSM8K, MATH-500, and our ConsensusBench demonstrate that the proposed method consistently surpasses GRPO-style approaches, highlighting the practical value of consensus nodes in guiding reasoning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shi-Qi Yan, Chao-Hong Tan, Qian Chen, Wen Wang, Xiangang Li, Zhen-Hua Ling
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
