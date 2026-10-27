---
title: "Self-Supervised Pretraining for PHM: What Transfers, What Does Not, and What Federating It Costs"
description: "Self-supervised pretraining has produced capable time-series foundation models, but its value for Prognostics and Health Management (PHM) has not been measured under leakage-controlled conditions."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.35280) · [PDF](https://arxiv.org/pdf/2610.35280)

## 一句话摘要

Self-supervised pretraining has produced capable time-series foundation models, but its value for Prognostics and Health Management (PHM) has not been measured under leakage-controlled conditions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-supervised pretraining has produced capable time-series foundation models, but its value for Prognostics and Health Management (PHM) has not been measured under leakage-controlled conditions. We measure it on a corpus of 47 public PHM datasets, harmonized to a single tensor contract and partitioned so that 11 datasets are withheld from pretraining in full. Transfer turns out to be task-dependent: a compact channel-independent Transformer encoder (801,808 parameters) pretrained with masked patch prediction raises fault-classification macro-F1 from 0.350 to 0.812 on CWRU and from 0.569 to 0.951 on HSG18, yet on CMAPSS remaining-useful-life estimation no pretrained checkpoint reliably improves upon a from-scratch baseline. We pretrain under two regimes---centralized, and simulated cross-silo federated with ten clients grouped by physical domain---holding architecture, objective, source data and optimization budget fixed. Two further findings are negative. At matched budget the centralized encoder leads by 15.5--20.2 macro-F1 points in four of four comparisons, although the comparison is confounded by a learning-rate schedule that favours the centralized arm and rests on a single pretraining run per regime; on RUL the two regimes are indistinguishable. And the intrinsic SSL loss is not a valid selection criterion: the centralized encoder more than halves the federated reconstruction loss without a corresponding gap on RUL, and a server-momentum sweep moves downstream validation macro-F1 by up to 0.29 while the SSL loss varies by 0.021. Transfer also hinges on the backbone learning rate: the same checkpoint yields 0.169 or 0.829 macro-F1 on CWRU depending on a single order of magnitude. We release the corpus pipeline, the protocol and the code.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jos\'e Sanz-Dur\'an, David Sol\'is-Mart\'in
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
