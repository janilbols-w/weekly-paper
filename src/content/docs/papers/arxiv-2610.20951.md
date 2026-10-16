---
title: "LEV: Thinking Fast and Deep with Looped Decision Models"
description: "Decision models answer typed questions about an input with one probability per option, computed in a single forward pass without generating text."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.20951) · [PDF](https://arxiv.org/pdf/2610.20951)

## 一句话摘要

Decision models answer typed questions about an input with one probability per option, computed in a single forward pass without generating text.

## 为什么值得关注

待编辑增强。

## 摘要原文

Decision models answer typed questions about an input with one probability per option, computed in a single forward pass without generating text. Like the fast System 1 of dual-process theory, they answer at once, but their depth is fixed at training time, so they spend the same computation on easy and hard questions. Models that reason in generated text can think longer, but they pay for every extra step in decoded tokens. We present LEV, a decision model that thinks deeper by rerunning its layers in a loop instead of generating tokens. LEV builds on a language model pretrained as a loop, reads the options after every loop step and trains all steps jointly, so one checkpoint can answer at any depth. On three looped backbones, accuracy rises with depth on the same weights, mostly on hard questions, and a 2.6B LEV goes from 63.2% at depth one to 76.2% at depth four on JevBench. On-demand depth, set per question by a small stopper with a threshold fitted on unlabelled requests, saves 15% to 24% of the computation at a cost of under one accuracy point, level with or slightly above a fixed mix of depths. On a locked test set, the 1.4B and 3B models are 5.4 to 8.8 points more accurate than dense (non-looped) models and cascades of the same latency below 50 ms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Dingjie Song, Zhiling Yan, Yuxuan Zhang, Lichao Sun
- 发布：2026-10-14；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/OpenLAIR/lev](https://github.com/OpenLAIR/lev)
- 阅读深度：metadata
