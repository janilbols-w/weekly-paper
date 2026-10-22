---
title: "TrainBridge: Agentic NPU Training Optimization Guided by GPU Compilation Evidence"
description: "We study how to improve training efficiency on Ascend NPUs."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.29171) · [PDF](https://arxiv.org/pdf/2610.29171)

## 一句话摘要

We study how to improve training efficiency on Ascend NPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study how to improve training efficiency on Ascend NPUs. In the NPU training programs we study, framework-level compilation optimizations such as operator fusion are only partially applied, leaving fragmented computation and avoidable execution overheads. Profiling-guided tuning can address these inefficiencies, but it often requires costly trial and error. To make training on NPUs more efficient, we propose TrainBridge, an agentic approach for transferring GPU optimization guidance to NPU training. TrainBridge uses the highly optimized execution produced by mature GPU compilation stacks as a task-specific reference for NPU tuning. It extracts optimization intents from the GPU training execution to guide NPU program rewrites and further refines the rewritten program through iterative profiling. Our GPU-to-NPU migration experiments show that TrainBridge achieves an average 1.7x speedup across four workloads covering LLM pretraining, image classification, and vision-language training, and an average speedup of nearly 2.0x across 27 Modded-NanoGPT speedrun records with highly optimized GPU implementations.

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

- taxonomy keywords: operator fusion
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yupeng Chen, Kunxiang Zhao, Xingjian Wang, Yue Zhao, Yijing Wu, Ye Liu, Kai Li, Congliang Chen, Ruoyu Sun
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
