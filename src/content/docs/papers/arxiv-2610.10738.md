---
title: "Lossy Compressive Text Autoencoders"
description: "Our work explores learning a compressed latent representation of text, at the intersection of data compression and representation learning."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.10738) · [PDF](https://arxiv.org/pdf/2610.10738)

## 一句话摘要

Our work explores learning a compressed latent representation of text, at the intersection of data compression and representation learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Our work explores learning a compressed latent representation of text, at the intersection of data compression and representation learning. We propose an autoencoder architecture that performs residual downscaling and upscaling of hidden representations along the time axis, with a residual low-dimension discrete bottleneck. We analyze our approach for different quantization methods, training objectives, and datasets. For different levels of compression, we evaluate the similarity between the original and reconstructed text both at the surface-level (BLEU) and at the semantic-level (LLM-based judge). Additionally, we evaluate our models on downstream question-answering and semantic text similarity benchmarks. Our approach results in compressed representations which are on par with lossless text compression algorithms at 2.24 bits per byte on web text data, while having good reconstruction and downstream task performance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vinko Sabol\v{c}ec, Angelos Katharopoulos, David Grangier
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
