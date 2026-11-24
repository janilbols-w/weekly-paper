---
title: "BitPrefill: W1.58A4 Tensor-Core Acceleration for Compute-Bound LLM Prefill"
description: "Low-bit quantization reduces large language model (LLM) inference cost, yet implementations optimized for memory-bound decode can leave compute-bound prefill on BF16 tensor cores."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.26657) · [PDF](https://arxiv.org/pdf/2611.26657)

## 一句话摘要

Low-bit quantization reduces large language model (LLM) inference cost, yet implementations optimized for memory-bound decode can leave compute-bound prefill on BF16 tensor cores.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit quantization reduces large language model (LLM) inference cost, yet implementations optimized for memory-bound decode can leave compute-bound prefill on BF16 tensor cores. This gap matters for input-heavy workloads, including long-context and multimodal applications, where prefill can account for a substantial fraction of inference latency. We propose a W1.58A4 operator that quantizes weights to ternary values and activations to 4-bit, while executing the linear projection on native INT4 general matrix multiply (GEMM) tensor cores, turning prefill from a full-precision matrix multiply into a low-bit one. We deploy the operator for BitNet-b1.58 on a single RTX 4090 and a Jetson Orin Nano edge device, and report GEMM-kernel latency, end-to-end LLMs prefill latency, and task accuracy against bf16 and BitNet/BitBLAS baselines. Our proposed kernel achieves ~1.42x acceleration compared to the original BF16 prefill phase, with negligible reduction on model accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Fang Chen, Xuming Chen, Sanmukh Kuppannagari, Gourav Datta
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
