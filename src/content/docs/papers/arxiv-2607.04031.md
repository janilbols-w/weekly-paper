---
title: "TileLens: Efficiently Using Large-Granularity Memory Systems with Transparent Two-Dimensional Memory Layout"
description: "Large Language Model (LLM) inference is bottlenecked by the capacity and bandwidth of GPU High-Bandwidth Memory (HBM)."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2607.04031) · [PDF](https://arxiv.org/pdf/2607.04031)

## 一句话摘要

Large Language Model (LLM) inference is bottlenecked by the capacity and bandwidth of GPU High-Bandwidth Memory (HBM).

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Model (LLM) inference is bottlenecked by the capacity and bandwidth of GPU High-Bandwidth Memory (HBM). Recent proposals, such as High-Bandwidth Flash (HBF) and RoMe, offer higher capacity or bandwidth than HBM, but require a minimum access granularity of kilobytes. We show that these Large-Granularity Memory Systems (LGMS) can degrade LLM inference performance by up to an order of magnitude. The root cause is read amplification during tiled matrix multiplication, in which each memory request fetches far more data than the compute tile needs. Such waste stems from a fundamental mismatch between the two-dimensional nature of compute tiles and the one-dimensional memory layout, causing each request to spill well beyond tile boundaries. To eliminate read amplification in LGMS, we propose to use tile-major layout. Rather than storing data as a one-dimensional strip, tile-major layout reshapes each contiguous memory block into a two-dimensional rectangle, aligning memory granularity with tile boundaries. To ease the adoption of tile-major layout on GPUs, we propose TileLens, lightweight software and hardware extensions that cover major classes of GPU kernels. TileLens-SW extends GPU DSLs so that DSL-based kernels can adopt tile-major by only changing the layout descriptor. TileLens-HW extends the Tensor Memory Accelerator (TMA) for tile-major support in TMA-based kernels without code changes. We evaluate TileLens on a cycle-level GPU simulator using Qwen-3 30B and Llama-3.1 70B. Combining a tile-major layout with our adaptive degree prefetcher, TileLens achieves near-HBM performance on HBF-augmented GPUs with a 5 us NAND read latency, reducing the geomean slowdown from 1.62-6.69x with conventional layouts to within 10% of an HBM-only baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jae Hyung Ju, Euijun Chung, Hritvik Taneja, Anish Saxena, Shinnung Jeong, Hyesoon Kim, Moinuddin K. Qureshi
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
