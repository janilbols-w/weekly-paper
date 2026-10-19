---
title: "A Stronger Teacher Within: Strengthening MoE Models via On-Policy Bidirectional Distillation"
description: "Reinforcement Learning with Verifiable Rewards (RLVR) has substantially improved Mixture-of-Experts (MoE) LLMs, but its outcome-level rewards provide only sparse supervision."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.23185) · [PDF](https://arxiv.org/pdf/2610.23185)

## 一句话摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has substantially improved Mixture-of-Experts (MoE) LLMs, but its outcome-level rewards provide only sparse supervision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement Learning with Verifiable Rewards (RLVR) has substantially improved Mixture-of-Experts (MoE) LLMs, but its outcome-level rewards provide only sparse supervision. On-Policy Distillation offers dense token-level feedback, yet requires a stronger compatible teacher, while on-policy self-distillation relies on hand-designed privileged information. We observe that the MoE architecture itself offers a way to resolve this dilemma, as increasing the activation budget per token exposes latent expert capacity and yields a potentially stronger teacher within the model. However, naive expansion degrades performance because newly co-activated experts are not optimized to work together. We therefore propose MoEvolve, a bidirectional distillation framework following a recovery-then-improvement strategy: we first restore the activation-expanded high-$k$ model and further strengthen it by exploiting its additional active capacity, then reverse the direction of distillation to transfer the enhanced capabilities back into the original low-$k$ configuration, retaining its inference-time activation budget. Across diverse MoE models and benchmarks, MoEvolve improves the initial models by up to $22.2$ domain-average points and outperforms same-budget RLVR baselines by up to $6.5$ points. Notably, the final low-$k$ models often surpass their activation-expanded teachers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haoyu Chen, Jun Bai, Yang Liu, Jianfei Zhang, Wenge Rong
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
