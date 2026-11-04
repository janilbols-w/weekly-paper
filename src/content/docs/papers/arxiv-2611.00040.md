---
title: "Real-Time Obstacle Detection and Distance Estimation on Smartphones for Visually Impaired and Distracted Pedestrians"
description: "According to the World Health Organization, at least 2.2 billion people worldwide live with visual impairment, including tens of millions with severe vision loss."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.00040) · [PDF](https://arxiv.org/pdf/2611.00040)

## 一句话摘要

According to the World Health Organization, at least 2.2 billion people worldwide live with visual impairment, including tens of millions with severe vision loss.

## 为什么值得关注

待编辑增强。

## 摘要原文

According to the World Health Organization, at least 2.2 billion people worldwide live with visual impairment, including tens of millions with severe vision loss. Traditional aids such as white canes or guide dogs remain costly, limited in capability, and inaccessible to many. At the same time, smartphone distraction in public spaces has been linked to elevated risks of collisions with vehicles, trips, and falls. These dual challenges motivate lightweight, smartphone-based solutions that combine accessibility with low latency. We present a Kotlin-based Android application that uses a YOLOv8 detector, retrained to recognize eighteen common urban obstacle classes, to deliver real-time obstacle alerts for both user groups. The detector was optimized with pruning, quantization, and early-exit branches, and deployed through the Android Neural Networks API (NNAPI), which can dispatch inference to GPU, NPU, or DSP accelerators when available. On a mid-range smartphone, these optimizations reduced average inference latency from about 3.2 s for the off-the-shelf YOLOv8n to 0.39-0.48 s; the recommended configuration (INT8 quantization with early exit) runs in 0.42-0.48 s while retaining a recall of 0.81. The application combines the optimized detector with ARCore-based or monocular focal-length distance estimation, so it works with a single smartphone camera and requires no LiDAR, depth camera, or other specialized sensor. Multimodal feedback, including Text-to-Speech guidance for visually impaired users and vibration alerts for distracted pedestrians, supports use across different contexts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Abtin Zandi, Sarvin Nami, Roza Ganjipour, Bardia Sabagh Kermani, Amirreza Tarabkhah, Hamed Farbeh
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
