---
title: "A Low-Latency ASIC Architecture for Real-Time Line Segment Detection"
description: "Line segment detection is a critical preprocessing step in embedded vision applications such as autonomous navigation, visual SLAM, and industrial inspection."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.06439) · [PDF](https://arxiv.org/pdf/2608.06439)

## 一句话摘要

Line segment detection is a critical preprocessing step in embedded vision applications such as autonomous navigation, visual SLAM, and industrial inspection.

## 为什么值得关注

待编辑增强。

## 摘要原文

Line segment detection is a critical preprocessing step in embedded vision applications such as autonomous navigation, visual SLAM, and industrial inspection. Deep learning methods achieve high accuracy but require substantial resources, limiting their deployment on resource-constrained platforms. Classical algorithms are efficient but exhibit content-dependent latency. This paper presents a low-latency ASIC architecture for real-time line segment detection. The proposed design is based on the step-length algorithm and incorporates five ASIC-specific features: register-based line buffering with data reuse, multiplierless MCM-based filtering, 8-class angle quantization, a CAM-like associative memory for single-cycle matching, and an optimized duplicate removal mechanism. The architecture is fully pipelined and processes one pixel per clock cycle with deterministic latency. Synthesized in a 45nm CMOS process, the design achieves 325 FPS at VGA resolution and 48 FPS at Full HD, with 25.54 mW power consumption and 0.412 mm\textsuperscript{2} area. At 125 MHz, the throughput increases to 406 FPS at VGA resolution with 31.48 mW power consumption. Compared with a 90nm ASIC implementation based on the Line Hough Transform, the proposed design reduces power consumption by 49\% and delivers over 1.6 times higher frame rate. The architecture is well suited for edge-computing applications requiring real-time performance, low power, and minimal area.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Amir Hossein Jalilvand, Parsa Hassani Shariat Panahi, M. Hassan Najafi
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
