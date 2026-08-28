---
title: "Thermal Tuning Overhead in Wafer-Scale Optical Interconnects for LLM MoE Training: A Cross-Layer Analysis and Ferroelectric-Based Mitigation"
description: "The rapid scaling of large language models (LLMs), particularly mixture-of-experts (MoE) architectures, has intensified interconnect demands because expert-parallel execution is communication-intensive."
---

**评分：43/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2608.24637) · [PDF](https://arxiv.org/pdf/2608.24637)

## 一句话摘要

The rapid scaling of large language models (LLMs), particularly mixture-of-experts (MoE) architectures, has intensified interconnect demands because expert-parallel execution is communication-intensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid scaling of large language models (LLMs), particularly mixture-of-experts (MoE) architectures, has intensified interconnect demands because expert-parallel execution is communication-intensive. Wafer-scale optical interconnects based on dense wavelength-division multiplexing (DWDM) offer a promising path to higher bandwidth; however, conventional microring-resonator (MRR)-based links rely on thermo-optic tuning and are therefore vulnerable to workload-induced thermal fluctuations. In this work, we present a cross-layer analysis of wafer-scale optical interconnects for MoE workloads that combines workload profiling, packet-level network simulation, and transient thermal analysis. We implement a wafer-scale topology in the ht-sim simulator and construct an Ansys thermal model of a 3D-integrated GPU/EIC/PIC stack. Our results show that transient temperature variations can exceed the tracking capability of conventional thermo-optic control loops and thereby introduce repeated tuning stalls during communication phases. The stall durations injected into the network simulation are derived directly from the thermal model rather than assumed. We further evaluate a ferroelectric-based electro-optic tuning mechanism that removes the continuous thermal-tuning requirement. In a four-layer proxy simulation across three MoE models, eliminating the tuning stalls yields speedups of 2.7x for Mixtral 8x7B, 3.8x for Qwen-MoE 14.3B, and 3.3x for LLaMA-MoE 6.7B relative to the thermo-optic case. These results indicate that minimizing photonic tuning latency is important for realizing the performance potential of optical interconnects in large-scale AI systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Seongwon Yoon, Pin-Jun Chen, Shimeng Yu
- 发布：2026-08-25；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
