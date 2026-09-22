---
title: "Length Penalties Make Chain-of-Thought Less Monitorable"
description: "Recent work trains reasoning models with length penalties to curb overthinking and cut inference cost."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.09786) · [PDF](https://arxiv.org/pdf/2607.09786)

## 一句话摘要

Recent work trains reasoning models with length penalties to curb overthinking and cut inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent work trains reasoning models with length penalties to curb overthinking and cut inference cost. We show that these penalties make the chain of thought less monitorable. A length-compressed model still lets misleading hints steer its answers, but it less often verbalizes their influence. We train Qwen3-4B and Qwen3-14B with reinforcement learning under length penalties targeting 60% down to 30% of baseline chain-of-thought length, then evaluate them with nine types of biasing hints on held-out MMLU-Pro-R and four transfer benchmarks. A chain is faithful when an LLM monitor can tell from it that the hint influenced the answer. At the 30% target, accuracy stays near baseline and wrong-answer hints switch answers as often as before. Yet faithfulness drops on every evaluation set for both models, by 39% for Qwen3-14B and 35% for Qwen3-4B on MMLU-Pro-R. A control trained with the same correctness and format rewards but no length penalty leaves faithfulness intact or raises it. Shortening alone does not explain the drop. Compressed chains mention the hint 7 to 35 percentage points less often than the uncompressed model's chains shortened to the same length by random sentence deletion, across both model sizes and all five evaluation sets. Length penalties therefore trade monitorability for inference cost by removing the evidence monitors depend on.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bryce Little
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
