---
title: "Honeyed Words, Hidden Daggers: Benchmarking and Training LLMs to See Through Mock Politeness"
description: "The Chinese idiom \"kou mi fu jian\" (\"honeyed words, hidden daggers\") names speech that is polite in form but hostile in function."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.26059) · [PDF](https://arxiv.org/pdf/2610.26059)

## 一句话摘要

The Chinese idiom "kou mi fu jian" ("honeyed words, hidden daggers") names speech that is polite in form but hostile in function.

## 为什么值得关注

待编辑增强。

## 摘要原文

The Chinese idiom "kou mi fu jian" ("honeyed words, hidden daggers") names speech that is polite in form but hostile in function. We present ZhenhuanBench, a 1,592-item benchmark built from expert commentary on Empresses in the Palace, covering speaker intent, emotion-language mismatch, and per-listener uptake. Text-only evaluation covers 34 LLMs. GPT-6 Astra leads the leaderboard at 73.48% overall, while its listener-reaction score is 58.37%. The annotations also supply supervised traces and string-verifiable training rewards. With 338 gold traces, an 8B model outperforms teacher distillation on identical items. Subsequent RL saturates, and chance correction reduces the estimated recoverable performance gap by a factor of 7.5. Our CPR-GRPO loop (Compress-Probe-Replenish) uses this estimate to weight gold supervision, reaching 67.0 on public multiple-choice tasks and 74.5 under the training-matched hidden protocol. Without target-task training, CPR outperforms Base, SFT, and GRPO across six Chinese and English pragmatic and sarcasm evaluations. On three external datasets, training with CPR yields higher mean Macro-F1 than SFT and GRPO.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Caixin Kang, Sitong Gong, Tianyu Yan, Kaipeng Zhang, Yoichi Sato, Yifei Huang
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
