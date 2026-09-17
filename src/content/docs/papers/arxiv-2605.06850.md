---
title: "How to Compress KV Cache in RL Post-Training? Shadow Mask Distillation for Memory-Efficient Alignment"
description: "Reinforcement Learning (RL) has emerged as a crucial paradigm for unlocking the advanced reasoning capabilities of Large Language Models (LLMs), encompassing frameworks like RLHF and RLAIF."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.06850) · [PDF](https://arxiv.org/pdf/2605.06850)

## 一句话摘要

Reinforcement Learning (RL) has emerged as a crucial paradigm for unlocking the advanced reasoning capabilities of Large Language Models (LLMs), encompassing frameworks like RLHF and RLAIF.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement Learning (RL) has emerged as a crucial paradigm for unlocking the advanced reasoning capabilities of Large Language Models (LLMs), encompassing frameworks like RLHF and RLAIF. Regardless of the specific optimization algorithm (e.g., PPO, GRPO, or Online DPO), online RL inherently requires an exploratory trajectory generation (rollout) phase. However, for long-context reasoning tasks, this rollout phase imposes a severe ``memory wall'' due to the exorbitant Key-Value (KV) cache footprint. While applying KV cache compression during rollouts mitigates this memory overhead, it induces a critical off-policy bias. Although modern KV compression is often nearly lossless during standard inference, even minuscule approximation errors are drastically amplified by the inherent instability of RL optimization. Specifically, the sampler generates responses under a sparse context, whereas the learner updates parameters using the full, dense context. Existing statistical solutions, such as importance reweighting, struggle to correct this magnified bias, suffering from high gradient variance and severe sample inefficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rui Zhu, Weiheng Bai, Qiushi Wu, Yang Ren, Haixu Tang, Yuchu Liu
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
