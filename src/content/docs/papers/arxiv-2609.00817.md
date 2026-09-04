---
title: "Characterizing the Scalability and Performance of Large-Scale AI Training Under Multi-Tenancy"
description: "Characterising AI workload performance on modern HPC systems requires understanding both their scalability in isolation and their behaviour under concurrent execution."
---

**评分：40/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.00817) · [PDF](https://arxiv.org/pdf/2609.00817)

## 一句话摘要

Characterising AI workload performance on modern HPC systems requires understanding both their scalability in isolation and their behaviour under concurrent execution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Characterising AI workload performance on modern HPC systems requires understanding both their scalability in isolation and their behaviour under concurrent execution. However, the interplay among parallelisation strategies, network congestion, compute capability, and interconnect technologies remains poorly understood. This work investigates the performance and scalability of AI models up to 2400 GPUs. We quantify the communication overheads and their impact across different interconnects by evaluating scale-up, scale-out, and rack-scale configurations under multiple allocation schemes. Finally, we study how multiple concurrent training jobs interfere with each other by designing a realistic noise model. We design a benchmark suite of AI models to evaluate the performance of five distinct parallelisation strategies across different supercomputing clusters, including Alps, Leonardo, LUMI, JUPITER, NVL72 GB300, and DGX A100. Our work provides a systematic characterization of the scalability and execution efficiency of distributed AI training, while offering key insights into performance behavior under realistic multi-tenant scenarios.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jacopo Raffi, Thomas Pasquali, Lorenzo Piarulli, Filippo Spiga, Marco Faltelli, Andreas Herten, Domenico Siracusa, Daniele De Sensi, Flavio Vella
- 发布：2026-09-02；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
