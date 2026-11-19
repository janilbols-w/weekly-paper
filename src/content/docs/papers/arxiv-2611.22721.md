---
title: "HADVQ: Hessian Aware Directional Vector Quantization"
description: "Ultra-low-bit quantization of large language models is a challenging task because aggressive compression severely distorts model parameters and disproportionately harms a small number of highly sensitive channels."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.22721) · [PDF](https://arxiv.org/pdf/2611.22721)

## 一句话摘要

Ultra-low-bit quantization of large language models is a challenging task because aggressive compression severely distorts model parameters and disproportionately harms a small number of highly sensitive channels.

## 为什么值得关注

待编辑增强。

## 摘要原文

Ultra-low-bit quantization of large language models is a challenging task because aggressive compression severely distorts model parameters and disproportionately harms a small number of highly sensitive channels. We present a vector quantization method tailored for this regime. Our approach begins with random preconditioning, which regularizes the weight space and makes it more amenable to quantization. We then represent weights in polar coordinates and decouple the quantization of directions and magnitudes. To quantize directions, we leverage the structure induced by random preconditioning and design a structured codebook based on the $E_8$ lattice, yielding a compact yet expressive representation. To further reduce degradation, we detect extremely important channels using a proxy Hessian and preserve them with an additional cost of only 0.16 bits. Together, these components provide an effective quantization pipeline for LLMs in the extremely low-bit regime. Empirical results demonstrate improved accuracy, highlighting the benefit of combining geometric structure, lattice-based codebooks, and selective channel preservation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Daniil Li, Mars Davletshin, Vadim Klyzhenko, Artem Danilishin, Valery Sandul, Daniil Ryazanov, Ekaterina Muravleva
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
