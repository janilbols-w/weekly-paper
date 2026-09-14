---
title: "Attention Quantization for Tabular Foundation Models"
description: "With the recent rise and adoption of tabular foundation models, optimizing their inference performance becomes an emerging field for efficiency research."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.13031) · [PDF](https://arxiv.org/pdf/2609.13031)

## 一句话摘要

With the recent rise and adoption of tabular foundation models, optimizing their inference performance becomes an emerging field for efficiency research.

## 为什么值得关注

待编辑增强。

## 摘要原文

With the recent rise and adoption of tabular foundation models, optimizing their inference performance becomes an emerging field for efficiency research. While the models are architecturally similar to transformer-based large language models (LLMs), the size and serving patterns differ significantly. We show that the focus should be on the attention calculation and less on weight or KV cache quantization, which are more popular in LLMs. We develop a quantization strategy for queries, keys, and values to FP8 and use explicit FP8 matrix multiplication instructions to speed up the attention calculation. We find that it is crucial to align the quantization error in the test rows with the quantization error in the training rows, as otherwise the accuracy drops drastically. Our Triton kernel achieves a speedup up to 1.7x over regular 16-bit kernels, and we show that on TabPFN-v3 and TabICLv2 there is no relevant accuracy loss across TabArena and BeyondArena.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jonas M. K\"ubler, Benjamin J\"ager, Klemens Fl\"oge, Noah Hollmann, Frank Hutter
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
