---
title: "Free Pause Tokens"
description: "A free pause token gives a language model extra compute to form each next-token prediction (as a pause, or thinking, token does) but carries that compute in a parallel prediction stream over a weight-shared backbone rather than as an extra token in the sequence."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.03807) · [PDF](https://arxiv.org/pdf/2609.03807)

## 一句话摘要

A free pause token gives a language model extra compute to form each next-token prediction (as a pause, or thinking, token does) but carries that compute in a parallel prediction stream over a weight-shared backbone rather than as an extra token in the sequence.

## 为什么值得关注

待编辑增强。

## 摘要原文

A free pause token gives a language model extra compute to form each next-token prediction (as a pause, or thinking, token does) but carries that compute in a parallel prediction stream over a weight-shared backbone rather than as an extra token in the sequence. It improves next-token prediction by 2-3 centinats in practice on a 1B parameter model. Because the pause rides an existing position instead of adding one, it is free to use: at inference it adds no context length, no KV cache, and essentially no latency with the growth in inference flops typically irrelevant as it is not the active bottleneck on throughput. The only primary cost is in training, where additional training compute versus an optimized pretraining pipeline is reduced to as low as x1.14 while preserving most of the benefits. The result is an isoflop, isoparameter, and isotoken improvement over standard next token trained transformers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：John Langford, Nathan Godey, Giovanni Monea, Yoav Artzi, Harry Dong, Ying Fan, Gustavo de Rosa, Zheng Zhan
- 发布：2026-09-03；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
