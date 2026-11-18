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

Generative AI is billed per token, yet tokens are not equally expensive. Each token enters the KV-cache and raises the cost of those that follow, so energy grows non-linearly along a sequence whose tokens look identical. No analytical model states what a token costs without per-LLM fitting, and no law names the factors that set it. From closed-form expressions of LLM inference's computational and memory-access complexity, we derive the SIMPLE Inference Model to Predict LLMs Energy (SIMPLE), a four-parameter law that separates prefill from decode, and decode into KV-cache and next-token computation cost. Over traces of 13 dense LLMs from several families on NVIDIA H100 GPUs, it attains R2 = 0.969 and 11.97% MAPE, 3.1-3.5x below the SOTA, without per-LLM calibration. SIMPLE explains as well as predicts: prefill energy grows quadratically with hidden dimension, so larger LLMs suffer most from long inputs; and higher GQA KV grouping reduces the per-token energy linearly relative to standard MHA. Increasing the reasoning token budget pushes output length beyond the analytically derived energy minimum, driving super-linear energy growth; accuracy rises but energy rises faster, so Intelligence per Joule peaks at an intermediate budget and falls by up to 3.14x across a 4.0x range. Moving to agentic serving raises energy per request by 13.0x, as both prefill and KV-cache terms grow with input length; prefix caching removes most of the prefill cost (-93%), but not KV-cache cost, so even a cached agentic request costs 4.8x more.

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
- 发布：2026-11-03；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
