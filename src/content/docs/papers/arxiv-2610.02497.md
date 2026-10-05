---
title: "LiteEMG-FM: An Efficient and Deployable Foundation Model for Robust EMG Sensing"
description: "Electromyography (EMG) signals vary substantially across individuals, body regions, recording sessions, and sensing hardware, limiting the generalization of models for assistive devices and human-computer interaction."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.02497) · [PDF](https://arxiv.org/pdf/2610.02497)

## 一句话摘要

Electromyography (EMG) signals vary substantially across individuals, body regions, recording sessions, and sensing hardware, limiting the generalization of models for assistive devices and human-computer interaction.

## 为什么值得关注

待编辑增强。

## 摘要原文

Electromyography (EMG) signals vary substantially across individuals, body regions, recording sessions, and sensing hardware, limiting the generalization of models for assistive devices and human-computer interaction. Existing time-series foundation models are also computationally expensive for real-time wearable deployment and often fail to capture EMG-specific time-frequency characteristics. We present LiteEMG-FM, an efficient hybrid CNN-Transformer foundation model for practical EMG sensing. Pretrained on 16 diverse upper- and lower-limb EMG datasets, LiteEMG-FM learns representations that generalize across users and datasets. For resource-constrained deployment, we implement a hierarchical wake-up architecture in which a lightweight, always-on 1D-CNN filters rest and non-target activity and activates LiteEMG-FM only for valid gestures. We evaluate full inference offloading, split inference, and full on-device processing, characterizing their trade-offs in latency, power consumption, and memory footprint. Across diverse evaluation settings, LiteEMG-FM outperforms state-of-the-art time-series foundation models and supervised baselines, particularly under zero-calibration cross-participant and data-scarce conditions. These results demonstrate that LiteEMG-FM is an effective, efficient, and deployable foundation model for EMG applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhao Wu, Xu Wu, Amirmohammad Radmehr, Jiawei Yu, Yi Wu, Phuc Nguyen, Jian Liu
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
