---
title: "POETS: Uncertainty-Aware LLM Optimization via Compute-Efficient Policy Ensembles"
description: "Balancing exploration with exploitation is a core challenge in black-box optimization and reinforcement learning."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2605.07775) · [PDF](https://arxiv.org/pdf/2605.07775)

## 一句话摘要

Balancing exploration with exploitation is a core challenge in black-box optimization and reinforcement learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Balancing exploration with exploitation is a core challenge in black-box optimization and reinforcement learning. We introduce POETS ($\textbf{Po}$licy $\textbf{E}$nsembles for $\textbf{T}$hompson $\textbf{S}$ampling), a novel framework that bridges uncertainty quantification and policy optimization. Our approach is grounded in the insight that policies trained with Kullback-Leibler (KL) regularization implicitly encode an underlying reward function. Building on this, POETS bypasses the complex, nested process of training an uncertainty-aware reward model and separately fitting a policy to this model. Instead, we directly train a policy ensemble to capture epistemic uncertainty by matching implicitly encoded reward functions to online, bootstrapped data. To overcome the prohibitive compute and memory constraints of ensembling Large Language Models (LLMs), POETS utilizes an efficient architecture: the ensemble shares a pre-trained backbone while maintaining diversity through independent Low-Rank Adaptation (LoRA) branches. Theoretically, we show that POETS implicitly approximates KL-regularized Thompson sampling, a principled optimization strategy with optimal cumulative regret bounds of $O(\sqrt{T \gamma_T})$. Empirically, we demonstrate that POETS achieves state-of-the-art sample efficiency across diverse scientific discovery domains, including protein search, therapeutic molecular design, and quantum circuit design. POETS also improves the optimization trajectory and out-of-distribution transfer of reinforcement learning across mathematical reasoning and code generation tasks, proving particularly robust in off-policy settings with experience replay or in small dataset regimes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nicolas Menet, Andreas Krause, Abbas Rahimi
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
