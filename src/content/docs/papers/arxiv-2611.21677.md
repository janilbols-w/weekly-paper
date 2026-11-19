---
title: "Chimera: A Configurable LLM Decode Accelerator Architecture with Compute-Memory-Floorplan Co-Design for HBM-Equipped Multi-Die FPGAs"
description: "GPUs are widely used for LLM inference, but single-request decoding is memory-bound, leaving their compute underutilized while they draw substantial power."
---

**评分：48/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.21677) · [PDF](https://arxiv.org/pdf/2611.21677)

## 一句话摘要

GPUs are widely used for LLM inference, but single-request decoding is memory-bound, leaving their compute underutilized while they draw substantial power.

## 为什么值得关注

待编辑增强。

## 摘要原文

GPUs are widely used for LLM inference, but single-request decoding is memory-bound, leaving their compute underutilized while they draw substantial power. HBM-equipped FPGAs are well suited to LLM decoding: their customizable datapaths use memory bandwidth more energy-efficiently than GPUs. However, high memory bandwidth alone does not ensure high decode performance: exploiting it requires parallel compute and memory interfaces, whose resource costs and placement on the chip can limit the throughput. We present Chimera, a configurable LLM decode accelerator architecture that co-designs compute, memory access, and floorplan. Specifically, HBM Proxy Ports extend HBM access to compute lanes on every super logic region (SLR) die, and tiered expert storage holds mixture-of-experts weights beyond the HBM capacity. In addition, a unified configuration analysis estimates per-token latency and per-SLR resource use and guides the design of each configuration within resource budgets. On an AMD Alveo U280, we build ten designs for eight dense, mixture-of-experts, hybrid linear/standard-attention, and ternary LLMs, up to an 80B-parameter mixture-of-experts LLM on four memory tiers. Chimera's designs achieve a geometric mean of 1.6$\times$ the token throughput of prior state-of-the-art FPGA implementations and 3.0$\times$ and 1.5$\times$ the energy efficiency of the RTX 3090 and A100 GPUs, setting a new benchmark for LLM decoding on HBM-equipped FPGAs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiheng Chen, Yifan Zhang, Yu-An Chou, Ye Qiao, Sitao Huang
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
