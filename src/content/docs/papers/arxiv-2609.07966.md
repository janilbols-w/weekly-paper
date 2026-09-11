---
title: "MetaKV: Adaptive KV Cache Compression for Constrained LLM Inference"
description: "Key--value (KV) cache compression is an effective way to reduce the memory overhead of large language model (LLM) inference, particularly for long-context workloads."
---

**评分：54/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.07966) · [PDF](https://arxiv.org/pdf/2609.07966)

## 一句话摘要

Key--value (KV) cache compression is an effective way to reduce the memory overhead of large language model (LLM) inference, particularly for long-context workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Key--value (KV) cache compression is an effective way to reduce the memory overhead of large language model (LLM) inference, particularly for long-context workloads. However, existing compression methods make different trade-offs among accuracy, inference latency, and peak KV cache memory utilization, making a single fixed configuration unsuitable across different prompts and resource constraints. We introduce MetaKV, an adaptive framework that selects a KV cache compression configuration for each input prompt based on user-specified latency and peak memory budgets. MetaKV uses lightweight prediction models to estimate the end-to-end latency, peak memory, and probability of a correct response for each candidate configuration, and selects the configuration that best satisfies the latency-memory constraints while preserving accuracy. We evaluate MetaKV across ten configurations from three representative KV cache compression methods, KVQuant, H$_2$O, and RocketKV, together with an uncompressed FP16 configuration, on four datasets covering mathematics, science, commonsense reasoning, and reading comprehension. Across a wide range of latency and peak memory constraints, MetaKV consistently outperforms the best static configuration, improving constrained success rate (CSR), the fraction of prompts answered correctly while satisfying both constraints, by approximately 0.07 on average and up to 0.135. These results demonstrate the benefit of adapting KV cache compression to individual prompts and latency-memory constraints. Code is available at https://github.com/MichaelWang0505/MetaKV.git

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Michael Wang, Keith Li, Roozbeh Bostandoost
- 发布：2026-09-07；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/MichaelWang0505/MetaKV.git](https://github.com/MichaelWang0505/MetaKV.git)
- 阅读深度：metadata
