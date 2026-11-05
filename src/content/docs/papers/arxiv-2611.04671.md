---
title: "LeanSparse: Memory-Efficient Serving for Native Sparse-Attention LLMs"
description: "Sparse attention limits the history read by each query, but serving long contexts still requires substantial GPU memory."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.04671) · [PDF](https://arxiv.org/pdf/2611.04671)

## 一句话摘要

Sparse attention limits the history read by each query, but serving long contexts still requires substantial GPU memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse attention limits the history read by each query, but serving long contexts still requires substantial GPU memory. Existing KV offloading systems retain the full history of indexer keys on GPU, limiting decode concurrency. Prefill's temporary memory demand can further delay admission even when enough memory remains for the same request's subsequent decode. We present LeanSparse, a serving system that reduces both decode's persistent memory use and prefill's temporary memory demand. Our design exploits two observations: prefill consumes historical data one layer at a time, and decode can identify promising candidates before comparing their original indexer scores. During prefill, LeanSparse streams layer histories through two reusable GPU buffers, overlapping next-layer loading with ongoing model computation. During decode, coarse-to-fine indexing searches compact representations and retrieves original indexer keys only for candidate refinement. Separate indexer key and KV caches reuse data across generation steps. We implement LeanSparse in SGLang and evaluate it on DeepSeek-V4-Flash. At 950K context length, LeanSparse supports 2.95$\times$ as many concurrent requests and achieves 2.14$\times$ decode throughput over HiSparse. On multi-turn Open-SWE traces, it reduces median time to first token from 21.6 to 0.6s and median session completion time by 17.7% relative to ECHO.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zaifeng Pan, Chris Wu, Xinwei Qiang, Zhengding Hu, Zhongkai Yu, Yufei Ding
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
