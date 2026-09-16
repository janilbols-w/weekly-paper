---
title: "Carry-Through Checksum: A Lightweight Fault-Detection for CNN Inference at the Edge"
description: "Convolutional Neural Networks (CNNs) are increasingly deployed in safety-critical edge applications, where soft errors can silently corrupt inference outputs and lead to unsafe decisions."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2609.16742) · [PDF](https://arxiv.org/pdf/2609.16742)

## 一句话摘要

Convolutional Neural Networks (CNNs) are increasingly deployed in safety-critical edge applications, where soft errors can silently corrupt inference outputs and lead to unsafe decisions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Convolutional Neural Networks (CNNs) are increasingly deployed in safety-critical edge applications, where soft errors can silently corrupt inference outputs and lead to unsafe decisions. Such applications typically rely on resource-constrained embedded GPUs, requiring fault detection and mitigation techniques that add minimal compute, memory, and latency overhead while integrating seamlessly with the standard GPU inference pipeline. Existing algorithm-based fault tolerance techniques rely on matrix augmentation and per-operation checksum verification, imposing substantial overhead that is prohibitive for CNN inference on embedded GPUs. In this work, we propose carry-through checksum, a fundamentally new scheme for soft-error detection in CNN inference on embedded GPUs. The method embeds dedicated carry-through filters into the convolutional layers, which compute a checksum from the CNN's own operations and propagate it through inference, enabling end-to-end error detection with a single output verification. Experimental results on multiple CNN architectures show that the proposed method detects 95.86% and 86.56% of critical faults for FP32 and FP16, respectively, at almost no additional per-image overhead. Detected faults are mitigated through re-execution, incurring only 2.27% run-time overhead across the entire test set on an NVIDIA Jetson Orin NX GPU.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fault tolerance
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kyrylo Nazarevych, Mohammad Hasan Ahmadilivani, Krister Kaldre, Davide Bertozzi, Jaan Raik
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
