---
title: "Norn: Context-Length-Aware Optimization of Weight and KV Cache Placement for Offloaded LLM Inference"
description: "Offloading model weights and the key-value (KV) cache to host memory enables large language models (LLMs) to run on a single memory-constrained GPU."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.32295) · [PDF](https://arxiv.org/pdf/2611.32295)

## 一句话摘要

Offloading model weights and the key-value (KV) cache to host memory enables large language models (LLMs) to run on a single memory-constrained GPU.

## 为什么值得关注

待编辑增强。

## 摘要原文

Offloading model weights and the key-value (KV) cache to host memory enables large language models (LLMs) to run on a single memory-constrained GPU. As the KV cache grows during decoding, GPU memory requirements and the costs of KV cache transfers and attention computation change. However, existing offloading methods generally use static computation assignments and placements of model weights and the KV cache, preventing them from adapting to these changes and degrading inference performance. We propose Norn, a context-length-aware offloaded LLM inference method. Based on offline profiling, Norn co-optimizes computation assignments and placements at the sublayer level, precomputing multiple execution plans and their switching points. During decoding, Norn switches plans as context length increases, overlapping computation and data transfers without knowing the output length in advance. For prefill, Norn employs operator-major chunked prefill to avoid repeated weight transfers and automatically selects the chunk size. Experiments with Qwen3-14B and Qwen3-32B on two single-GPU systems show up to a 16.8$\times$ speedup in end-to-end latency over Pipelined Sharding and a 4.2$\times$ speedup over its oracle variant with known input and output lengths.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Naoto Sugiura, Hiroki Matsutani
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
