---
title: "Agentic Search Spaces for Tabular Machine Learning"
description: "Despite the rapid progress of LLM-based agents for planning, code generation, and debugging, their practical value for tabular machine learning remains underexplored."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.16309) · [PDF](https://arxiv.org/pdf/2609.16309)

## 一句话摘要

Despite the rapid progress of LLM-based agents for planning, code generation, and debugging, their practical value for tabular machine learning remains underexplored.

## 为什么值得关注

待编辑增强。

## 摘要原文

Despite the rapid progress of LLM-based agents for planning, code generation, and debugging, their practical value for tabular machine learning remains underexplored. In this paper, we investigate a concrete use case: whether state-of-the-art agentic AI systems can design extended HPO search spaces for established tabular models that outperform the standard search spaces provided by the model authors. Specifically, we represent each tabular model as a modular pipeline covering preprocessing, embeddings, architecture, training, and inference. We then task the agent to propose candidate code implementations for each module and use a classical HPO algorithm to jointly optimize over these candidates and the model's default hyperparameters. Compared with the base HPO spaces, the expanded search spaces improve the performance of nearly every model family across a suite of 45 datasets, with average relative gains of 0.6%, rising to 2.0% on small-to-medium regression datasets. Notably, these gains come at no extra tuning cost: the enlarged spaces outperform the base under the same tuning and ensembling budgets. The gains transfer to the recent TabArena benchmark, where the agentic spaces improve the official Elo scores of four of the five model families and the two strongest agentic ensembles surpass the best AutoGluon ensemble of conventional models. Overall, our study suggests that LLM agents can provide practical value for tabular ML by expanding the design space.

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

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Renat Sergazinov, Artem Chistyakov, Sergey Pankevich, Artem Babenko
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
