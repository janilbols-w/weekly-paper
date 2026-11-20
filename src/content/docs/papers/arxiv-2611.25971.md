---
title: "Kameleo: In-Situ Activation-Precision Selection for Bit-Serial LLM Accelerators"
description: "Weight-only quantization keeps the activations of large language models (LLMs) in a higher-precision format, pushing the on-chip inference cost to the activation arithmetic."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](http://arxiv.org/abs/2611.25971v1) · [PDF](https://arxiv.org/pdf/2611.25971v1)

## 一句话摘要

Weight-only quantization keeps the activations of large language models (LLMs) in a higher-precision format, pushing the on-chip inference cost to the activation arithmetic.

## 为什么值得关注

待编辑增强。

## 摘要原文

Weight-only quantization keeps the activations of large language models (LLMs) in a higher-precision format, pushing the on-chip inference cost to the activation arithmetic. Bit-serial, variable-length accelerators offer a promising path to reduce this cost by lowering activation precision while preserving model quality. They process only the mantissa bits that each layer needs. The length has to be chosen per layer and operator, and today it is chosen by offline calibration: a search driven by the perplexity of the full model on a representative dataset. The search is repeated for every model and workload, and its result degrades silently on other data. This paper presents Kameleo, an accelerator that selects the activation precision at runtime, on the accelerator, from the data it is processing. Kameleo replaces the global perplexity by a local proxy that compares the output of each GEMM at reduced and at full precision. It exploits the fact that a bit-serial datapath produces this comparison almost for free, because the reduced-precision result is an intermediate state of the full-precision computation. Two passes over the first tokens of a workload set the precision of every GEMM. On four LLMs and seven datasets, Kameleo stays within a 1% perplexity budget at a 2.11-2.34x reduction of prefill cycles on the matrix multiplication unit (MXU), close to the reduction of configurations calibrated offline on the evaluation data itself. Calibrated configurations transferred to other data, in contrast, often violate the budget. The selection hardware adds only 3.7% to the accelerator area. Kameleo thereby makes variable-length mantissas feasible in real deployments, where offline calibration for every model and workload is not.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Robin Geens, Thomas Debelle, Marian Verhelst, Chao Fang
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
