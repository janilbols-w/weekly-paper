---
title: "Spexis: Speculative Lookahead Scheduling for LLM Inference"
description: "Spexis is a multi-GPU LLM inference framework that improves the efficiency of pipeline and tensor parallelism through speculative parallelism."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.34370) · [PDF](https://arxiv.org/pdf/2609.34370)

## 一句话摘要

Spexis is a multi-GPU LLM inference framework that improves the efficiency of pipeline and tensor parallelism through speculative parallelism.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spexis is a multi-GPU LLM inference framework that improves the efficiency of pipeline and tensor parallelism through speculative parallelism. Rather than using speculative decoding only to accelerate token generation, Spexis runs speculation in parallel with normal execution, introducing a new parallelism axis without increasing KV-cache memory usage. This improves memory efficiency and helps mitigate the bottlenecks of multi-GPU inference. Spexis further uses lookahead scheduling to predict speculation quality and future memory pressure, allowing it to reduce wasted speculation, KV-cache eviction, and recomputation. Built on top of vLLM, Spexis largely improves serving performance across a range of GPU configurations, achieving speedups of up to 34% over a baseline that uses the optimal combination of pipeline and tensor parallelism. Spexis's source code is publicly available at https://github.com/mlsys-seo/spexis.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hyungyu Jung, Jaehyeok Yu, Hoonseo Choi, Sungkyun Kim, Jinho Lee, Jiwon Seo
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/mlsys-seo/spexis](https://github.com/mlsys-seo/spexis)
- 阅读深度：metadata
