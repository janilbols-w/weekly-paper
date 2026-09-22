---
title: "Adapting Tree-Structured Speculative Decoding to DeepSeek-V4 for Efficient Inference"
description: "Repeated execution of the target model during autoregressive decoding is a major source of LLM inference latency."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.24698) · [PDF](https://arxiv.org/pdf/2609.24698)

## 一句话摘要

Repeated execution of the target model during autoregressive decoding is a major source of LLM inference latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Repeated execution of the target model during autoregressive decoding is a major source of LLM inference latency. Unlike linear speculation, which follows a single candidate chain, tree-structured speculation retains multiple branches from shared prefixes; under the same budget, this broader coverage can improve acceptance and efficiency. Adapting it to DeepSeek-V4 is nontrivial: its CSA/HCA online compressed attention concentrates the difficulty on the target-verify side, where branches diverging from a shared prefix compress into different states, breaking cross-branch state consistency. We integrate tree-structured speculative decoding into the DeepSeek-V4-Flash pipeline via branch-aware causal verification, temporary state isolation, and accepted-path state refresh, keeping verification and compressed-state updates consistent across branches. Across budgets D=5 to D=8, batch sizes 1 to 64, and three datasets (GSM8K, MBPP, ShareGPT), tree speculation achieves a higher accepted length than the matched linear configurations in all settings (e.g., at D=8 about 2.83--3.41 versus 2.39--2.84) and improves throughput in nearly all configurations---marginal only at the smallest budget---by up to about 18.5%. More importantly, the gains follow stable, transferable regularities: the relative gain grows with the budget and is most pronounced for less predictable workloads at small-to-medium batch sizes, while beyond a certain budget throughput plateaus and decouples from the still-rising accepted length. These results show that retaining multiple candidate paths under the same budget can effectively improve DeepSeek-V4 decoding efficiency, and offer experience for adapting speculative decoding to future models with compressed, sparse, or structured context representations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Changxu Liu, Zhaogeng Li
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
