---
title: "Atik: A Shared-Mesh Transformer Accelerator for RISC-V"
description: "Transformer inference repeatedly invokes dense matrix multiplication and attention, including its data-dependent softmax normalization."
---

**评分：47/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.09522) · [PDF](https://arxiv.org/pdf/2611.09522)

## 一句话摘要

Transformer inference repeatedly invokes dense matrix multiplication and attention, including its data-dependent softmax normalization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer inference repeatedly invokes dense matrix multiplication and attention, including its data-dependent softmax normalization. We present Atik, an open-source RoCC accelerator for RocketChip that executes matrix multiplication and dense attention through one shared fixed-point MAC mesh. Atik accepts and returns BF16 tensors, uses a streaming online-softmax schedule that never materializes the full score matrix, and is invoked through a small descriptor-based ABI. We evaluate three meshes cycle-by-cycle on FireSim and report standalone Sky130 physical-design area. Across 137 logged FireSim test records, all tests pass their benchmark tolerance with zero reported output mismatches. Relative to the same scalar Rocket BF16 reference, the 8x8 configuration reaches 31.5x peak matmul speedup and 225.8x peak attention speedup. Hybrid projections for the single-layer workload-derived C models, using directly measured accelerator-kernel cycles, give aggregate speedups of 44.2x, 77.1x, and 32.3x for ViT, TinyBERT, and GPT-2 prefill, respectively; these are not full-model hardware replays.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ahmed Zeer, Erkan Uslu
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
