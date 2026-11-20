---
title: "Splice-Core: Low-Order-Bit-Splicing GEMM for Highly Energy-Efficient AI Inference Accelerators"
description: "Splice-Core is a temporal-unary/binary (tub) hybrid general matrix multiplication (GEMM) unit that minimizes low-order accumulation latency, while retaining value-dependent execution for high-order activation bits."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2611.25617v1) · [PDF](https://arxiv.org/pdf/2611.25617v1)

## 一句话摘要

Splice-Core is a temporal-unary/binary (tub) hybrid general matrix multiplication (GEMM) unit that minimizes low-order accumulation latency, while retaining value-dependent execution for high-order activation bits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Splice-Core is a temporal-unary/binary (tub) hybrid general matrix multiplication (GEMM) unit that minimizes low-order accumulation latency, while retaining value-dependent execution for high-order activation bits. We present two novel processing element (PE) variants: (i) Splice-BP utilizing bit planes, and (ii) Splice-LUT, which selects a shared weight multiple in a single cycle. Compared to a binary systolic array, Splice-BP/Splice-LUT achieve 77.4%/76.4% geometric-mean tile energy reductions, respectively, across 26 INT4 convolutional neural network (CNN) and large language model (LLM) workloads in 45nm. Splice-LUT further increases geometric-mean tile throughput by 44.4% and reduces geometric-mean energy-delay product (EDP) by 6.13x across the 26 configurations. Across the evaluated W8A8 convolution and expert-projection workloads, Splice-BP and Splice-LUT reduce tile energy by 77.3-88.1%. Post-place-and-route INT4 yields 14%/9% smaller area for Splice-BP/Splice-LUT, compared to the systolic array.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Prabhu Vellaisamy, Hsien-Fu Hung, Andrew Kim, Shawn Blanton, John Paul Shen
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
