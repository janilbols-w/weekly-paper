---
title: "Certified Sparse Attention via Perturbed Retrieval"
description: "Sparse attention speeds up long-context decoding by reading few keys of the KV cache, but existing methods do not control the error of a query, and on real KV caches their errors have heavy tails."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.24991) · [PDF](https://arxiv.org/pdf/2610.24991)

## 一句话摘要

Sparse attention speeds up long-context decoding by reading few keys of the KV cache, but existing methods do not control the error of a query, and on real KV caches their errors have heavy tails.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse attention speeds up long-context decoding by reading few keys of the KV cache, but existing methods do not control the error of a query, and on real KV caches their errors have heavy tails. We show that perturbing the score of every key with an independent Exp(1) variable turns threshold retrieval into sampling keys with probability proportional to their attention weights. Lowering the threshold along a geometric grid gives nested samples, a Horvitz--Thompson estimate of the output at every level, and confidence bounds that hold simultaneously over all levels, so each head stops at the first level whose certificate meets the target error $\varepsilon$. With fresh perturbations at every decoding step, each certificate fails with probability at most $\delta$ during generation. At a suitable threshold, the estimator reads $O(\varepsilon^{-2}\log(1/\delta))$ values regardless of the context length, and no adaptive method reads fewer, up to constants. A 4-bit scan with deterministic bounds, shared across a grouped-query-attention group, generates the candidates exactly but reads every key. On three LLMs and ten settings at 16K--128K tokens, no certificate is violated, and at equal keys read our 90th-percentile error is 4.6--7.9$\times$ lower than that of the best of 15 baseline families. At equal bytes, the best baselines have 0.6--1.6 times our 90th-percentile error and at least 4.9 times our largest. End to end, our method stays within one point of dense attention on tasks and within 0.1\% in PG-19 perplexity, and the strongest baselines at equal bytes score as well. On CPU, decoding steps at 32K--128K tokens run 1.1--1.4$\times$ faster than dense attention on the same 16-bit cache.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Runguo Li
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
