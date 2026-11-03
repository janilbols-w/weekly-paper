---
title: "AMMA: A Multi-Chiplet Memory-Centric Architecture for Low-Latency 1M Context Attention Serving"
description: "All current LLM serving systems place the GPU at the center, from production-level attention-FFN disaggregation to NVIDIA's Rubin GPU-LPU heterogeneous platform."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2604.26103) · [PDF](https://arxiv.org/pdf/2604.26103)

## 一句话摘要

All current LLM serving systems place the GPU at the center, from production-level attention-FFN disaggregation to NVIDIA's Rubin GPU-LPU heterogeneous platform.

## 为什么值得关注

待编辑增强。

## 摘要原文

All current LLM serving systems place the GPU at the center, from production-level attention-FFN disaggregation to NVIDIA's Rubin GPU-LPU heterogeneous platform. Even academic PIM/PNM proposals still treat the GPU as the central hub for cross-device communication. Yet the GPU's compute-rich architecture is fundamentally mismatched with the memory-bound nature of decode-phase attention, inflating serving latency while wasting power and die area on idle compute units. The problem is compounded as reasoning and agentic workloads push context lengths toward one million tokens, making attention latency the primary user-facing bottleneck. To address these inefficiencies, we present AMMA, a multi-chiplet, memory-centric architecture for low-latency long-context attention. AMMA replaces GPU compute dies with HBM-PNM cubes, roughly doubling the available memory bandwidth to better serve memory-bound attention workloads. To translate this bandwidth into proportional performance gains, we introduce (i) a logic-die microarchitecture that fully exploits per-cube internal bandwidth for decode attention under a minimal power and area budget, (ii) a two-level hybrid parallelism scheme, and (iii) a reordered collective flow that reduces intra-chip die-to-die communication overhead. We further conduct a design-space exploration over per-cube compute power and intra-chip D2D link bandwidth, providing actionable guidance for hardware designers. Evaluations show that AMMA achieves 15.5X lower attention latency and 6.9X lower energy consumption compared with the NVIDIA H100.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhongkai Yu, Haotian Ye, Chenyang Zhou, Ohm Rishabh Venkatachalam, Zaifeng Pan, Zhengding Hu, Junsung Kim, Won Woo Ro, Po-An Tsai, Shuyi Pei, Yangwook Kang, Yufei Ding
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
