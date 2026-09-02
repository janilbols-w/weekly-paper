---
title: "QABBA: Symbolic Time-Series Compression via Integer-Quantized Aggregation"
description: "The expansion of time-series data from sensors and monitoring systems has made compact representations increasingly important."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2411.15209) · [PDF](https://arxiv.org/pdf/2411.15209)

## 一句话摘要

The expansion of time-series data from sensors and monitoring systems has made compact representations increasingly important.

## 为什么值得关注

待编辑增强。

## 摘要原文

The expansion of time-series data from sensors and monitoring systems has made compact representations increasingly important. Such representations should retain signal structure while cutting storage, transmission and computation costs. Adaptive Brownian Bridge-based Aggregation (ABBA) addresses this need by converting long numerical series into short symbolic sequences, but reductions in parameter storage and computational precision remain desirable. We propose Quantized ABBA (QABBA), a quantized version of ABBA. By quantizing the symbolic centers, QABBA reduces the parameter footprint and enables integer arithmetic while maintaining high reconstruction quality. We establish several error bounds for the additional approximation introduced by quantization: a dimension-free bound on the excess error of each segment, a time-domain reconstruction-error bound, a stability condition for symbolic assignment, and a rule for allocating bits between segment lengths and increments. The resulting symbolic strings can be passed directly to a pretrained large language model (LLM) without any extra time-series embedding layer. Experiments on the Monash regression archive, UCR Time Series Classification Archive, and UEA Multivariate Time Series Classification Archive demonstrate a practical trade-off among storage, reconstruction accuracy and downstream predictive performance. QABBA therefore provides an error-controlled, low-precision symbolic representation for time-series compression and LLM-based analysis.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Erin Carson, Xinye Chen, Fei He, Cheng Kang
- 发布：2026-08-26；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/inEXASCALE/qabba](https://github.com/inEXASCALE/qabba)
- 阅读深度：metadata
