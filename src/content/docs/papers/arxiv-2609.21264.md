---
title: "Programming AMD XDNA NPUs with Open-source Compiler Tools: A FlashAttention Case Study"
description: "Spatial NPUs such as AMD XDNA place compute tiles beside small local memories and leave data movement between them to software."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.21264) · [PDF](https://arxiv.org/pdf/2609.21264)

## 一句话摘要

Spatial NPUs such as AMD XDNA place compute tiles beside small local memories and leave data movement between them to software.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spatial NPUs such as AMD XDNA place compute tiles beside small local memories and leave data movement between them to software. Mapping a multi-stage workload onto such a device is largely a question of where the intermediate tensors live. We report what we learned making those choices for FlashAttention with the open-source IRON and MLIR-AIR flows. We compare four reference designs on XDNA 1 and XDNA 2: one runs each operator separately, two stream between operators on chip, and one fuses all three attention stages into a single kernel. The fused kernel holds the $\boldsymbol{QK}^{\mathsf T}$ scores in compute-tile local memory and reduces partial results over the cascade interconnect, so the scores never return to shared MemTile memory. On XDNA 2, it reaches 3.62 TFLOP/s over complete end-to-end execution, twice the IRON design, with 5.3 to 7.2 times the energy efficiency of the integrated GPU on the same chip at 2K tokens and above. It covers twelve LLM configurations, from BERT to DeepSeek, up to 128K tokens. Roofline analysis at each memory level explains this result and shows when to stop. XDNA 1 has lower ridge points, so streaming on chip already reaches the compute-bound regime: the same fusion that doubles throughput on XDNA 2 is nearly wasted on XDNA 1. Comparing a mapping's operational intensity against each level's ridge point predicts which case applies before writing any code. Fuse until the mapping clears that ridge point, then stop. We release the reference designs as maintained open source.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Erwei Wang, Ephrem Wu, Victor J. B. Jung, Jiajie Li, Andre Rosti, Joseph Melber, Samuel Bayliss
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
