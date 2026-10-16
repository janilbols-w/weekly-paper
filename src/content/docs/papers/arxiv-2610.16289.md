---
title: "Fast Quantized Johnson$-$Lindenstrauss Transforms"
description: "Quantization has emerged as one of the primary techniques for reducing the memory footprint of large language models during inference."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.16289v1) · [PDF](https://arxiv.org/pdf/2610.16289v1)

## 一句话摘要

Quantization has emerged as one of the primary techniques for reducing the memory footprint of large language models during inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization has emerged as one of the primary techniques for reducing the memory footprint of large language models during inference. A prominent example is Quantized Johnson$-$Lindenstrauss (QJL), which compresses KV caches using 1-bit asymmetric quantization while approximately preserving the inner products required by the attention mechanism. Recent theoretical and practical work aims at replacing the dense Gaussian projections used by the aforementioned transforms with more structured embeddings $-$ such as compositions of randomized Hadamard transforms $-$ while retaining the same embedding dimension. In this paper, we introduce two constructions based on a composition of randomized Hadamard transforms, albeit with a Gaussian rather than Rademacher diagonal in the second stage. The first adds Gaussian dithering to smooth the quantizer, while the second inserts a random permutation to regularize the covariance structure of the resulting Gaussian measurements. We prove embedding-dimension and running-time guarantees analogous to those of Fast JL in the non-quantized setting. The first construction achieves $m=O(\varepsilon^{-2}\log^2(d/δ))$, while the second achieves $m=O(\varepsilon^{-2}\log(d/δ))$ under a restriction on $m$. Both constructions can be applied in $O(d\log d)$ time.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Angelos Korakitis, Vasileios Nakos
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
