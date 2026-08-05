---
title: "Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling"
description: "Large language model (LLM) serving spans diverse applications with stringent service-level objectives (SLOs), often requiring GPUs to run at maximum frequencies and increasing energy consumption."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.01891) · [PDF](https://arxiv.org/pdf/2608.01891)

## 一句话摘要

Large language model (LLM) serving spans diverse applications with stringent service-level objectives (SLOs), often requiring GPUs to run at maximum frequencies and increasing energy consumption.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving spans diverse applications with stringent service-level objectives (SLOs), often requiring GPUs to run at maximum frequencies and increasing energy consumption. Existing energy-management approaches adapt GPU frequencies only at the request or inference-phase level, overlooking operator-level differences in frequency sensitivity between Attention and feed-forward networks (FFNs). We find that the energy-optimal frequencies of Attention and FFN (A/F) differ and vary with the inference phase, workload, and system configurations. However, runtime variability and independent A/F frequency control create a large search space and high communication overhead. To address these challenges, we present AFlex, a framework that jointly optimizes resource provisioning and GPU frequency scaling for disaggregated A/F serving. AFlex introduces a global scheduler and a local operator-level dynamic voltage and frequency scaling (DVFS) controller to determine A/F resource allocations and frequencies. It further introduces an interleaved A/F pipeline with dynamic microbatch depth and adaptive request batching to reduce pipeline bubbles. We implement AFlex in SGLang and evaluate it on NVIDIA A800 GPUs using Qwen3-32B and Mixtral-8$\times$7B under production Conversation and Coding traces. \AFlex reduces energy per token by up to 49\% over state-of-the-art disaggregated serving and 48\% over frequency-scaling systems while satisfying TTFT and TPOT SLOs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Cunchen Hu, Liangliang Xu, Tian Liu, Min Lyu, Yongkun Li, Sa Wang, Shuo Quan, Yanan Yang, Wenda Tang, Yiduo Wang, Fu Yu, Jie Wu
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
