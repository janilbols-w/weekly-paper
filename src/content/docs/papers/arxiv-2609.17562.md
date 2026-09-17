---
title: "BLADE: ReliaBle Dynamic Hardware-Aware SNN-ANN Boundary SeLection for Event-BAseD Object DEtection"
description: "Hybrid Spiking Neural Network (SNN)-Artificial Neural Network (ANN) architectures combine the energy efficiency of SNNs with the superior detection accuracy of ANNs for event-based object detection."
---

**评分：45/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.17562) · [PDF](https://arxiv.org/pdf/2609.17562)

## 一句话摘要

Hybrid Spiking Neural Network (SNN)-Artificial Neural Network (ANN) architectures combine the energy efficiency of SNNs with the superior detection accuracy of ANNs for event-based object detection.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid Spiking Neural Network (SNN)-Artificial Neural Network (ANN) architectures combine the energy efficiency of SNNs with the superior detection accuracy of ANNs for event-based object detection. Existing hybrid SNN--ANN networks, however, employ static inference and select the SNN-ANN boundary primarily according to accuracy and energy consumption, without considering dynamic inference or reliability. This paper presents BLADE, the first reliability-aware boundary selection methodology for dynamic hybrid SNN-ANN networks with ANN early exit. The proposed framework jointly optimizes the SNN-ANN boundary and ANN early-exit configuration according to reliability, detection accuracy, execution time, and energy consumption, while incorporating reliability through hierarchical statistical fault injection during design-space exploration. Experimental evaluation on an event-based object detector achieves an mAP 0.5 of 0.691 while reducing the inference compute energy to 15.82~mJ when the ANN early exit fires. Reliability analysis identifies the most significant floating-point exponent bit as the dominant source of catastrophic failures, producing significant-or-worse accuracy degradation in 58.8% of its fault injections. Protecting this single bit with approximately 3% storage overhead eliminates catastrophic failures across the evaluated realistic technology fault rates. Furthermore, increasing the proportion of SNN computation improves fault tolerance, with the fully SNN configuration achieving a reliability retention of 0.965 under aggressive fault conditions. The results demonstrate that jointly optimizing reliability, accuracy, execution time, and energy consumption enables more dependable deployment of dynamic hybrid SNN--ANN systems for safety-critical edge AI applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mahdi Taheri, Alwin Paul
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
