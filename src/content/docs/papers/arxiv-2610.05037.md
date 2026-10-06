---
title: "SparseCraft: Agentic Hardware-Software Co-Optimization for Sparse Computing"
description: "Sparse-accelerator design spaces are usually searched against analytical models, so a design point is admitted on what a model predicts rather than on what the hardware does."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.05037) · [PDF](https://arxiv.org/pdf/2610.05037)

## 一句话摘要

Sparse-accelerator design spaces are usually searched against analytical models, so a design point is admitted on what a model predicts rather than on what the hardware does.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse-accelerator design spaces are usually searched against analytical models, so a design point is admitted on what a model predicts rather than on what the hardware does. SparseCraft closes that gap with a language model inside a closed CHIA loop. In each of 15 iterations the model reads the measured outcome of the previous one and edits the Chisel RTL, the memory configuration and the sparse-kernel schedule of a Gemmini accelerator through MCP tool servers, and no candidate counts until it has been checked for legality, elaborated, simulated cycle-accurately, checked bit-for-bit on every output against a golden reference, and synthesised. The harness turns each measurement into the next work order, a diagnosed bottleneck with matching strategy guidance, the history of tried designs and a score of the model's own prediction, and a second model repairs changes that fail a gate. On a $512 \times 512$ GraphChallenge sparse-DNN layer the loop reaches 2.1x fewer cycles, 9.8x less off-chip traffic and 22.8% less area than the block-sparse Gemmini baseline, with 5.61x higher modelled perf/W and 11.8x lower EDP. The levers span three layers: a schedule that keeps the dense operand resident removes 9.8x of the traffic, a zero-gated MAC and a zero-row skip unit that the model wrote in Chisel cut energy, and resizing the memories cuts area.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rajatabha Chakraborty, M P Samartha, Vedant Pahariya, Priyesh Shukla
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
