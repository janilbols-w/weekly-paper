---
title: "C2C-Explorer: An Exploration Framework for Chip-to-Chip Interconnect Architectures in LLM Cloud Computing Systems"
description: "The scaling-up of large language models (LLMs) necessitates computing systems to have multi-processor-chip architectures, elevating the importance of chip-to-chip (C2C) communication."
---

**评分：48/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2608.08611) · [PDF](https://arxiv.org/pdf/2608.08611)

## 一句话摘要

The scaling-up of large language models (LLMs) necessitates computing systems to have multi-processor-chip architectures, elevating the importance of chip-to-chip (C2C) communication.

## 为什么值得关注

待编辑增强。

## 摘要原文

The scaling-up of large language models (LLMs) necessitates computing systems to have multi-processor-chip architectures, elevating the importance of chip-to-chip (C2C) communication. However, designing efficient C2C hardware architectures for LLM workloads faces three key challenges: generating realistic LLM-specific C2C traffic, accurately simulating hardware-level communication at scale, and efficiently exploring the exponentially large C2C design space. We propose C2C-Explorer, an adaptive Bayesian DSE framework that integrates a LLM-workload-driven traffic generator, a scalable interconnect simulator (switch/full-mesh, up to 512 chips), and a metric-guided evaluator into a workload-to-hardware optimization pipeline, enabling systematic C2C architectural co-design under realistic LLM workloads. Validated against FPGA-based C2C prototypes, the C2C simulator achieves 2.46-8.23% end-to-end timing error across diverse traffic patterns. Its hybrid cycle and event model further accelerates large-scale simulation by up to 7.8$\times$ over a pure cycle-accurate baseline. Applied to a 32-XPU DeepSeek-R1-671B inference workload, C2C-Explorer identifies configurations that improve goodput by 44.1% and reduce memory by 98.4%. C2C-Explorer is open-source and available at https://github.com/Selinaee/C2C-Explorer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jiayi Li, Di Wu, Qingxu Li, Hongxiao Zhao, Jiaqi Yang, Anjunyi Fan, Wenbin Zhang, Boqiang Wu, Shuting Liu, Shifeng Fang, Jianbo Dong, Dimin Niu, Bonan Yan
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Selinaee/C2C-Explorer](https://github.com/Selinaee/C2C-Explorer)
- 阅读深度：metadata
