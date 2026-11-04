---
title: "AoiZora: Compiler-Agnostic, Placement-Aware Auto-Parallelization for Video Diffusion Transformers"
description: "Video diffusion transformers (DiTs) process tens of thousands of spatio-temporal tokens per denoising step, so low-latency inference and training commonly spread them across several accelerators."
---

**评分：39/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2606.17566) · [PDF](https://arxiv.org/pdf/2606.17566)

## 一句话摘要

Video diffusion transformers (DiTs) process tens of thousands of spatio-temporal tokens per denoising step, so low-latency inference and training commonly spread them across several accelerators.

## 为什么值得关注

待编辑增强。

## 摘要原文

Video diffusion transformers (DiTs) process tens of thousands of spatio-temporal tokens per denoising step, so low-latency inference and training commonly spread them across several accelerators. Auto-parallelization systems price a sharding on its logical graph, but its cost depends on the program the compiler generates and, on direct networks such as TPU sub-slices, on which chip runs each logical rank; both are visible only after compilation, while the chip assignment must be fixed before it. We present AoiZora, a compiler-agnostic auto-parallelization framework built on two IRs, one for the program a partitioner shards and one for the program a compiler emits; it chooses the logical mesh, the layout of every tensor and operation, and the device assignment of an unsharded model by pricing its compiled programs, without executing any candidate. At the core of AoiZora is evidence, a compiler-neutral record of a compiled program that leaves its placement open, so that one compilation can be priced under many placements by a calibrated model of the accelerator network and the placement can determine which sharding is selected. On TPU v5e, AoiZora reduces the denoising latency of Wan 2.1 and HunyuanVideo by 1.23x and 1.32x on average over expert configurations and Alpa, finding each plan within 10 minutes; it also speeds up training on TPU v5p by 1.11x on 4 chips and 1.21x on 8 chips on average and parallelizes PyTorch programs on GPUs with the same core.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kaijian Wang, Yuanyuan Xu, Fanjiang Ye, Ye Cao, Jingwei Zuo, T. S. Eugene Ng, Yarong Mu, Yuke Wang
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
