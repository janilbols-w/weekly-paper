---
title: "Implementation and Evaluation of BitNet Inference on a CGLA by Signed-Int4 Instructions"
description: "Large language model (LLM) inference transfers model weights and activations for every generated token, making memory traffic and its energy cost part of the decode path."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.27453) · [PDF](https://arxiv.org/pdf/2609.27453)

## 一句话摘要

Large language model (LLM) inference transfers model weights and activations for every generated token, making memory traffic and its energy cost part of the decode path.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference transfers model weights and activations for every generated token, making memory traffic and its energy cost part of the decode path. BitNet b1.58 represents its low-bit weights by ternary values and uses integer activations. However, this arithmetic does not match conventional int8 or floating-point general matrix multiplication, and existing BitNet accelerators implement it in specialized datapaths. We instead map this operation to a CPU-Grounded Linear Array (CGLA), a programmable ASIC with explicit direct memory access, local memories, and reusable compiler-visible integer lanes. The mapping adds OP_SMA4 as a reusable signed-int4 multiply-accumulate instruction rather than a BitNet-only datapath. Each ternary weight occupies one signed 4-bit lane. Each int8 activation is split into two signed-int4 fragments and reconstructed by shift-and-add. Frequency scaling of the 145 MHz FPGA measurement to an 840 MHz 28 nm CGLA achieved 0.390 ns per signed-int4 product. We showed that CGLA-offloaded BitNet C++ execution measures 2.52 tokens/s.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Takuto Ando, Yasuhiko Nakashima
- 发布：2026-09-23；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
