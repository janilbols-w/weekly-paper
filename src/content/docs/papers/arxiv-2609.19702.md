---
title: "Understanding and Exploiting Diagonal Attention Sparsity in Autoregressive Image Generation"
description: "Autoregressive image generation has emerged as a paradigm for multimodal AI systems due to its compatibility with transformer-based LLM serving infrastructures."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.19702) · [PDF](https://arxiv.org/pdf/2609.19702)

## 一句话摘要

Autoregressive image generation has emerged as a paradigm for multimodal AI systems due to its compatibility with transformer-based LLM serving infrastructures.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive image generation has emerged as a paradigm for multimodal AI systems due to its compatibility with transformer-based LLM serving infrastructures. However, generating thousands of visual tokens per request makes decoding increasingly bottlenecked by KV cache accesses during attention computation. Sparse attention is particularly attractive for this workload because many visual generation applications tolerate moderate quality degradation in exchange for improved performance and efficiency. While sparse attention has been extensively explored for text-based LLM inference, it remains unclear whether its sparsity assumptions generalize effectively to autoregressive image generation. We present the first systematic characterization of attention sparsity in autoregressive image generation across diverse workloads and representative open-source models. Our analysis reveals several distinguishing properties, including a pronounced prefill-decode asymmetry, strong attention concentration on prompt and local tokens, and a unique diagonal attention sparsity pattern arising from the spatial locality of visual tokens. Motivated by these observations, we propose a diagonal-aware sparse attention mechanism that selectively skips KV entries along the diagonal attention direction within a recent window. Implemented on top of a GPU-based serving system using FlexGen, FlashAttention-2, and custom kernels, our approach achieves up to 3.1x throughput and 1.19x latency improvements with less than 2% quality degradation compared to dense inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Daeun Kim, Junwha Hong, Changhun Oh, Yoonsung Kim, Yoonhyeong Lee, Jongse Park
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
