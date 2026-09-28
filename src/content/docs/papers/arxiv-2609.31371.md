---
title: "Towards Understanding LLM-Based Log Anomaly Detection: An Empirical Study of Performance, Efficiency, and Robustness"
description: "Large language models (LLMs) have demonstrated promising performance in log anomaly detection, yet how their adaptation strategies, architectures, and deployment configurations affect detection effectiveness remains insufficiently understood."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.31371) · [PDF](https://arxiv.org/pdf/2609.31371)

## 一句话摘要

Large language models (LLMs) have demonstrated promising performance in log anomaly detection, yet how their adaptation strategies, architectures, and deployment configurations affect detection effectiveness remains insufficiently understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have demonstrated promising performance in log anomaly detection, yet how their adaptation strategies, architectures, and deployment configurations affect detection effectiveness remains insufficiently understood. To investigate these factors, we conduct a systematic empirical analysis across three public log datasets, examining different adaptation strategies, model architectures, parameter scales, and quantization settings. Our results reveal substantial performance differences across adaptation strategies, while model scaling yields varying detection gains across datasets. We further observe that models with comparable detection accuracy can exhibit markedly different computational costs, and that low-bit quantization largely preserves detection performance in the evaluated configurations. Finally, we examine detection robustness under structural, semantic, and label noise at different perturbation levels. These findings provide empirical insights into the performance, efficiency, and robustness of LLM-based log anomaly detection, highlighting practical considerations beyond conventional accuracy-oriented evaluation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bin Li, Dongdong Wang, Siyang Lu
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
