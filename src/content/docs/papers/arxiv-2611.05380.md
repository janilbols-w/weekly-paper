---
title: "VAR-Q: Tuning-free KV Cache Quantization for Visual Autoregressive Image and Video Generation"
description: "Visual autoregressive generation spans two dominant paradigms: next-scale prediction for images and video, and next-frame prediction for video."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.05380) · [PDF](https://arxiv.org/pdf/2611.05380)

## 一句话摘要

Visual autoregressive generation spans two dominant paradigms: next-scale prediction for images and video, and next-frame prediction for video.

## 为什么值得关注

待编辑增强。

## 摘要原文

Visual autoregressive generation spans two dominant paradigms: next-scale prediction for images and video, and next-frame prediction for video. Both decode block-by-block rather than token-by-token, yielding KV caches whose statistics diverge from those of language models. At scale, KV memory exceeds the weights and limits large-scale deployment caused by a large amount of visual tokens. Our analysis of these caches reveals three findings. First, a small set of massive-value channels carries the functional load: ablating these outlier channels collapses generation, whereas ablating a matched set of inlier channels leaves quality intact. Second, the outliers organize along two axes, feature and block, with magnitudes persistent within each cell and shifting across cells. Third, this structure arises from two independent mechanisms: projection bias and RoPE-induced scattering. Guided by these findings, we propose VAR-Q, a tuning-free KV-cache quantization framework that groups along the same two axes. The generation loop provides block boundaries for free, removing the need for outlier detection or calibration. Paired with bit-packing kernels for runtime memory reduction, VAR-Q delivers low-bit quantization across nine models spanning both paradigms, cutting KV memory by up to 78.5% with negligible quality degradation and enabling 6x larger inference batches.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Boxun Xu, Jiaji Lu, Yuxuan Yin, Zihu Wang, Ziyue Liu, Yu Wang, Zirui Liu, Peng Li
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
