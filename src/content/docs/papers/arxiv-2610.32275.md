---
title: "RootDown: Deploying and Benchmarking Models for Beet-Root Detection on Edge Devices"
description: "Quality inspection of sugar beets after harvest and storage is critical to preserve sugar content and ensure optimal processing efficiency."
---

**评分：39/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.32275) · [PDF](https://arxiv.org/pdf/2610.32275)

## 一句话摘要

Quality inspection of sugar beets after harvest and storage is critical to preserve sugar content and ensure optimal processing efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quality inspection of sugar beets after harvest and storage is critical to preserve sugar content and ensure optimal processing efficiency. The transfer of harvested beets to field clamps or trucks provides an opportunity to visually inspect individual beets automatically on loader conveyors. However, this is a challenging task as the large number of beets causes partial overlap and occlusion, complicating both annotation and detection. In this work, we propose an end-to-end image-based pipeline for detecting partially occluded sugar beets in loading scenarios as a first step toward automated quality inspection. We introduce a dedicated benchmark and present an automatic annotation strategy that leverages the SAM 3 foundation model to generate bounding boxes. We compare models trained on manually annotated and automatically generated labels. Additionally, we investigate deployment considerations by benchmarking multiple inference configurations, including execution on an edge device, under realistic operational constraints regarding precision, inference time and power consumption. Our results show that, despite substantial occlusion and inherent annotation ambiguity, foundation-model-based labels can substitute for a substantial share of manual annotation, trading labeling effort for data volume at a modest accuracy cost. Furthermore, we demonstrate that a Raspberry Pi 5 equipped with a Hailo accelerator enables high-performance, low-power inference, making it a practical solution for mobile outdoor deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Gerardus Croonen, Andreas Trondl, Julia Simon, Daniel Steininger
- 发布：2026-10-26；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
