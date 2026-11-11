---
title: "Multi-Node Transformers for Object Detection and Captioning Across Distributed Edge Networks"
description: "This paper presents a unified transformer-based framework for object detection and dense region captioning across distributed edge networks."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.11291) · [PDF](https://arxiv.org/pdf/2611.11291)

## 一句话摘要

This paper presents a unified transformer-based framework for object detection and dense region captioning across distributed edge networks.

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper presents a unified transformer-based framework for object detection and dense region captioning across distributed edge networks. The architecture uses a shared visual encoder followed by detection, region extraction, and autoregressive language-decoding stages, allowing localization and region description to reuse the same image features. This design removes the second image-encoding path required by decoupled detection and captioning pipelines. To support execution on resource-limited devices, a workload-allocation formulation assigns model stages and input streams across connected edge nodes while accounting for execution time, memory capacity, processor utilization, power limits, and intermediate tensor transfer cost. The framework is evaluated on a six-device edge testbed comprising four NVIDIA Jetson Orin Nano and Orin NX inference nodes and two Raspberry Pi 5 auxiliary CPU nodes, with TensorRT FP16 and INT8 execution on the NVIDIA devices. On a Jetson Orin Nano, the unified INT8 model achieves 38.1 FPS with 3.5 GB peak memory use and 11.8 W measured power. Under four concurrent streams, the proposed allocation achieves 35.2 FPS and 28.4 ms mean end-to-end latency with an internode transfer rate of 6.8 MB/s.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saurabh Kumar, Dewant Katare, Prakriti Jain
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
