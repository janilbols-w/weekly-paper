---
title: "DMA-Latte: Expanding the Reach of DMA Offloads to Latency-bound ML Communication"
description: "Offloading communication to existing direct memory access (DMA) engines, available on most state-of-the-art commercial GPUs, has emerged as a practical and low-cost solution to efficiently overlap computation and communication in machine learning (ML)."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2511.06605) · [PDF](https://arxiv.org/pdf/2511.06605)

## 一句话摘要

Offloading communication to existing direct memory access (DMA) engines, available on most state-of-the-art commercial GPUs, has emerged as a practical and low-cost solution to efficiently overlap computation and communication in machine learning (ML).

## 为什么值得关注

待编辑增强。

## 摘要原文

Offloading communication to existing direct memory access (DMA) engines, available on most state-of-the-art commercial GPUs, has emerged as a practical and low-cost solution to efficiently overlap computation and communication in machine learning (ML). However, the reach of DMA offloads has so far been limited to bandwidth-bound scenarios only (10s of MB to GB transfer sizes). In this work, we break this barrier and extend DMA communication offloads to latency-bound regions (KB to low MB). Specifically, we leverage hitherto untapped features available in the state-of-the-art AMD Instinct$^{\mathrm{TM}}$ GPUs that render DMA communication offloads competitive even in latency-bound regions. We demonstrate the efficacy of these features both at the operator level (ML communication collectives such as all-gather and all-to-all), and at the end-to-end workload level (LLM inference). At the operator level, our optimizations provide up to 4.5$\times$ speedups (3.2$\times$ geomean in the latency-bound region) over baseline DMA offload, narrowing the performance gap while delivering additional power savings (3-10%) for ML collectives compared to state-of-the-art GPU core-based communication library, RCCL. At the workload level, we demonstrate acceleration for LLM inference: up to 1.65$\times$ lower latency and up to 1.9$\times$ higher throughput over the state-of-the-art vLLM inference framework. We conclude with a discussion of AMD Instinct GPU runtime innovations that stand to expose these features.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Suchita Pati, Shaizeen Aga, Mahzabeen Islam, Ryan Quach, Saleel Kudchadker, Mohamed Assem Ibrahim
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
