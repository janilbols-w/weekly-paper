---
title: "CHARMING: Parallel Edge AI Acceleration Across Tensor Processing and In-Memory Computation"
description: "Edge AI increasingly relies on specialized accelerators for low-latency inference under tight resource and energy constraints, yet their efficiency remains limited by data movement."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.17785) · [PDF](https://arxiv.org/pdf/2611.17785)

## 一句话摘要

Edge AI increasingly relies on specialized accelerators for low-latency inference under tight resource and energy constraints, yet their efficiency remains limited by data movement.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge AI increasingly relies on specialized accelerators for low-latency inference under tight resource and energy constraints, yet their efficiency remains limited by data movement. Prior work, CHARM, mitigates this overhead by overlapping data movement with computation. We observe that in-memory computing can further supplement tensor processing as a parallel accelerator while eliminating certain data movements entirely. We present CHARMING, a heterogeneous edge AI architecture that uses accuracy- and quantization-aware partitioning to distribute and concurrently execute inference workloads across tensor processing and in-memory computation. CHARMING partitions attention heads between an AIE array and an in-DRAM compute unit, balancing execution according to model architecture, sequence length, and precision while selecting heads to minimize accuracy degradation. CHARMING also integrates quantization into the AIE projection stage to further reduce data movement. We validate CHARMING end-to-end in hardware on AMD Versal VCK5000 and Alveo U200 platforms and evaluate LLM and video-generation models across multiple precisions using measured hardware results and simulation of the latest in-memory compute hardware. CHARMING improves prefill performance by up to 23.6 percent and decode performance by up to 44 percent over AIE-only acceleration. With int4 x int4 fixed-point in-memory computation, CHARMING reduces per-layer energy by up to 7.6 percent and improves energy-delay product by up to 24.7 percent, while maintaining accuracy similar to a 32-bit floating-point baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Md Omar Faruque, Jingang Jin, Jo\~ao Paulo C. de Lima, Shouzhi Fang, William C. Tegge, Peipei Zhou, Qinru Qiu, Alex K. Jones
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
