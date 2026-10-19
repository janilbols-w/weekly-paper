---
title: "BS-Spec: BFP-Based Bit-Sharing for Self-Speculative LLM Decoding with LUT-Driven Mixed-Precision Acceleration"
description: "As large language models (LLMs) are increasingly deployed across diverse inference services, serving workloads span a wide range of batch sizes, context lengths, and performance requirements."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.22877) · [PDF](https://arxiv.org/pdf/2610.22877)

## 一句话摘要

As large language models (LLMs) are increasingly deployed across diverse inference services, serving workloads span a wide range of batch sizes, context lengths, and performance requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) are increasingly deployed across diverse inference services, serving workloads span a wide range of batch sizes, context lengths, and performance requirements. Speculative decoding improves inference throughput, but conventional approaches require a separate draft model and KV cache, while existing self-speculative methods suffer from workload-insensitive draft configurations and inefficient mixed-precision execution. In this paper, we present BS-Spec, a block floating point (BFP)-based bit-sharing framework that jointly optimizes draft construction, workload-aware precision selection, and hardware execution. BS-Spec derives multiple draft representations directly from a single BFP target model by partially loading the most significant bits of weights and the KV cache while preserving shared exponents, eliminating separate draft-model storage. Offline calibration selects the weight and KV-cache precision pair that maximizes estimated speedup for each serving regime, and a precision lookup table applies the selected configuration at runtime. To support this adaptive execution, we design a mixed-precision BFP accelerator with a lookup table (LUT)-based variable-precision datapath for both draft and target computation. Experimental results show that BS-Spec achieves up to $1.9\times$ speedup over conventional autoregressive decoding and improves speedup over the evaluated bit-sharing self-speculative decoding baselines by $67.2\%$ on average, demonstrating the benefits of jointly co-designing bit sharing, precision adaptation, and specialized hardware for diverse LLM serving workloads.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiwoo Kim, Gunho Park, Sunwoo Yoo, Baeseong Park, Dongsoo Lee, Youngjoo Lee
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
