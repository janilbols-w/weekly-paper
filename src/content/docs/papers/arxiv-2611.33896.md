---
title: "Looped Models are Fast Multi-Token Predictors"
description: "Looped language models can adapt computation for predicting a token without a proportional rescaling in unique model parameters by adjusting the number of loops."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.33896) · [PDF](https://arxiv.org/pdf/2611.33896)

## 一句话摘要

Looped language models can adapt computation for predicting a token without a proportional rescaling in unique model parameters by adjusting the number of loops.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped language models can adapt computation for predicting a token without a proportional rescaling in unique model parameters by adjusting the number of loops. This property has been used for self-speculative decoding, taking shallow loops as fast drafters and deep loops as verifiers, which is effective since drafting still uses full parameters. In this paper, we show that shallow loops can be also predictive of several future tokens and leverage this to drastically accelerate the inference of looped language models. To that end, we present Floodgates, a simple self-speculative decoding method that appends a block of mask tokens as a suffix and learns via low-rank adaptation to draft these tokens in parallel. Across seven models, five benchmarks, a range of batch sizes, and both greedy and sampled decoding, Floodgates is the fastest lossless decoding method in most cases, attaining up to 7.5x acceleration. Through analysis, we show that this speedup is enabled by all-depth training of looped models, with the shallow drafter's ability to leverage full-depth computation by conditioning on deep prefix cache evaluated during verification.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ayhan Suleymanzade, Sean McLeish, Sehoon Kim, Jinwoo Kim, Antoine Bosselut
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
