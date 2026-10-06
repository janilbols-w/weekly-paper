---
title: "Improving Reasoning Ability via Asynchronous On-Policy Self-Distillation under Positive Rollouts"
description: "Distillation and reinforcement learning through verifiable rewards (RLVR) have achieved progress in enhancing the reasoning ability of large language models (LLMs)."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.06650) · [PDF](https://arxiv.org/pdf/2605.06650)

## 一句话摘要

Distillation and reinforcement learning through verifiable rewards (RLVR) have achieved progress in enhancing the reasoning ability of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Distillation and reinforcement learning through verifiable rewards (RLVR) have achieved progress in enhancing the reasoning ability of large language models (LLMs). However, we note that negative rollouts may admit no gradation of failure severity, and the combinatorial vastness makes penalizing a few sampled negatives unlikely to cover a meaningful reward signal under sparse binary rewards. In this work, we propose Positive-Only Policy Optimization (POPO), an on-policy self-distillation integrated RLVR framework in which learning occurs exclusively on online positive rollouts. Specifically, POPO utilizes bounded importance sampling over the positive rollout set. Thus, no disjoint negative rollouts are used for gradient guidance during post-training. We show that implicit negative gradients can emerge naturally through reinforcing the positive probability via rollout redistribution. Next, POPO stabilizes the policy optimization through self-distillation. First, it applies a Siamese policy network with a momentum-based adaptation law for asynchronous policy evolution. Second, we replace the KL-divergence with a bounded similarity penalty term in the Siamese representation space. We conduct extensive experiments using publicly available, well-established text-LLM models across all-level mathematical benchmarks (MATH-500, AMC23, AIME 2024/2025, and Olympiad). Our experiment demonstrates that POPO achieves superior performance compared to GRPO. Notably, we show that POPO can achieve 36.67% in AIME 2025 with Qwen-Math-7B, outperforming GRPO 30.00%. Our ablation and sweep studies further illustrate the necessity and robustness.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mingwei Xu, Hao Fang
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
