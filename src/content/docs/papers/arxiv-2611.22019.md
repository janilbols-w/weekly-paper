---
title: "Computed Permutation Trellis Coding: Near-Optimal Quantization from Two Multiplications and a 64-Byte Table"
description: "We propose Computed Permutation Trellis Coding (CPTC), a low-bit quantization format for tensors written once and read many times."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.22019) · [PDF](https://arxiv.org/pdf/2611.22019)

## 一句话摘要

We propose Computed Permutation Trellis Coding (CPTC), a low-bit quantization format for tensors written once and read many times.

## 为什么值得关注

待编辑增强。

## 摘要原文

We propose Computed Permutation Trellis Coding (CPTC), a low-bit quantization format for tensors written once and read many times. Formats that round each value on its own, such as INT4 and FP4, waste a large part of their bits against the information-theoretic ideal. Trellis codes recover this loss by encoding values jointly, but prior decoders either need a large lookup table for their best quality or compute values with a hash that restricts what they can decode. CPTC's decoder multiplies its state by two coefficients and adds the top bits of the products to index a 64-byte table. Because that sum is not uniformly distributed, the rarely used ends of a small table can hold values far out in the tails. One decoder serves every bit width from 1 to 6, reproduces the standard integer and floating-point formats exactly, and comes within 0.07 bits of the ideal at 4 bits. It matches a random-permutation trellis code whose table is thousands of times larger, and exceeds every QTIP codebook. In LLM weight quantization without fine-tuning, CPTC has the lowest KL divergence to the unquantized model at every tested bit width on Llama 3.1 8B and 70B Instruct against QTIP's codebooks (by up to 27%). The decoder has been built into the AWS Trainium 4 AI accelerator, where it runs at the throughput of the native FP4 and FP8 formats for a negligible fraction of the systolic array's area. Fused encoding kernels quantize an 8B model's linear layers in under two minutes on one GPU and, in cycle-level simulation, on one Trainium 4 chip.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8, int4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Muhammed Fatih Bal{\i}n
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
