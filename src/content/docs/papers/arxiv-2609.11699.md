---
title: "Negative Self-Distillation: Learning to Reason by Avoiding Flaws"
description: "On-Policy Self-Distillation (OPSD) has emerged as a popular paradigm for large language model (LLM) self-improvement, allowing models to act as their own teachers by leveraging privileged information such as ground-truth solutions."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.11699) · [PDF](https://arxiv.org/pdf/2609.11699)

## 一句话摘要

On-Policy Self-Distillation (OPSD) has emerged as a popular paradigm for large language model (LLM) self-improvement, allowing models to act as their own teachers by leveraging privileged information such as ground-truth solutions.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-Policy Self-Distillation (OPSD) has emerged as a popular paradigm for large language model (LLM) self-improvement, allowing models to act as their own teachers by leveraging privileged information such as ground-truth solutions. However, recent findings indicate that OPSD can severely degrade the performance of LLMs on complex reasoning tasks: By forcing the student to imitate an artificially confident reasoning trace conditioned on privileged information, OPSD inadvertently suppresses expressions of uncertainty and penalizes the exploratory, self-corrective behaviors required to solve challenging problems. To address this, we introduce Negative Self-Distillation (NSD), a new framework that optimizes LLMs by diverging from flawed reasoning rather than imitating privileged solutions. Instead of relying on ground-truth answers or external supervision, NSD uses the model itself to generate a question-specific negative condition (eg, acting as a ``careless reasoner'') and pushes the student's distribution away from this self-generated negative teacher. Naively applying unlearning objectives to achieve this divergence is problematic, as flawed reasoning tokens are confounded with basic linguistic tokens; indiscriminately penalizing both risks catastrophically degrading the model's foundational language capabilities. We resolve this by designing a dynamic gating mechanism that automatically identifies and isolates reasoning-critical tokens, ensuring gradient updates target only behavioral flaws while preserving the model's linguistic priors. Empirically, NSD consistently outperforms OPSD and other label-free, self-bootstrapping reinforcement learning (RL) baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rongcan Pei, Zhepei Wei, Shuyao Xu, Xinyu Zhu, Wei-Lin Chen, Yu Meng
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
