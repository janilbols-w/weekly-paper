---
title: "Efficient Block-Layer Parallel Inference for Vision-Language-Action on Hybrid Architectures"
description: "Vision-Language-Action (VLA) models are becoming a promising paradigm for autonomous driving, but their deployment on existing vehicle platforms remains difficult because they introduce both high inference latency and strong GPU-side resource pressure."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.14586) · [PDF](https://arxiv.org/pdf/2608.14586)

## 一句话摘要

Vision-Language-Action (VLA) models are becoming a promising paradigm for autonomous driving, but their deployment on existing vehicle platforms remains difficult because they introduce both high inference latency and strong GPU-side resource pressure.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-Language-Action (VLA) models are becoming a promising paradigm for autonomous driving, but their deployment on existing vehicle platforms remains difficult because they introduce both high inference latency and strong GPU-side resource pressure. In a full autonomous driving stack, this problem is even more pronounced: legacy vehicle platforms were provisioned for modular pipelines, yet after several planning-related functions are absorbed into a unified VLA model, part of the original CPU budget becomes underutilized, while the visual encoder and the main reasoning path still concentrate most computation and memory demand on the GPU. As a result, directly deploying VLA together with the rest of the onboard system can be hard under realistic GPU memory constraints. To address this issue, we present a hybrid CPU--GPU inference framework with flexible resource scheduling for autonomous driving. Our design partitions the VLA backbone at the block-layer granularity, executes the visual encoder and LLM prefix on the GPU, and offloads the LLM suffix to the CPU through a cross-frame asynchronous pipeline, thereby exposing a schedulable boundary for redistributing compute and memory pressure across heterogeneous processors. We evaluate the proposed framework on two representative driving VLA models, Orion and MindDrive. On Bench2Drive, our method reduces average latency from 521ms to 408.0ms for Orion and from 443ms to 306.2ms for MindDrive, corresponding to 21.7% and 30.9% reduction, respectively. For Orion, the estimated peak GPU memory is further reduced from 45GB to 29GB. In real-vehicle deployment under coexistence with Autoware.Universe, native Orion cannot run because the onboard GPU memory budget is insufficient, whereas the hybrid version runs successfully together with the full vehicle stack.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haibo HU, Lianming Huang, Qiao Li, Nan Guan, Chun Jason Xue
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
