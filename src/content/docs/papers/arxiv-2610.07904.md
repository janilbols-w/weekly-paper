---
title: "ApexQuant: Data-Free Elastic Quantization by Residual Re-Isotropization"
description: "We introduce ApexQuant, a calibration-free quantization method that recursively re-quantizes the residual error, serving as a refinement layer on top of existing quantizers."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.07904) · [PDF](https://arxiv.org/pdf/2610.07904)

## 一句话摘要

We introduce ApexQuant, a calibration-free quantization method that recursively re-quantizes the residual error, serving as a refinement layer on top of existing quantizers.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce ApexQuant, a calibration-free quantization method that recursively re-quantizes the residual error, serving as a refinement layer on top of existing quantizers. We establish that a fresh random rotation returns each residual to the uniform distribution on the hypersphere, which characterizes the rate of progressive error decay across successive passes. This result lets us determine, before any weight is read, how many passes a layer needs for a target weight-space error. Every prefix is itself a valid lower-rate model, so one artifact serves several precisions. We instantiate ApexQuant with three interchangeable stages, scalar, $E_8$ and trellis, and validate it on four open-weight LLMs and on Earth-observation and medical domains where in-distribution data is often unattainable as imagery arrives under restrictive licences or due to patient material under privacy constraints. Progressive re-isotropization comes within a few percent of full precision at four bits and gives the best two-bit arm we measure, in a completely data-free setting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Aksel Fristrup, Sumit Pandey, Ankit Kariryaa
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
