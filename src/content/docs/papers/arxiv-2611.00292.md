---
title: "TADA: Technology Aware DNN Accelerator Performance and Energy Estimator"
description: "Deep neural network (DNN) accelerators for edge inference must meet tight energy, latency, and area (EDP) constraints, and their optimal hardware architecture and dataflow configuration is typically identified through design space exploration (DSE)."
---

**评分：58/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.00292) · [PDF](https://arxiv.org/pdf/2611.00292)

## 一句话摘要

Deep neural network (DNN) accelerators for edge inference must meet tight energy, latency, and area (EDP) constraints, and their optimal hardware architecture and dataflow configuration is typically identified through design space exploration (DSE).

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep neural network (DNN) accelerators for edge inference must meet tight energy, latency, and area (EDP) constraints, and their optimal hardware architecture and dataflow configuration is typically identified through design space exploration (DSE). However, on-chip memory technology including cell type, bank organization, and process node, is rarely treated as a first-class citizen in DSE. For example, increasing memory capacity can reduce memory accesses through greater data reuse, but at the cost of higher area and access energy, thereby limiting the compute units budget. Consequently, memory technology can fundamentally shift the optimal accelerator architecture for a given area and EDP budget. Existing machine learning (ML)-based DSE methods require repeating simulation, data generation, and model training for each new memory technology. We present TADA, a memory technology-aware DNN accelerator performance and energy estimator that predicts system latency and energy for a given workload, hardware configuration, and memory technology. TADA is trained on a synthetic dataset that generalizes across memory technologies. The dataset spans current and future technology trends while enforcing physics-based guardrails to preserve realistic area-energy trade-offs. Each memory technology is represented by a technology signature, a vector of read energy, write energy, and storage capacity across a range of areas, provided as input alongside the workload and hardware configuration. Across 21 unseen technology curves spanning SRAM, STTRAM, ReRAM, PCM, FeFET, eDRAM, and CTT, TADA predicts system energy and latency with 1.5-4.4% and 0.7-1.2% mean absolute percentage error, respectively. In three pairwise case studies, it matches the simulator-selected memory technology at 98.7-100% of area budgets, with a mean EDP loss of at most 0.21%, while achieving over 10^4x higher evaluation throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 18 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator, edge inference
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tanvi Sharma, Surya Selvam, Anand Raghunathan, Kaushik Roy
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
