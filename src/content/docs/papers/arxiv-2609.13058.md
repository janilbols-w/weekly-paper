---
title: "Expert-Space Exploration in MoE Reinforcement Learning"
description: "Reinforcement learning (RL) has become central to post-training of large language models."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2609.13058) · [PDF](https://arxiv.org/pdf/2609.13058)

## 一句话摘要

Reinforcement learning (RL) has become central to post-training of large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) has become central to post-training of large language models. Recent advances in RL for Mixture-of-Experts (MoE) models have primarily focused on improving optimization stability and training efficiency, while treating the expert selection as a fixed component. Since routing determines the sparse computation paths that induce output distributions, expert selection offers an additional source of rollout diversity. Through empirical analysis, we find that perturbing expert routing effectively alters model output and increases rollout diversity, which is similar to increasing the decoding temperature. However, direct perturbation can activate unsuitable experts and substantially degrade rollout quality. Motivated by these observations, we introduce Expert-Space Exploration Reinforcement Learning (ESRL), an architecture-aware framework that explicitly explores the expert-routing space of MoE models. ESRL preserves high-confidence experts as anchors, and restricts stochastic routing to a plausible candidate pool, thereby retaining reliable computation paths. The perturbation strength is further adapted according to router entropy to avoid over-perturbation. To mitigate the routing mismatch introduced by perturbation, ESRL records the expert paths used during rollout and replays them during policy optimization. Experiments demonstrate that ESRL achieves the best performance across MoE backbones with top-K, top-1, and shared-expert routing, as well as across mathematics, science, and code tasks without additional sampling or computational cost. Specifically, ESRL on Qwen3-30B-A3B achieves the best among all compared methods, improving average Pass@1 and Pass@8 over GRPO by 3.2 and 4.5 percentage points, respectively. Further analyses of expert utilization and training dynamics provide insights into how exploiting MoE-specific routing structure benefits RL training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongyi He, Zhenghao Lin, Xiao Liu, Peng Cheng, Yan Lu, Yeyun Gong
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
