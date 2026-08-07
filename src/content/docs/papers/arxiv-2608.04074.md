---
title: "Spend Bits Where Queries Look: KV Cache Vector Quantization with Attention-Preserving Transforms"
description: "Long-context LLM decoding reads the key-value (KV) cache at every step."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.04074) · [PDF](https://arxiv.org/pdf/2608.04074)

## 一句话摘要

Long-context LLM decoding reads the key-value (KV) cache at every step.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM decoding reads the key-value (KV) cache at every step. Loading it takes longer than computing attention over it, so throughput is bandwidth-bound. Hence, reducing the cache size can raise both decoding speed and serving capacity. The challenge is to reduce cache size while preserving the attention products, keeping reconstruction cheap, and using a fixed per-token bit count. At two bits per element, the most competitive methods rely on orthogonal transforms. However, existing techniques are either data-oblivious or use the query statistics without deriving the transform from a distortion criterion. Moreover, they rely on transforms built on top of random or Hadamard rotations, which equalize variances across entries rather than compacting energy, and fixed-width scalar quantizers, which are suboptimal at low rates. In this paper, we formulate KV cache quantization as a transform coding problem in which distortion is the error in the attention products. We derive closed-form optimal transforms for keys and values from calibration statistics, under a high-resolution model. We show that the optimal key transform is not orthogonal and satisfies a generalized Parseval relation: the attention-aware distortion becomes mean-squared error (MSE) in the transform domain. Thus, we can use MSE-optimal vector quantizers applied directly to the transformed key coefficients. To meet the fixed-width layout requirement, we show that grouping coefficients into equal-volume partitions makes equal-size codebooks attain the variable-rate optimum under the same high-resolution model. At two bits per element, our method, termed NOVA-KV, recovers most of the long-context retrieval accuracy lost by scalar quantization methods at comparable throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Samuel Fernández-Menduiña, Amir Ziashahabi, Eduardo Pavez, Antonio Ortega, Salman Avestimehr
- 发布：2026-08-04；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
