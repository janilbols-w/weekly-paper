---
title: "Iapetus: Content-Aware Hierarchical Scheduling for Collaborative ViT Inference in LEO Satellite Networks"
description: "Collaborative inference pools distributed resources to run compute-intensive Vision Transformers (ViTs) in satellite edge computing."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.03318) · [PDF](https://arxiv.org/pdf/2609.03318)

## 一句话摘要

Collaborative inference pools distributed resources to run compute-intensive Vision Transformers (ViTs) in satellite edge computing.

## 为什么值得关注

待编辑增强。

## 摘要原文

Collaborative inference pools distributed resources to run compute-intensive Vision Transformers (ViTs) in satellite edge computing. Model partitioning enables such collaboration by assigning consecutive layer groups to different nodes, but the large volume of intermediate activation data incurs substantial transfer overhead that can erase its benefit. Token compression reduces downstream computation and activation transfer, but its quality impact depends on input content, model depth, and earlier pruning decisions, while layer offloading must adapt to time-varying contact and battery conditions. We present \sys, a content-aware hierarchical scheduler that screens constellation-wide options to retain a bounded candidate set, then refines each candidate into a complete token compression and layer offloading trajectory using quality prediction and joint planning. A unified objective balances per-task latency, energy, and quality loss against accumulated workload and battery pressures. We implement \sys on an NVIDIA Jetson AGX Orin hardware-in-the-loop testbed and use its validated execution model for constellation-scale trace replay across multiple ViT workloads and constellation settings. At \(5\)~tasks/s, \sys accomplishes 91.6\% of released tasks, 26.1 percentage points above MARATD3, the strongest baseline, while reducing mean latency and battery draw by 53.0\% and 70.8\%, respectively, and meeting quality targets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yan Chen, Yunxiang Zhang, Guanjun Jiang, Haiquan Wang
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
