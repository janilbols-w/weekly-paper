---
title: "Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data"
description: "As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.11917) · [PDF](https://arxiv.org/pdf/2609.11917)

## 一句话摘要

As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data.

## 为什么值得关注

待编辑增强。

## 摘要原文

As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data. Prior work has studied data repetition for densely activated Transformers, but the effects of data repetition remains largely unexplored for recently dominant sparse architectures such as Mixture-of-Experts (MoE), despite their increased compute efficiency. We vary data repetition rates across single- and multi-domain data mixes, and across MoE settings, including expert count and granularity. We consistently find, for models ranging from 80M to 1B active (8.5B total) parameters, that MoEs degrade more rapidly under data repetition. This effect increases with sparsity, dictated by total rather than active parameters. While 80M dense models can repeat data over 8x with minimal degradation, MoEs instead begin to suffer at 4x, and deteriorate rapidly, ceding their performance benefits in all-unique data settings to underperform dense models after 32x. We experiment with existing regularization methods as a potential remedy. We find that some methods, such as dropout, can mitigate overfitting. In particular, with strong masking-based regularization, MoEs are able to outperform dense models even when data is repeated more than 64 times. However, no method fully matches the performance of all-unique training data. Finally, we analyze internal mechanisms correlated with MoE overfitting in high repetition regimes, and find that MoE routing universally stabilizes early in training, and that expert specialization correlates with overfitting to repeated data. In sum, our work addresses the adverse interactions between sparsity and data repetition: we present evidence for the core mechanisms of overfitting and its potential remediation, and suggest promising avenues for future methods to reduce over-specialization in model parameters by disrupting memorization patterns.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Atindra Jha, Margaret Li, Jure Leskovec, Percy Liang, Luke Zettlemoyer
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
