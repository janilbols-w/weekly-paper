---
title: "The World Model Hardware Accelerator"
description: "Diffusion transformers invert the arithmetic that autoregressive decoding made familiar."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.16244) · [PDF](https://arxiv.org/pdf/2609.16244)

## 一句话摘要

Diffusion transformers invert the arithmetic that autoregressive decoding made familiar.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion transformers invert the arithmetic that autoregressive decoding made familiar. There is no token-by-token recurrence: every denoising step is a full-sequence forward pass over static shapes, so the entire schedule is known at compile time and the only serial dimension is the step count itself. We exploit that structure in WMHA, a latency-first diffusion-transformer inference accelerator: a very-long-instruction-word sequencer issues four engines from one instruction word, a weight-stationary 16x16 dual-dot array streams FP8 and BF16 contractions, and a single-pass online-softmax attention pipeline keeps keys and values resident through a skewed software pipeline. The design is specified in a frozen micro-architecture document, implemented in synthesizable SystemVerilog, and verified against a double-precision reference model by a UVM environment whose acceptance criterion is semantic: the device must run a real denoising trajectory and reduce mean squared error against a clean latent by at least a factor of ten. It does so by a factor of 23, at both synthesized configurations, with zero element failures across 237 million checked values. Eleven application benchmarks built from published model shapes, including the original diffusion-transformer configuration, run on the device and report measured occupancy beside separately labelled projections. Five engines are taken to routed layout in sky130 with parasitic-annotated timing and measured-activity power; the full chip is synthesized, and the host limit that stopped its place-and-route is quantified together with the machine that would remove it.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shashank Chaurasia
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
