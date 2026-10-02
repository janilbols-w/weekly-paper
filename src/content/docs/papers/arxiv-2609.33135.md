---
title: "MpFA: Hardware-Efficient Train-Free QK4V8 FlashAttention Kernels on Blackwell GPUs"
description: "Long-context LLM inference pushes modern GPU serving stacks into an attention-bound regime, where both compute and memory are dominated by the softmax-GEMM pipeline."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2609.33135v1) · [PDF](https://arxiv.org/pdf/2609.33135v1)

## 一句话摘要

Long-context LLM inference pushes modern GPU serving stacks into an attention-bound regime, where both compute and memory are dominated by the softmax-GEMM pipeline.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM inference pushes modern GPU serving stacks into an attention-bound regime, where both compute and memory are dominated by the softmax-GEMM pipeline. On NVIDIA Blackwell GPUs, FP4 Tensor Cores offer high matmul throughput, but we find that fully FP4 attention often fails to translate this throughput into end-to-end speedups due to non-matmul costs: online quantization after softmax, tensor/shared-memory data movement, and contention on the softmax path. We present MpFA, a training-free FlashAttention kernel optimized for Blackwell. Guided by hardware characterization, MpFA uses mixed precision: NVFP4 for QK and FP8 for PV (QK4PV8). This preserves low-bit QK throughput while avoiding the conversion and scaling overheads of FP4 PV. To recover accuracy without further stressing the softmax pipeline, MpFA introduces rank-one smoothing compensation implemented as an additional Tensor Core MMA. MpFA further improves performance with a fine-grained asynchronous pipeline, tensor-memory reuse, and adaptive parallel partitioning across prefill and decode. On an NVIDIA B200 and across 16K-128K contexts, MpFA improves prefill throughput over state-of-the-art BF16/FP8 baselines and increases end-to-end output throughput by 2.81$\times$ over BF16 FA4 across Llama-3.1-8B and Qwen3-14B. Across five benchmark suites and two models, rank-one compensation recovers 62.5% of the accuracy loss with about 2.0% kernel overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8, mixed precision, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chencheng Deng, Jianbin Fang, Dezun Dong
- 发布：2026-09-27；更新：2026-09-27
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
