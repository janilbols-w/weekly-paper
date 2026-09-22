---
title: "Leveraging Industrial Foundation Models at the Edge of Particle Physics Detectors via Distillation Learning and Hardware Co-design"
description: "Data acquisition (DAQ) systems at future particle physics experiments stand to benefit from the extremes of AI/ML development: large-scale foundation models can enhance the performance of feature extraction algorithms, and small-scale on-detector deployments can enable real-time intelligent data handling."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.23385) · [PDF](https://arxiv.org/pdf/2609.23385)

## 一句话摘要

Data acquisition (DAQ) systems at future particle physics experiments stand to benefit from the extremes of AI/ML development: large-scale foundation models can enhance the performance of feature extraction algorithms, and small-scale on-detector deployments can enable real-time intelligent data handling.

## 为什么值得关注

待编辑增强。

## 摘要原文

Data acquisition (DAQ) systems at future particle physics experiments stand to benefit from the extremes of AI/ML development: large-scale foundation models can enhance the performance of feature extraction algorithms, and small-scale on-detector deployments can enable real-time intelligent data handling. This work provides the first fine-tuning of an industrial foundation model for particle physics DAQ. Starting from the backbone of Google Research's TimesFM (Time Series Foundation Model), we demonstrate fine-tuning on real-time regression tasks for drift chamber trackers and dual-readout calorimeters. Furthermore, the fine-tuned TimesFM model is distilled into a student and co-designed with FPGA implementation to enable these models to run in real-time at future colliders. The fine-tuned distillations meet or exceed the performance of previously published AI/ML solutions for each task. Further, the pipeline of distillation and model compression from TimesFM is generic and can be easily adapted to a variety of 1D waveform tasks across domains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Gia Ancone, Qibin Liu, Liangyu Wu, Julia Gonski
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
