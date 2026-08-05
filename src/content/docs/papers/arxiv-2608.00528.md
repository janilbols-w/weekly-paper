---
title: "S$^4$R: Selective Sampling, Subspaces, and Sparse Reconstruction for Compressed Long-Context KV Caching"
description: "The growth of context window lengths in Large Language Models (LLMs) significantly enhances their long-context capabilities but incurs prohibitive memory costs due to the Key-Value (KV) cache."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.00528) · [PDF](https://arxiv.org/pdf/2608.00528)

## 一句话摘要

The growth of context window lengths in Large Language Models (LLMs) significantly enhances their long-context capabilities but incurs prohibitive memory costs due to the Key-Value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

The growth of context window lengths in Large Language Models (LLMs) significantly enhances their long-context capabilities but incurs prohibitive memory costs due to the Key-Value (KV) cache. Although low-rank compression of KV cache is a promising remedy, existing methods face a dilemma: offline approaches depend on external calibration data, whereas online approaches incur substantial compute for full-prompt decomposition and reconstruction. In this paper, we propose S$^4$R, which builds low-rank subspaces from selectively sampled tokens and computes attention over a sparsely reconstructed KV representation. S$^4$R uses prompt-aware initialization to build initial key/value bases from a representative prompt subset, trading off calibration-data dependence against prefilling cost. Because fully reconstructing the cache at every decoding step is prohibitively expensive and hurts throughput, we further adopt sparse reconstruction to retain only informative positions during decoding. Extensive experiments on LongBench and RULER with Llama and Qwen model families show that S$^4$R achieves up to 5$\times$ KV compression with near full-cache accuracy, combining the efficiency of fixed compression with the adaptability of prompt-dependent methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jialong Han, You Wu, Kewei Tu
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
