---
title: "STS: Efficient Sparse Attention with Speculative Token Sparsity"
description: "The quadratic complexity of attention imposes severe memory and computational bottlenecks on Large Language Model (LLM) inference."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.15508) · [PDF](https://arxiv.org/pdf/2605.15508)

## 一句话摘要

The quadratic complexity of attention imposes severe memory and computational bottlenecks on Large Language Model (LLM) inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

The quadratic complexity of attention imposes severe memory and computational bottlenecks on Large Language Model (LLM) inference. This challenge is particularly acute for emerging agentic applications that require processing multi-million token sequences. We propose STS, a sparse attention mechanism that requires no model retraining. STS leverages the key insight that tokens identified as important by a smaller draft model are highly predictive of important tokens for a larger target model. By integrating into speculative decoding frameworks, STS repurposes the draft model's attention scores to dynamically construct a token-and-head-wise sparsity mask. This mask effectively prunes the expensive attention computation in the target LLM. Our evaluation shows that STS achieves a 2.67x speedup operating at approximately 90% sparsity on representative benchmark NarrativeQA, maintaining negligible accuracy degradation compared to dense attention. STS establishes a new state-of-the-art on the sparsity-accuracy trade-off, outperforming prior techniques by enabling higher sparsity levels for a given accuracy budget.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiangnan Yu, Ceyu Xu, Yongji Wu, Yuan Xie
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
