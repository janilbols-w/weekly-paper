---
title: "Scaling Influence Functions in LLMs through Eigenbasis-Corrected One-Bit Gradient Projection"
description: "Influence functions estimate how individual training examples affect the behavior of large language models (LLMs)."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2609.37842v1) · [PDF](https://arxiv.org/pdf/2609.37842v1)

## 一句话摘要

Influence functions estimate how individual training examples affect the behavior of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Influence functions estimate how individual training examples affect the behavior of large language models (LLMs). Analyzing how training data influence different behaviors of an LLM involves repeated influence computation. Reusing stored training gradients reduces the computational cost, but storing full gradients is prohibitively expensive at LLM scale. We study how to compress these gradients while preserving influence estimates for future queries that are unknown at storage time. Through a worst-case analysis, we characterize the optimal fixed-dimensional linear representation and propose eigenbasis-corrected one-bit gradient projection (EOGP) to approximate it at scale. Specifically, EOGP uses EK-FAC to reduce gradient dimensionality, then applies PCA within the retained subspace to learn compression directions from the training gradients. We then apply one-bit quantization to the resulting coordinates, allowing more coordinates to be retained within a fixed storage budget. On GPT-2, EOGP predicts retraining outcomes more accurately than the evaluated compression baselines while using one-sixteenth of their per-example storage. On OLMo 2 SFT models from 1B to 32B parameters, EOGP remains competitive with the baselines allocated over 100 times as much storage per example.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jaeseung Heo, J Rosser, Dongwoo Kim
- 发布：2026-09-29；更新：2026-09-29
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
