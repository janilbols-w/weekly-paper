---
title: "PackLoop: Row-Packed Self-Speculative Decoding for Looped Language Models under Concurrency"
description: "Looped language models reuse one block of weights T times per token, trading parameters for test-time depth, but autoregressive decoding then pays T sequential passes per token."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.30205) · [PDF](https://arxiv.org/pdf/2611.30205)

## 一句话摘要

Looped language models reuse one block of weights T times per token, trading parameters for test-time depth, but autoregressive decoding then pays T sequential passes per token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped language models reuse one block of weights T times per token, trading parameters for test-time depth, but autoregressive decoding then pays T sequential passes per token. Self-speculative decoders recover 2-10x for a single request, yet their gains fade as requests share a GPU, and current practice is to speculate less as load grows. We show that what fails under load is the layout of speculative work, not speculation. In concurrent decoding the unit of cost is the row, one request advancing on one loop, which reads that loop's key-value (KV) cache once; additional positions inside a row are nearly free. Pipelined schedules such as the wavefront place every speculative position on a different loop, hence in a row of its own, so each token is still read T times. We present PackLoop, built on one principle: speculate only inside rows that are read anyway. Deep loops accumulate positions and advance them as a block in one row, context-copy proposals join the row that the first loop already reads, and a closed-form admission rule, the economic order quantity of inventory theory, sets how long to accumulate from a cost model calibrated once per engine. PackLoop is exact: in FP32 its output is token-for-token identical to autoregressive decoding, also under sampling and early exit. Across 164 load points spanning three GPUs, four Ouro models, six benchmarks, and contexts up to 32K tokens, one PackLoop configuration is faster than the best existing schedule, chosen per point, at 161 points (median 1.25x, up to 1.76x) and never significantly slower. Its lead grows with concurrency and context length, the regime in which existing self-speculation gains least.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Runguo Li, Dezhen Lu
- 发布：2026-11-23；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
