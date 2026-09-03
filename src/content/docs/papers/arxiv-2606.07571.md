---
title: "Enabling KV Caching of Shared Prefix for Diffusion Language Models"
description: "Key-value (KV) caching for shared prefixes is essential for high-throughput large language model (LLM) serving, but it faces critical challenges in emerging diffusion language models (DLMs)."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.07571) · [PDF](https://arxiv.org/pdf/2606.07571)

## 一句话摘要

Key-value (KV) caching for shared prefixes is essential for high-throughput large language model (LLM) serving, but it faces critical challenges in emerging diffusion language models (DLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Key-value (KV) caching for shared prefixes is essential for high-throughput large language model (LLM) serving, but it faces critical challenges in emerging diffusion language models (DLMs). In DLMs, bidirectional attention means that updating any token dynamically alters the entire context and its corresponding KVs. Thus, existing caching techniques developed for LLMs, which assume that KVs remain invariant once computed, corrupt the shared prefix KVs. Our experiments show that applying these techniques to DLMs causes model accuracy to collapse to near zero. To unlock high-throughput DLM serving, we propose bidirectional prefix caching, BiCache, the first KV caching technique for shared prefixes in DLMs. BiCache is designed based on key observations from our comprehensive analysis: shared prefix KVs remain stable and reusable in shallow layers, while the depth of shallow layers depends on the fraction of shared prefix tokens in each request. Thus, BiCache dynamically identifies a safe layer depth for reusing shared prefix KVs and eliminates redundant computation. Evaluations demonstrate that BiCache significantly improves serving throughput by 36.3%-98.3% compared to existing techniques without accuracy collapse (only 0-1.8% difference).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Younghun Go, Jaehoon Han, Changyong Shin, Chuck Yoo, Gyeongsik Yang
- 发布：2026-09-02；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
