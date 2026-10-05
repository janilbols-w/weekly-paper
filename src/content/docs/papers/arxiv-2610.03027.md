---
title: "Tailoring the Quantization Space for 1-Bit KV Cache Compression"
description: "The key-value (KV) cache becomes a major memory bottleneck in long-context LLM inference, placing substantial pressure on memory capacity and bandwidth."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.03027) · [PDF](https://arxiv.org/pdf/2610.03027)

## 一句话摘要

The key-value (KV) cache becomes a major memory bottleneck in long-context LLM inference, placing substantial pressure on memory capacity and bandwidth.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache becomes a major memory bottleneck in long-context LLM inference, placing substantial pressure on memory capacity and bandwidth. To mitigate this bottleneck, vector quantization (VQ) has emerged as a promising approach for aggressive KV cache compression. However, existing VQ methods degrade substantially in the 1-bit regime. At such extreme compression, each codebook must represent a larger group of channels with a limited set of centroids, making effective use of its capacity increasingly challenging. To address this, we introduce $\textbf{TaSQ}$, which tailors the VQ target space by combining query-guided channel weighting, cross-head normalization, and covariance-aware channel grouping to better reflect the error sensitivity and statistical structure of cached activations. Since these transforms are RoPE-compatible and can be easily merged into projection weights and codebooks, TaSQ preserves the conventional VQ lookup structure and adds negligible serving overhead. Across general, long-chain-of-thought reasoning, and long-context retrieval benchmarks, TaSQ consistently outperforms existing low-bit KV cache VQ baselines while preserving reasoning stability. On a single RTX 6000 Ada GPU, its SGLang implementation supports up to $14\times$ larger batch sizes and achieves $1.87\times$ higher peak throughput compared to the BF16 baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Minsoo Cheong, Donghyun Son, Sungjoo Yoo
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
