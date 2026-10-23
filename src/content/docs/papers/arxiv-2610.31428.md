---
title: "Predictable performance is suboptimal, and what it means for model routing"
description: "Large language models (LLMs) differ in capabilities and costs, motivating routing methods that adaptively choose a model for each query."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2610.31428) · [PDF](https://arxiv.org/pdf/2610.31428)

## 一句话摘要

Large language models (LLMs) differ in capabilities and costs, motivating routing methods that adaptively choose a model for each query.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) differ in capabilities and costs, motivating routing methods that adaptively choose a model for each query. These methods rely on performance prediction: given a query, estimate whether a model will answer it correctly. Most routing methods train separate predictors of candidate models' performance to guide model selection. Our work shows that performance prediction only beats a simple baseline when the candidate model is suboptimal on the task or the performance predictor adds significant capacity relative to the candidate model. Specifically, we take a model's self-confidence, the probability it assigns to its chosen answer, as a baseline and study how much a performance predictor can improve on it. First, we show that any performance predictor that outperforms a model's self-confidence can be used to improve the model's loss: the predictor's advantage transfers exactly in log loss through recalibration. Second, accounting for the predictor's additional parameters, we bound its advantage by the model's suboptimality plus the gain from those parameters. Third, we extend our theoretical results to two-model cascades, which route queries to a more capable model when the first model is predicted to fail. Experiments with 16 language models on four benchmarks show that predictors gain a larger advantage over self-confidence on more suboptimal models. This advantage shrinks as models improve through finetuning. Cascading exhibits the same two patterns: predictor-based routing offers larger gains over confidence-based routing for more suboptimal models, and these gains diminish after finetuning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guanhua Zhang, Moritz Hardt
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
