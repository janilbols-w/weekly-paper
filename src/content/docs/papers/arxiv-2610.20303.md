---
title: "SpectrumQuant: Spectrum Alignment for LLM Quantization"
description: "Orthogonal transforms have emerged as an effective tool for low-bit quantization of large language models (LLMs), as they reshape activation distributions without changing the underlying model function."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.20303) · [PDF](https://arxiv.org/pdf/2610.20303)

## 一句话摘要

Orthogonal transforms have emerged as an effective tool for low-bit quantization of large language models (LLMs), as they reshape activation distributions without changing the underlying model function.

## 为什么值得关注

待编辑增强。

## 摘要原文

Orthogonal transforms have emerged as an effective tool for low-bit quantization of large language models (LLMs), as they reshape activation distributions without changing the underlying model function. Existing approaches typically rely either on fixed data-agnostic transforms, such as Hadamard rotations, or on calibration-time optimization of learned rotations. We study rotation selection from first principles and show that maximizing covariance leads to spectral alignment and provides a principled criterion for constructing quantization-friendly orthogonal transforms. Based on this insight, we propose SpectrumQuant, a closed-form rotation method that estimates activation covariance from calibration data and uses it to construct a covariance-aware orthogonal transform for post-training quantization. Our formulation characterizes quantization-friendly rotations as compositions of alignment and mixing components, while recovering Hadamard matrices as a special case. Interestingly, a class of butterfly matrices belongs to this category. In the realm of LLM quantization, SpectrumQuant bridges the gap between data-agnostic structured rotations and learned rotations, providing an effective and efficient data-aware alternative for post-training quantization. Experiments on Llama and Mistral models show that SpectrumQuant is competitive with state-of-the-art rotation strategies while requiring less than one-third of the GPU memory and significantly less time than learned rotations approaches like SpinQuant and DartQuant.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dwaipayan Haldar, Indranil Patra, Azhar Yousuf, Chandra Sekhar Seelamantula
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
