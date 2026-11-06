---
title: "EntropyCache: Decoded Token Entropy Guided KV Caching for Diffusion Language Models"
description: "Diffusion-based large language models (dLLMs) rely on bidirectional attention, which prevents lossless KV caching and requires a full forward pass at every denoising step."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2603.18489) · [PDF](https://arxiv.org/pdf/2603.18489)

## 一句话摘要

Diffusion-based large language models (dLLMs) rely on bidirectional attention, which prevents lossless KV caching and requires a full forward pass at every denoising step.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion-based large language models (dLLMs) rely on bidirectional attention, which prevents lossless KV caching and requires a full forward pass at every denoising step. Existing approximate KV caching methods reduce this cost by selectively updating cached states, but their decision overhead scales with context length or model depth. We propose EntropyCache, a training-free KV caching method that uses the maximum entropy of newly decoded token distributions as a constant-cost signal for deciding when to recompute. Our design is grounded in two empirical observations: (1) decoded token entropy correlates with KV cache drift, providing a cheap proxy for cache staleness, and (2) feature volatility of decoded tokens persists for multiple steps after unmasking, motivating recomputation of the $k$ most recently decoded tokens. The skip-or-recompute decision requires only $O(V)$ computation per step, independent of context length and model scale. Experiments on LLaDA-8B-Instruct and Dream-7B-Instruct show that EntropyCache achieves $15.2\times$-$26.4\times$ speedup on standard benchmarks and $22.4\times$-$24.1\times$ on chain-of-thought benchmarks, with competitive accuracy and decision overhead accounting for only $0.5\%$ of inference time. Code is available at https://github.com/mscheong01/EntropyCache.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Minsoo Cheong, Donghyun Son, Woosang Lim, Sungjoo Yoo
- 发布：2026-11-03；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/mscheong01/EntropyCache](https://github.com/mscheong01/EntropyCache)
- 阅读深度：metadata
