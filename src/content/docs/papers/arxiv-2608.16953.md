---
title: "DTX: A Throughput-First Training Accelerator for Diffusion and Transformer Models"
description: "DTX is a throughput-first training accelerator for diffusion and transformer models."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.16953) · [PDF](https://arxiv.org/pdf/2608.16953)

## 一句话摘要

DTX is a throughput-first training accelerator for diffusion and transformer models.

## 为什么值得关注

待编辑增强。

## 摘要原文

DTX is a throughput-first training accelerator for diffusion and transformer models. Any summation serialized through a single FP32 adder is a loop-carried dependence that pins a machine near 2 FLOP/cycle regardless of physical design; DTX is built so no such chain exists anywhere -- every reduction is a pipelined binary tree, every FP operator a two-stage pipeline with initiation interval 1. An 8x8 weight-stationary systolic array with a fused bias/activation/cast epilogue, an 8-lane vector unit, an 8-lane fused AdamW pipeline, and a pipelined Philox Gaussian source are co-issued by a 4-slot VLIW word over a unified 64 KB tile space: 216 FLOP/cycle, roughly 108x the loop-carried floor per clock. With no canonical sum order, verification is tolerance-based against an FP64 golden model, with exact-equality carve-outs and a demonstrably tight bound (a premise-violating program measured 5,340x over budget; 17/17 tests, 107,108 elements, zero failures). Semantic gates confirm an on-device diffusion-MLP run reduces its loss (56.4 to 26.0), counter-level proof shows compute/DMA overlap sustains the peak, an analytical iso-node decomposition bounds the GPU comparison at 6-10x throughput per watt, and a sky130 campaign hardens the systolic array to DRC-clean GDS at 83.3 MHz post-route -- 1.9x an optimized loop-carried MAC baseline on the same node and flow.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Shashank
- 发布：2026-08-19；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
