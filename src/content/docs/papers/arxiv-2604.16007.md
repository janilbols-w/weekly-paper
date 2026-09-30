---
title: "MemExplorer: Navigating the Heterogeneous Memory Design Space for Agentic Inference NPUs"
description: "Emerging agentic large language model (LLM) workloads are driving rapidly growing demand for memory capacity and bandwidth."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2604.16007) · [PDF](https://arxiv.org/pdf/2604.16007)

## 一句话摘要

Emerging agentic large language model (LLM) workloads are driving rapidly growing demand for memory capacity and bandwidth.

## 为什么值得关注

待编辑增强。

## 摘要原文

Emerging agentic large language model (LLM) workloads are driving rapidly growing demand for memory capacity and bandwidth. Different phases of inference, such as prefill and decode, have distinct requirements. Industry is responding by combining heterogeneous accelerators into interconnected systems, as exemplified by NVIDIA's Vera Rubin platform, where each device has its own memory architecture. The range of available memory technologies is also expanding. High-density on-chip SRAM, HBM, LPDDR, GDDR, and emerging options such as high-bandwidth flash (HBF) each offer different trade-offs in capacity, bandwidth, and power. Identifying efficient memory architectures for next-generation inference accelerators remains challenging because the design space spans workload characteristics, NPU design choices, and memory system designs. To address this challenge, we present MemExplorer, a new memory system synthesizer for heterogeneous NPU systems. MemExplorer provides a unified way to model memory technologies at different levels of the hierarchy, including on-chip and off-chip memory. It automatically selects an efficient heterogeneous memory system alongside NPU design choices, such as matrix engine size, to balance throughput and power across prefill and decode devices in a multi-device system. For agentic workloads under the same power budget, MemExplorer achieves up to 2.3 times the energy efficiency of the baseline NPU and 3.23 times that of an H100 in the prefill-only setting. At equivalent performance targets in the decode setting, it delivers up to 1.93 times and 2.72 times the power efficiency of the baseline NPU and H100, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Haoran Wu, Zeyu Cao, Yao Lai, Binglei Lou, Jiayi Nie, Can Xiao, Timi Adeniran, Kevin Lau, Przemyslaw Forys, Kauser Johar, Catriona Wright, Junyi Liu, Kai Shi, Nicholas D. Lane, Rika Antonova, Jianyi Cheng, Timothy Jones, Aaron Zhao, Robert Mullins
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
