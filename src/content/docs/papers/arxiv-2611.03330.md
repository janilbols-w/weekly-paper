---
title: "The SIMPLE Law for Energy Cost of LLM Inference"
description: "Generative AI is billed per token, yet tokens are not equally expensive."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.03330) · [PDF](https://arxiv.org/pdf/2611.03330)

## 一句话摘要

Generative AI is billed per token, yet tokens are not equally expensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Generative AI is billed per token, yet tokens are not equally expensive. Each token enters the KV-cache and raises the cost of those that follow, so energy grows non-linearly along a sequence whose tokens look identical. No analytical model states what a token costs, and the most accurate SOTA model is a fit, not a law: it absorbs architecture into fitted coefficients, requiring per-LLM fitting. We derive closed-form expressions of the computational and memory-access complexity of LLM inference in terms of architectural hyperparameters, covering MHA and GQA, and compare a family of analytical models of increasing granularity. From these, we obtain the SIMPLE Inference Model to Predict LLMs Energy (SIMPLE), a four-parameter law that separates prefill from decode, and decode into KV-cache cost and next-token computation. Over traces of 13 dense LLMs from six families on NVIDIA H100 GPUs, it attains R2 = 0.969 and 11.97% MAPE, 3.1-3.5x below the SOTA, without per-LLM calibration. The SIMPLE law explains as well as predicts: prefill energy grows quadratically with the hidden dimension, so larger LLMs suffer most from long inputs; and more aggressive GQA KV grouping reduces the per-token energy by up to 3x relative to standard MHA. Increasing the reasoning token budget pushes output length beyond the analytically derived energy minimum, driving super-linear energy growth; although accuracy grows with the budget, energy grows faster, so Intelligence per Joule peaks at an intermediate budget and falls by up to 3.14x across a 4.0x reasoning-budget range. Agentic serving raises energy per request by 13.0x relative to non-agentic ones, driven by the growth of both the prefill and the KV-cache terms with input length; while prefix caching removes most of the prefill cost (-93%), the KV-cache term is unaffected, so even a cached agentic request costs 4.8x more.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache, prefix caching
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hiari Pizzini Cavagna, Andrea Proia, Daniele Cesarini, Zeynep Kiziltan, Andrea Bartolini
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
