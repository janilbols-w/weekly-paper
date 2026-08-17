---
title: "ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation"
description: "Structured pruning is a hardware-friendly way to compress LLMs, but it is mostly validated on multiple-choice recognition tasks, while the same compressed checkpoints can collapse on the free-form generation that deployment actually requires."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.13124) · [PDF](https://arxiv.org/pdf/2607.13124)

## 一句话摘要

Structured pruning is a hardware-friendly way to compress LLMs, but it is mostly validated on multiple-choice recognition tasks, while the same compressed checkpoints can collapse on the free-form generation that deployment actually requires.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning is a hardware-friendly way to compress LLMs, but it is mostly validated on multiple-choice recognition tasks, while the same compressed checkpoints can collapse on the free-form generation that deployment actually requires. Two observations trace this gap. First, greedy \textsc{pass}@$1$ nearly vanishes after compression, yet \textsc{pass}@$k$ recovers substantially under repeated sampling: useful generations are demoted, not erased. Second, the recoverable regime fails mainly through suffix repetition. Recovery should therefore train on the compressed model's own on-policy states with dense token-level supervision, which On-Policy Distillation (OPD) provides by reusing the pre-compression model as a frozen teacher. However, long on-policy rollouts spend early recovery budget on low-information repetitive suffixes, delaying loss descent. To mitigate this waste, we propose \textbf{\shortopd}, a short-to-long OPD schedule that detects teacher-confirmed repetitive suffixes, treats the surviving prefix as each rollout's effective length, and allocates future rollout budgets to the effective lengths the policy can currently use. Across math, code, and open-ended generation, \shortopd\ raises the compressed model's score to about $9\times$ its unrecovered value and $1.6$--$4.4\times$ standard recovery recipes (SFT w/o KD, KD, and SeqKD), and it matches a fixed $8192$-token rollout horizon within two points using a quarter of the training time ($8.5$ vs.\ $35.9$ hours) and $71\%$ fewer rollout tokens. We hope this recipe helps move structured pruning beyond marginal gains on perplexity and multiple-choice benchmarks, a step closer to deployment-ready generation quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model, distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qingyu Zhang, Qianhao Yuan, Hongyu Lin, Yaojie Lu, Xianpei Han, Le Sun, Ming Xu, Jiarui Li
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
