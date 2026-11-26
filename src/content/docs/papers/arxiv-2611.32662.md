---
title: "OpenWoud: Vendor-Unlocked Scalable Adaptive Random Forest Accelerator"
description: "Online Machine Learning (ML) enables real-time decision-making on evolving data streams."
---

**评分：51/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.32662) · [PDF](https://arxiv.org/pdf/2611.32662)

## 一句话摘要

Online Machine Learning (ML) enables real-time decision-making on evolving data streams.

## 为什么值得关注

待编辑增强。

## 摘要原文

Online Machine Learning (ML) enables real-time decision-making on evolving data streams. These dynamic models learn continuously to adapt to new concepts, as previous ones become invalid, but their performance is often limited by throughput. The Adaptive Random Forest (ARF) is a state-of-the-art model for this setting, which naturally exposes parallelism and is therefore well-suited for hardware acceleration. However, prior Field Programmable Gate Array (FPGA)-based accelerators are vendor-locked and rely on resource-hungry Floating-Point (FP) arithmetics, limiting their scalability and portability. We present OpenWoud, a vendor-unlocked ARF framework for FPGAs. Our design replaces FP operators with a flexible FiXed-Point (FxP) arithmetic library and introduces fully transparent, manually scheduled dataflows for training and drift detection. This enables fine-grained time/area trade-offs and predictable behavior across platforms. A comprehensive evaluation on both synthetic and real datasets shows that OpenWoud maintains or increases accuracy (up to +12.89%), compared to a prior FPGA accelerator, while reducing the resource utilization by half. Competitive performance is observed compared to GPU (0.5 - 1.5x speed-up) and an FPGA baseline (0.2 - 0.5x), despite the latter being based on idealized simulation. Crucially, OpenWoud sustains true sample-by-sample inference, unlike GPUs that require batch insertion.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ewout van Nimwegen, Elijah Seth Cishugi, Hendrik Folmer, Marco Ottavi, Kuan-Hsun Chen
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
