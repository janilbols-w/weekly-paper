---
title: "XOR-Trellis: Ultra-Low-Complexity Dequantization and Curvature-Aware Hadamard-Free LLM Quantization"
description: "Trellis-coded quantization enables high-dimensional compression of large language model (LLM) weights at ultra-low bit widths without the exponentially large codebooks required by conventional vector quantization."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.00432) · [PDF](https://arxiv.org/pdf/2610.00432)

## 一句话摘要

Trellis-coded quantization enables high-dimensional compression of large language model (LLM) weights at ultra-low bit widths without the exponentially large codebooks required by conventional vector quantization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Trellis-coded quantization enables high-dimensional compression of large language model (LLM) weights at ultra-low bit widths without the exponentially large codebooks required by conventional vector quantization. Practical deployment, however, presents two challenges: reconstructing compressed weights at sufficient parallel throughput to avoid making dequantization an inference bottleneck, and maintaining quantization accuracy without costly incoherence transformations. We address these challenges with two complementary techniques. First, we introduce an ultra-low-complexity trellis dequantizer that uses a structured, hardware-efficient state-to-value mapping while preserving diverse reconstruction choices for trellis search. Second, we reformulate discrete trellis path optimization with a curvature-aware objective that reflects model sensitivity directly in the original coordinate space. Together, these techniques enable high-quality ultra-low-bit trellis quantization with inexpensive, highly parallel runtime reconstruction and without relying on Hadamard-based incoherence processing.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaofan Que, Nir Elkayam, Spandan Pyakurel, Shuokai Pan, Dibakar Gope
- 发布：2026-09-30；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
