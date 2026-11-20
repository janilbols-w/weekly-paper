---
title: "When Features Beat Noise: A Noise-Driven Hypothesis Testing Method for Feature Selection"
description: "Feature selection has remained a daunting challenge in machine learning and artificial intelligence, where increasingly complex, high-dimensional datasets demand principled strategies for isolating the most informative predictors."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2511.20851) · [PDF](https://arxiv.org/pdf/2511.20851)

## 一句话摘要

Feature selection has remained a daunting challenge in machine learning and artificial intelligence, where increasingly complex, high-dimensional datasets demand principled strategies for isolating the most informative predictors.

## 为什么值得关注

待编辑增强。

## 摘要原文

Feature selection has remained a daunting challenge in machine learning and artificial intelligence, where increasingly complex, high-dimensional datasets demand principled strategies for isolating the most informative predictors. Despite widespread adoption, many established techniques such as Boruta, Recursive Feature Elimination and other wrapper based methods suffer from notable limitations; some incur substantial computational cost, while others offer no definite statistical driven stopping criteria or assess the significance of their importance scores. This paper proposes a novel feature selection method that addresses these limitations. Our approach introduces multiple random noise features and evaluates each feature's importance against the maximum importance value among these noise features incorporating a non-parametric bootstrap-based hypothesis testing framework to establish a solid theoretical foundation. We establish the conceptual soundness of our approach through statistical derivations that articulate the principles guiding the design of our algorithm. To assess reliability and practical utility, we validated the method on controlled simulations and diverse real-world datasets, where it consistently outperformed established feature-selection approaches including Boruta, Model-X Knockoffs, RFE, LASSO, Elastic Net, and mRMR in recovering meaningful signals. Hence, the method emerges as a robust algorithm for principled feature selection, enabling the distillation of informative predictors that support reliable inference, enhanced predictive performance, and efficient computation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mousam Sinha, Tirtha Sarathi Ghosh, Koushik Biswas, Ridam Pal
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
