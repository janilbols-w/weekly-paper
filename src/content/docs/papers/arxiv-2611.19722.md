---
title: "MIAO: Microscaling Intermediate Accumulation Optimization"
description: "Microscaling (MX) quantization enables lower-precision large language model (LLM) inference with limited accuracy degradation, reducing memory requirement and multiplication cost."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.19722) · [PDF](https://arxiv.org/pdf/2611.19722)

## 一句话摘要

Microscaling (MX) quantization enables lower-precision large language model (LLM) inference with limited accuracy degradation, reducing memory requirement and multiplication cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Microscaling (MX) quantization enables lower-precision large language model (LLM) inference with limited accuracy degradation, reducing memory requirement and multiplication cost. However, despite reduced operand precision, accumulation is often retained at high floating-point precisions, leaving a substantial hardware cost that operand quantization alone does not address. In particular, systolic arrays, as used in tensor accelerators such as Google TPU and AWS Trainium, distribute accumulation across distinct processing elements but conventionally use uniform accumulator precision throughout the array. This spatial organization offers an opportunity to reduce hardware cost by tailoring precision to individual accumulation stages. In this work, we present MIAO, a hardware-software co-design framework that jointly selects product precision and stage-dependent accumulator widths to minimize hardware area and energy cost under an end-to-end perplexity constraint. MIAO first calibrates MX block-scale shifts to reduce intermediate magnitudes while preserving operand quantization accuracy, then assigns narrower accumulators to earlier stages and progressively wider accumulators to later stages. To efficiently explore the resulting design space, MIAO combines hardware cost estimates derived from logic synthesis with a calibrated accuracy predictor to identify promising precision configurations, then validates the accuracy of promising candidates through bit-exact end-to-end LLM evaluation. Across MXFP8, MXFP6, and MXFP4, MIAO reduces processing element (PE) array area by up to 38.7% and energy by up to 36.1% relative to the all-BF16 accumulation baseline, with at most 1.60% additional perplexity degradation over operand-only MX quantization across six LLMs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: microscaling, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chloe Wong, Nicolas Rakela, Man Shi, Hansung Kim, Ruohan Richard Yan, Coleman Richard Charles Hooper, Yakun Sophia Shao
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
