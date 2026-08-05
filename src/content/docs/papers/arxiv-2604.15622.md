---
title: "AdaDINO: Context-Adaptive DINO-Distilled Vision Foundation Models for Efficient Open-Vocabulary Edge Inference"
description: "Always-on contextual AI runs language-aligned vision foundation models (VFMs) on edge devices, where the on-device model is the dominant continuous compute cost under strict latency and power limits."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2604.15622) · [PDF](https://arxiv.org/pdf/2604.15622)

## 一句话摘要

Always-on contextual AI runs language-aligned vision foundation models (VFMs) on edge devices, where the on-device model is the dominant continuous compute cost under strict latency and power limits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Always-on contextual AI runs language-aligned vision foundation models (VFMs) on edge devices, where the on-device model is the dominant continuous compute cost under strict latency and power limits. Due to an observed low-frequency shift in scene context and its relevant vocabulary, we present AdaDINO, an adaptive framework that makes on-device VFM inference efficient by matching execution to the current scene and task. We build on a known phenomenon, that the accuracy drop of shrinking model sizes depends on the task, and turn it into task-level adaptive execution. AdaDINO integrates neural architecture search (NAS) into a language-aligned VFM backbone distilled from DINOv2, training a single family of subnets for efficient execution during runtime. A multimodal large language model (LLM) on the cloud, invoked at low frequency, refines the candidate class set from scene context, while a learned selector activates the least-cost subnet predicted to retain a target fraction of accuracy. With the backbone and semantic pipeline held fixed, learned selection alone reduces average compute by $37\%$ over the best fixed subnet at equal segmentation accuracy. Across zero-shot classification and open-vocabulary segmentation, AdaDINO establishes a strong accuracy-efficiency frontier, improving over evaluated models of comparable sizes by up to $7.9\%$ in acc@1 on IN1K and $5.2\%$ mIoU on ADE20K, and reducing average FLOPs by up to $74.9\%$ at similar accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: edge inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiwei Zhao, Yi Zheng, Huapeng Su, Jieyu Lin, Stefano Ambrogio, Cijo Jose, Michael Ramamonjisoa, Patrick Labatut, Barbara De Salvo, Chiao Liu, Phillip B. Gibbons, Ziyun Li
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
