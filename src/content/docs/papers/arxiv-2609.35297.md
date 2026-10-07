---
title: "LionMuon: Alternating Spectral and Sign Descent for Efficient Training"
description: "Pretraining a language model takes enormous compute, and the right optimizer can save a good part of it."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.35297) · [PDF](https://arxiv.org/pdf/2609.35297)

## 一句话摘要

Pretraining a language model takes enormous compute, and the right optimizer can save a good part of it.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pretraining a language model takes enormous compute, and the right optimizer can save a good part of it. Muon's spectral step gives a stronger direction than a sign step, but it is expensive. Every step runs Newton-Schulz iterations on the full matrix and, in distributed training, an extra all-reduce. Sign steps, as in Lion and Signum, are cheap and stay local to each device. We propose LionMuon, which takes one Muon step every $P$ iterations and Lion steps in between, with a single dual-EMA momentum buffer shared by both. Muon's compute and communication are paid once per $P$ steps, and the optimizer state is half of AdamW's. A single-EMA variant, SignMuon, already improves on Muon. We prove complexity bounds under heavy-tailed noise in which the period sets an interpolation between Muon's and Lion's smoothness and noise constants, and which say when LionMuon is faster than both. On 124M and 355M models trained on FineWeb, LionMuon with $P=2$ and $P=5$ reaches a lower loss than Muon, AdamW, Lion and Signum at the same number of tokens. Under 4-GPU data-parallel training it reaches Muon's final loss with a third less wall-clock on PCIe, and it beats the communication-efficient Muon variants Dion and MuonBP on loss at no more exposed communication, while keeping the exact gradient. Code: https://github.com/brain-lab-research/lion-muon

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Arman Bolatov, Artem Riabinin, Nikita Kornilov, Andrey Veprikov, Samuel Horváth, Martin Takáč, Aleksandr Beznosikov
- 发布：2026-09-28；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/brain-lab-research/lion-muon](https://github.com/brain-lab-research/lion-muon)
- 阅读深度：metadata
