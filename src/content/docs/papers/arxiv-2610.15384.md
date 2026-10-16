---
title: "E8 Lattice Key Quantization for Low-Bit KV-Cache Compression"
description: "Compressing the key-value (KV) cache is essential for serving long-context large language models (LLMs) under memory constraints."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.15384v1) · [PDF](https://arxiv.org/pdf/2610.15384v1)

## 一句话摘要

Compressing the key-value (KV) cache is essential for serving long-context large language models (LLMs) under memory constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Compressing the key-value (KV) cache is essential for serving long-context large language models (LLMs) under memory constraints. While current scalar quantization methods achieve significant compression, they typically face a quality-fidelity trade-off, either suffering from performance instability at 2-bit precision or necessitating 3-bit keys to maintain model quality. In this work, we demonstrate that a uniform low-bit k2v2 configuration (2-bit keys and 2-bit values) can preserve near-baseline quality by using vector quantization (VQ) based on the $E_8$ lattice for KV keys. We show that structured VQ exploits correlations across adjacent dimensions to achieve signal-to-quantization-noise ratios (SQNR) higher than those of independent scalar quantization at the same key payload rate. To ensure practical utility, we adapt a table-based asymmetric scoring algorithm that avoids explicit codebook dequantization during attention computation and preserves decode-throughput parity with scalar baselines. Across five LLM families, our $E_8$ k2v2 approach yields \textasciitilde$6\times$ KV compression, roughly 20\% smaller than scalar k3v2 (3-bit keys and 2-bit values), while retaining near-baseline long-context perplexity. In our full-suite perplexity evaluation, $E_8$ improves over scalar k3v2 in 80\% of model--dataset--context settings. These results indicate that $E_8$ lattice VQ improves quality per byte while keeping throughput at parity, suggesting that structured key quantization is a useful primitive for KV-compression stacks. Overall, our work provides a low-overhead primitive for expanding the quality-memory frontier in long-context LLM inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sasho Nedelkoski, Alexander Acker, Soeren Becker, Dominik Scheinert, Odej Kao
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
