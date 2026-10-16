---
title: "MFSA: A Multi-Format Systolic Array with Native Micro Scaling Support"
description: "AI workloads increasingly employ low-precision formats such as BF16 / FP16, FP8 variants, FP4, Micro Scaling (MX), and INT modes across models, layers, and execution stages to balance accuracy, memory footprint, and throughput, which in turn requires hardware to support these formats in a flexible and efficient way."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.19645) · [PDF](https://arxiv.org/pdf/2610.19645)

## 一句话摘要

AI workloads increasingly employ low-precision formats such as BF16 / FP16, FP8 variants, FP4, Micro Scaling (MX), and INT modes across models, layers, and execution stages to balance accuracy, memory footprint, and throughput, which in turn requires hardware to support these formats in a flexible and efficient way.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI workloads increasingly employ low-precision formats such as BF16 / FP16, FP8 variants, FP4, Micro Scaling (MX), and INT modes across models, layers, and execution stages to balance accuracy, memory footprint, and throughput, which in turn requires hardware to support these formats in a flexible and efficient way. We present MFSA, a weight-stationary multi-format systolic array that achieves area efficiency through two architectural choices. At the PE level, MFSA uses dot-product-accumulator-based processing elements extended from an existing open-source trans-precision FPU to support reduced-precision formats (FP32/FP16/BF16/CFP8/FP4/INT16/INT8/INT4) with a shared datapath and proportional throughput scaling. At the array level, MFSA employs Online Block-Scale Rebasing (OBSR) for block-scaled formats, which folds each block scale into the running FP32 partial sum at block boundaries without adding a second cross-block accumulator, thereby reducing the additional overhead of block-scaling support. In TSMC 28 nm at 1 GHz, matched-throughput BF16/FP8/FP4 cascaded FMA-PE baselines are 1.5x/2.5x/4.5x larger than the single-format DPA-PE, the gap growing with subword parallelism. A routed 16x16 MFSA reaches a peak 0.5/1/2/4 TOPS of FP32/BF16/FP8/FP4, and OBSR cuts the incremental MX overhead by 64.2% in area and 67.5% in energy versus a naive MX implementation baseline, without hurting the numerical stability on real LLM traces. Adding support for all other formats based on a BF16+CFP8 systolic array costs 25.7% additional area. OBSR also extends to non-power-of-two block scales: folding the fractional part of an E4M3 scale into the MFPE dot product supports NVFP4 alongside OCP MX for 11.8% area and 7.3% power over a CFP8+FP4 base, less than half the cost of a naive implementation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8, int4, int8
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiayi Wang, Kearnan Bishop, Ang Li
- 发布：2026-10-14；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
