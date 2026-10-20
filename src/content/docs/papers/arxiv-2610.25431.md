---
title: "MOSAIC: Multi-Objective Search for Allocating Inference Cache Across LLM Decoder Layers"
description: "The Key-Value (KV) cache is the main memory bottleneck of long-context LLM inference."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.25431) · [PDF](https://arxiv.org/pdf/2610.25431)

## 一句话摘要

The Key-Value (KV) cache is the main memory bottleneck of long-context LLM inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

The Key-Value (KV) cache is the main memory bottleneck of long-context LLM inference. Token eviction methods such as SnapKV, H2O, AdaKV and L2Norm shrink it, but they give every transformer layer the same budget, although layers differ in which tokens they need. We present MOSAIC, a multi-objective neural architecture search that learns per-layer KV-cache budgets for any eviction method. One search maps the trade-off between average budget and task score; its best allocation transfers to every target budget without further search, and an optional budget-constrained search refines it. Across four eviction methods on Llama-3-8B-Instruct and Mistral-7B-Instruct-v0.2, MOSAIC beats uniform allocation in 146 of 154 (task, method, budget) settings, by up to +48 points on RULER and +11.9 on LongBench (LCC). On both models, it reaches the score of uniform allocation with up to 4x less KV cache (75% smaller). Against EvolKV, MOSAIC explores a ~10^40 x larger search space with 4x fewer evaluations and 18% fewer GPU-hours per budget, and scores higher in 5 of 6 settings. The learned allocations consistently favour a small set of middle layers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Sravanth Kodavanti, Manjunath Arveti
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
