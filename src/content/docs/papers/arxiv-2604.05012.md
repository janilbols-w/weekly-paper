---
title: "Comparative Characterization of KV Cache Management Strategies for LLM Inference"
description: "Efficient inference with Large Language Models (LLMs) increasingly relies on Key-Value (KV) caches to store previously computed key and value vectors at each layer."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2604.05012) · [PDF](https://arxiv.org/pdf/2604.05012)

## 一句话摘要

Efficient inference with Large Language Models (LLMs) increasingly relies on Key-Value (KV) caches to store previously computed key and value vectors at each layer.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficient inference with Large Language Models (LLMs) increasingly relies on Key-Value (KV) caches to store previously computed key and value vectors at each layer. These caches are essential to minimize redundant computation during autoregressive token generation, lowering computational complexity from quadratic to linear. However, the growth of KV caches has posed significant system-level challenges, particularly as model sizes increase, context lengths grow, and concurrent requests compete for limited memory resources. Even though several recent frameworks for KV cache management have emerged, their comparative trade-offs in memory consumption and inference performance have not been fully understood, especially under varying request sizes and model configurations. In this work, we conduct an empirical study of three state-of-the-art KV cache management frameworks: vLLM, InfiniGen, and H2O. These frameworks employ techniques such as tensor offloading, token eviction heuristics, and speculative scheduling to balance memory usage and performance. We evaluate their performance in terms of a range of metrics such as latency, throughput, and memory usage across a spectrum of key parameters including request rates, model sizes, and sparsity levels. Our results pinpoint the conditions for each framework to perform the best, revealing the most suitable selection and configuration of KV cache strategies under memory and performance constraints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Oteo Mamo, Olga Kogiou, Hyunjin Yi, Weikuan Yu
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
