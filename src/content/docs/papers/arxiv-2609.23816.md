---
title: "SPLASH: A Virtualized HBM-HBF Hierarchy with Flash-Aware Sparse Attention for Long-Context Inference"
description: "As context lengths, request lifetimes and concurrency grow, the key-value (KV) cache dominates memory usage in large language model (LLM) inference."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.23816) · [PDF](https://arxiv.org/pdf/2609.23816)

## 一句话摘要

As context lengths, request lifetimes and concurrency grow, the key-value (KV) cache dominates memory usage in large language model (LLM) inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

As context lengths, request lifetimes and concurrency grow, the key-value (KV) cache dominates memory usage in large language model (LLM) inference. High-bandwidth memory (HBM), the memory on contemporary GPUs, achieves far higher bandwidth than off-package memory, yet its capacity, bounded by DRAM density, has not kept pace with this demand. High-Bandwidth Flash (HBF), an emerging memory technology, bridges this gap, combining the advanced packaging of HBM with the density of flash to deliver terabyte-scale capacity at HBM-class read bandwidth. Exploiting this capacity for long-context KV caches, however, requires hiding the vastly different physical characteristics of flash from the GPU while keeping decode interactive. We therefore introduce Splash, an architecture that virtualizes HBM and HBF for the KV cache. We architect custom HBM and HBF base dies with novel memory and flash controllers that handle the access semantics and device management of flash. These controllers keep the GPU agnostic of the underlying memory, allowing the HBM-HBF hierarchy to behave as one logical memory for the KV cache. The added capacity of HBF enables long contexts, but dense attention, which reads the entire KV cache for every generated token, cannot keep decode interactive at these lengths. Splash therefore makes sparse attention flash-aware through query-driven address translation, in which the HBF base die resolves each query into the flash addresses of the relevant KV pages and schedules their reads across flash planes. Since the HBF base die holds the location of every page, this translation hides flash from the GPU and balances the selected reads across flash planes, coupling abstraction with performance. Across five models and up to one million tokens, Splash improves per-GPU decode throughput by up to 4.5x over the strongest baseline under a 100 ms latency budget.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aditya Anirudh Jonnalagadda, Agasthi Haputhanthri, Pranav Dangi, Rohan Juneja, Wenshuo Yue, Aritra Bagchi, Bin Gao, Tulika Mitra
- 发布：2026-09-20；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
