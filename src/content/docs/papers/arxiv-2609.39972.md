---
title: "UBTree: Parallel Tree Drafting via Unigram and Bigram Models for Speculative Decoding"
description: "Speculative decoding accelerates language model inference by verifying multiple draft tokens in a single target-model pass."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](http://arxiv.org/abs/2609.39972v1) · [PDF](https://arxiv.org/pdf/2609.39972v1)

## 一句话摘要

Speculative decoding accelerates language model inference by verifying multiple draft tokens in a single target-model pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates language model inference by verifying multiple draft tokens in a single target-model pass. Recent parallel drafters have achieved breakthrough performance in frontier production models, but their effectiveness deteriorates as the entropy of target distributions increases due to insufficient draft diversity. To overcome this bottleneck without sacrificing parallelism, we introduce UBTree, a parallel drafter that couples a Unigram proposer with a Bigram selector to construct drafting Trees. The unigram proposer is trained with the standard cross-entropy objective to generate candidate tokens independently for each position, while a lightweight bigram selector predicts transition scores between adjacent candidate pairs. Unlike the proposer, the selector is trained with a renormalized KL objective on high-temperature data. This tree-native training broadens the supervision beyond the greedy path, encouraging plausible alternative branches that improve the chance of accepting additional tokens during tree verification. Across seven standardized benchmarks with Qwen3-4B and Qwen3-8B, UBTree achieves an average speedup of $5.84$--$6.94\times$ over autoregressive decoding and outperforms DARTree in all 28 comparisons. Production-scale evaluation further demonstrates UBTree's advantage over frontier baselines such as DSpark.

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

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chumeng Liang, Linxuan Wang, Xinyu Peng, Huabin Liu, Yuxin Chen, Ge Liu, Guang Lin, Qifan Song, Jianguo Li
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
