---
title: "A 25-$\\mu$s/inf Event-driven Graph Neural Network Processor with Spatiotemporal Caching and Spline Convolution for Ultra-low-latency AI at the Edge"
description: "Dynamic-vision-sensor (DVS) cameras generate events on a per-pixel basis with a $\\mu$s-level temporal resolution, calling for new algorithm-hardware co-design approaches compared to standard frame-based vision."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.15241) · [PDF](https://arxiv.org/pdf/2609.15241)

## 一句话摘要

Dynamic-vision-sensor (DVS) cameras generate events on a per-pixel basis with a $\mu$s-level temporal resolution, calling for new algorithm-hardware co-design approaches compared to standard frame-based vision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Dynamic-vision-sensor (DVS) cameras generate events on a per-pixel basis with a $\mu$s-level temporal resolution, calling for new algorithm-hardware co-design approaches compared to standard frame-based vision. While event-driven graph neural networks (EV-GNNs) emerge as a promising algorithmic solution, they raise new HW challenges by mixing dense-regular compute operations and sparse-irregular memory accesses. We present ETHEREAL, the first EV-GNN accelerator that scales to 640$\times$480 resolutions, thanks to a neighbor-parallel spline convolution engine and a 2D/3D-split memory hierarchy with a novel region-of-interest spatiotemporal caching mechanism. Measurement results demonstrate end-to-end inference with 25.6$\mu$s latency and 1.7$\mu$J energy per event on state-of-the-art workloads

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Adrian Kneip, Martin Lefebvre, Daniel Gehrig, Victoria Catalán Pastor, Davide Scaramuzza, Marian Verhelst, Charlotte Frenkel
- 发布：2026-09-14；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
