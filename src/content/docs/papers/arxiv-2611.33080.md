---
title: "Shifter Quantization: Compact Representations for Native Integer Computation"
description: "Groupwise quantization is used in LLM quantization to improve accuracy at low bit widths, but grouping weights keeps standard integer MMA from spanning the full dot product for efficient GPU inference."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.33080) · [PDF](https://arxiv.org/pdf/2611.33080)

## 一句话摘要

Groupwise quantization is used in LLM quantization to improve accuracy at low bit widths, but grouping weights keeps standard integer MMA from spanning the full dot product for efficient GPU inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Groupwise quantization is used in LLM quantization to improve accuracy at low bit widths, but grouping weights keeps standard integer MMA from spanning the full dot product for efficient GPU inference. We develop a new quantization method, Shifter Quantization (SQ), that reconstructs native-width integer operands by appending and shifting shared bits. To further extend the efficiency, we develop a special variant of SQ, Shifter Integer (SHI), to use INT4 kernels. We show that SQ and SHI formats perform better than standard groupwise quantization in quality, as measured by projection error and KL divergence, and in inference speed, as measured during decoding and prefill. For low precision like 2-bit quantization, SQ2 and SHI2 achieve 2.71-3.77x the 4,096-token prefill throughput of llama.cpp on a Q2_K checkpoint and reduce WikiText-2 KL by 6.6-7.8%. For mid precision like 4-bit quantization, SQ4 achieves 1.43-2.47x the prefill throughput of NInfer's groupwise-integer baselines across the tested models and prompt lengths, with 24-40% lower KL than the NInfer baselines. For high precision like 8-bit quantization, SQ8 achieves 27.4% higher batch-one prefill throughput and 72.7% lower KL than vLLM's online FP8.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, int4, low precision, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yufeng Huang
- 发布：2026-11-24；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
