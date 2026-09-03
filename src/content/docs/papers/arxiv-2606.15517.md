---
title: "SHARD: Safe and Helpful Alignment via Self-Reframing Distillation"
description: "Large language models often struggle with sensitive prompts."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.15517) · [PDF](https://arxiv.org/pdf/2606.15517)

## 一句话摘要

Large language models often struggle with sensitive prompts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models often struggle with sensitive prompts. They may refuse outright, provide generic safety boilerplate, or fail to address the user's legitimate informational needs that can be answered safely. We introduce SHARD, a self-reframing distillation method to improve safe-helpfulness. It first rewrites sensitive prompts to surface benign intent using philosophical guidelines, then reframes its original responses into safe, more helpful ones, and finally fine-tunes the model on its self-reframed responses. Across DNA and the English subset of LINGUASAFE, SHARD improves helpfulness for most model families while preserving safety. It also remains competitive with distillation from a larger teacher model, suggesting that models can internalize safe and helpful behavior elicited from their own. Warning: This paper contains content that may be offensive or harmful.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Viswonathan Manoranjan, Amogh Gupta, Anvesh Rao Vijjini, Thomas Hofweber, Snigdha Chaturvedi
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
