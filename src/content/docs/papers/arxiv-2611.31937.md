---
title: "Native Block-Quantized Matrix Multiplication and Explicit K/V Residency with Dual-View Access for LLM Inference on RISC-V Vector Processors"
description: "Some key execution states in large language model inference persist across multiple instructions and are difficult to express and exploit within RVV semantics centered on individual operations."
---

**评分：55/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.31937) · [PDF](https://arxiv.org/pdf/2611.31937)

## 一句话摘要

Some key execution states in large language model inference persist across multiple instructions and are difficult to express and exploit within RVV semantics centered on individual operations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Some key execution states in large language model inference persist across multiple instructions and are difficult to express and exploit within RVV semantics centered on individual operations. We define specialization boundaries according to data-state lifetimes and propose Quantized Block Streams (QBS) and Attention/KV Context (AKV) while preserving RVV programmability. QBS organizes native-block format processing, block traversal, integer computation, and ordered FP32 accumulation into a unified execution process, whereas AKV maintains local K/V residency and supplies operand views aligned with the computation direction while leaving Attention arithmetic on RVV. Cycle-accurate RTL evaluation shows that QBS achieves geometric-mean speedups of 35.68x and 51.34x for projection Compute and Matmul, respectively, while AKV achieves a 1.45x geometric-mean speedup over Tiled RVV for Decode Attention. Compared with the baseline, the complete design increases total area by 12.65%; on the evaluated projection workloads, throughput per area and energy efficiency improve by 46.63x and 19.78x, respectively. Further evaluation demonstrates applicability across multiple block-quantization formats and across models with different Attention organizations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Weiying Wang, Yuanyang Xiang, Zhiwei Zhang
- 发布：2026-11-24；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
