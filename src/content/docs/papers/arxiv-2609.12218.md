---
title: "BRIDGE-EEG: Bridging Self-Supervised Pretraining and Efficient Deployment for Cross-Dataset EEG Classification"
description: "The growing use of electroencephalography (EEG) motivates automated analysis that is accurate, transferable, and deployable on constrained hardware."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.12218) · [PDF](https://arxiv.org/pdf/2609.12218)

## 一句话摘要

The growing use of electroencephalography (EEG) motivates automated analysis that is accurate, transferable, and deployable on constrained hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

The growing use of electroencephalography (EEG) motivates automated analysis that is accurate, transferable, and deployable on constrained hardware. Recent EEG foundation models learn general representations from large-scale pretraining, but their size and computational cost limit edge and wearable deployment. We introduce BRIDGE-EEG, an efficient multi-task EEG classification pipeline that preserves the benefits of pretraining while reducing model size. A unified preprocessing scheme maps heterogeneous recordings with different channel counts, montages, and sampling rates to a device-agnostic 62-channel time--frequency representation. We pretrain an SE-ResNet18 teacher (11.84 M parameters) with SimCLR on unlabeled EEG from five heterogeneous datasets, then compress it into SE-ResNet8 (1.56 M) and SE-ResNet4 (0.48 M) students using task-agnostic and task-specific distillation. We evaluate six benchmarks spanning abnormality detection, motor imagery, and emotion recognition. For abnormality detection and emotion recognition, the students achieve accuracy comparable to or better than several recent EEG foundation models with 10--1,000$\times$ more parameters. Motor imagery shows a remaining representation gap, highlighting the importance of pretraining diversity. Inference profiling on a server GPU, desktop CPU, and NVIDIA Jetson Orin Nano shows up to 3.0$\times$ lower edge energy per inference (15.64 mJ vs. 46.67 mJ). The compact models further support future deployment on MCU-class wearables.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Meghna Roy Chowdhury, Chengwei Zhou, Haotian Yu, Gourav Datta, Shreyas Sen
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
