---
title: "From Trajectories to Prefixes: Reusing Teacher Trajectories via Replayed Prefixes and Online Continuation"
description: "Small language models are attractive backbones for interactive agents, but direct distillation from strong teacher trajectories often turns rich multi-turn behavior into one-shot imitation targets."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.19395) · [PDF](https://arxiv.org/pdf/2607.19395)

## 一句话摘要

Small language models are attractive backbones for interactive agents, but direct distillation from strong teacher trajectories often turns rich multi-turn behavior into one-shot imitation targets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Small language models are attractive backbones for interactive agents, but direct distillation from strong teacher trajectories often turns rich multi-turn behavior into one-shot imitation targets. This is inefficient in long-horizon environments, where early decisions shape later states and rewards. We propose Prefix-GRPO, a reinforcement learning framework that decomposes teacher trajectories into replay-aligned prefix queries and online continuations. Each prefix is replayed in the environment to recover a valid intermediate state, after which the student continues online interaction and receives task reward. Unlike response-only GRPO, Prefix-GRPO also applies clipped policy updates to historical assistant tokens inside the replayed prefix, using a policy-distilled SFT checkpoint to estimate their old log-probabilities. This unifies prefix learning and continuation learning within the same policy-optimization form. Experiments on TextCraft, BabyAI, and ALFWorld show that Prefix-GRPO improves small-model agents over distillation and standard RL baselines, while ablations show that replay alone is insufficient without explicit prefix-token optimization. The implementation and reproduction scripts are available at https://github.com/HappynessI/Prefix_GRPO.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yihan Wang, Zhong Guan, Haoran Sun, Jiale Huang, Likang Wu, Hongke Zhao
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/HappynessI/Prefix_GRPO](https://github.com/HappynessI/Prefix_GRPO)
- 阅读深度：metadata
