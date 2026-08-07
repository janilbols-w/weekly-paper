---
title: "Decomposed Entailment for Factuality Checking and Hallucination Detection"
description: "The reliability of Large Language Models (LLMs) is often compromised by factual inconsistencies, including hallucinations---cases where generated content is not supported by the underlying source."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.05823) · [PDF](https://arxiv.org/pdf/2608.05823)

## 一句话摘要

The reliability of Large Language Models (LLMs) is often compromised by factual inconsistencies, including hallucinations---cases where generated content is not supported by the underlying source.

## 为什么值得关注

待编辑增强。

## 摘要原文

The reliability of Large Language Models (LLMs) is often compromised by factual inconsistencies, including hallucinations---cases where generated content is not supported by the underlying source. We present HallDetect, a lightweight, reference-free, and black-box framework for hallucination detection that we evaluate not only on summarization but across a broader range of source-grounded generation settings. HallDetect builds on decomposition-based factuality evaluation: generated content is decomposed into atomic claims, each verified by a compact encoder-based entailment model through a contrastive formulation over a multi-scale library of source chunks, and aggregated with an asymmetric score in which a single confidently contradicted claim flags the response. Under a controlled protocol in which all methods share the same 4-bit quantized backbones and consumer-grade hardware budget, HallDetect outperforms comparably resourced generative and embedding-based baselines on three of four benchmarks while remaining stable across backbone families, and yields a claim-to-span audit trail that localizes each error.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Achir Oukelmoun, Nasredine Semmar, Gaël De Chalendar
- 发布：2026-08-06；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
