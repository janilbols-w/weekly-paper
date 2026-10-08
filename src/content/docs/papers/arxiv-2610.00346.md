---
title: "Benchmarking System One decision models against trained classifiers and language models for automated decision gates"
description: "Software that hands branching decisions to a model needs a declared option and a probability it can threshold."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.00346) · [PDF](https://arxiv.org/pdf/2610.00346)

## 一句话摘要

Software that hands branching decisions to a model needs a declared option and a probability it can threshold.

## 为什么值得关注

待编辑增强。

## 摘要原文

Software that hands branching decisions to a model needs a declared option and a probability it can threshold. Typed decision models, also called System One models, return such probabilities without generating text, while supervised classifiers and generative language models are the established alternatives. One harness sends eight decision-model checkpoints from six families, including the hosted model Jev, and four open generative models from three developers the same semantic requests, and scores trained and zero-shot classifiers on the same workflow, intent, emotion and social-science items. With task labels, a fine-tuned DeBERTa-v3-large has the highest observed accuracy on every labeled benchmark but one. Without labels, no decision model is significantly more accurate than Jev on workflows or intents, but Gemma-4-31B matches it on workflows and exceeds it on CLINC-150 at higher cost and latency. Stated probabilities of generative models become unreadable when replies miss the key format, whereas key likelihoods avoid this but can saturate. A guaranteed 5 percent risk leaves Jev 0.528 of the intent decisions, and an in-scope threshold still accepts 0.310 of out-of-scope requests. On typed-decisions, swapping yes and no flips 50.5 answers per hundred for Jev and at least 16.8 for every generative model tested, against at most 6.5 for four fine-tuned decision checkpoints. Exposure to a benchmark's training data explains the largest lead of an open checkpoint, which vanishes on rater-labeled emotions. An intent-trained first stage escalating to Gemma-4-31B reaches that model's accuracy at about Jev's price. The results yield condition-dependent design rules for automated decision gates.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Amir Rafe, Subasish Das
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
