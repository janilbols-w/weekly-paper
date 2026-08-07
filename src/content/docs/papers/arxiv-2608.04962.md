---
title: "SpecRoll: Fast-Slow Verifier-Feedback Adaptation for Speculative Reinforcement Learning Rollouts"
description: "Reinforcement learning (RL) post-training improves the reasoning capabilities of large language models, but autoregressive rollout generation remains a major efficiency bottleneck."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.04962) · [PDF](https://arxiv.org/pdf/2608.04962)

## 一句话摘要

Reinforcement learning (RL) post-training improves the reasoning capabilities of large language models, but autoregressive rollout generation remains a major efficiency bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) post-training improves the reasoning capabilities of large language models, but autoregressive rollout generation remains a major efficiency bottleneck. Speculative decoding can accelerate generation, yet applying it during RL is difficult because the target policy continually evolves: static proposers become stale, while frequent drafter updates add substantial overhead. We introduce SpecRoll, a speculative rollout engine that preserves the target model's sampling distribution while adapting at two timescales. Lightweight future-token heads generate parallel proposals, while our proposed Reflex module uses delayed verifier feedback to perform bounded, trajectory-local hidden-state corrections without backpropagation. A complementary slow path updates the head parameters only when sustained degradation is detected. SpecRoll combines these mechanisms with concurrency-aware sparse-tree verification and exact target verification, leaving the target rollout distribution and GRPO objective unchanged. Across five models ranging from 1.5B to 14B and three mathematical reasoning datasets, SpecRoll achieves 1.26-2.15x generation speedup and 1.21-2.04x end-to-end speedup over vanilla GRPO. It also outperforms FastGRPO in both generation and end-to-end time across all 15 matched settings, with an average pairwise end-to-end gain of 1.18x. Controlled ablations show that the fast and slow adaptation paths provide complementary benefits. Our source code is available at https://anonymous.4open.science/r/SpecRoll-26062006.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Nhat Minh Pham, Duy Tung Doan, Thi Duyen Ngo, Vinh Van Nguyen, Khac-Hoai Nam Bui
- 发布：2026-08-05；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
