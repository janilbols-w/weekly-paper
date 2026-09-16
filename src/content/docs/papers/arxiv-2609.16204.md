---
title: "Decoy Direction Optimization: A Post-Hoc Defense Against LLM Abliteration"
description: "Safety guardrails in open-weight language models can be readily bypassed using Refusal Feature Ablation (RFA), a technique that identifies and projects out a linear refusal direction from the residual stream, often achieving a high attack success rate (ASR) while preserving model capability."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.16204) · [PDF](https://arxiv.org/pdf/2609.16204)

## 一句话摘要

Safety guardrails in open-weight language models can be readily bypassed using Refusal Feature Ablation (RFA), a technique that identifies and projects out a linear refusal direction from the residual stream, often achieving a high attack success rate (ASR) while preserving model capability.

## 为什么值得关注

待编辑增强。

## 摘要原文

Safety guardrails in open-weight language models can be readily bypassed using Refusal Feature Ablation (RFA), a technique that identifies and projects out a linear refusal direction from the residual stream, often achieving a high attack success rate (ASR) while preserving model capability. Defending against these attacks typically requires computationally expensive safety finetuning for every new checkpoint. We introduce Decoy Direction Optimization (DDO), a fast, post-hoc weight-editing defense that requires no base-model finetuning. Our approach is based on a simple mechanistic insight: ablation attacks rely on contrastive estimators to find the refusal direction. Rather than trying to hide the true refusal circuitry, DDO actively injects a high-magnitude, nonlinear decoy signal into the network's MLP neurons. When an attacker attempts to locate the refusal direction, the decoy corrupts their estimator, tricking them into ablating a harmless orthogonal feature while the actual safety mechanism remains intact. We prove a spectral bound formalizing this effect and evaluate DDO across six model families, achieving <10% ASR under standard RFA. On Llama-3-8B-Instruct, DDO remains comparable to trained defenses under adaptive multi-phase attacks (65% vs. 58% worst-case ASR) and reduces Heretic weight-level attack ASR from 88.7% to 18%, all at 30 to 450 times lower optimization cost per configuration than the trained baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aashiq Muhamed, Mona T. Diab, Virginia Smith
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
