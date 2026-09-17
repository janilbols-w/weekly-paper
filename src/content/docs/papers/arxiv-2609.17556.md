---
title: "WARD: Runtime Workload-Adaptive Vision TRansformer Framework for Dependable Edge AI"
description: "Edge-deployed AI operate under dynamically changing power budgets, reliability requirements, and input distributions, requiring continuous adaptation."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2609.17556) · [PDF](https://arxiv.org/pdf/2609.17556)

## 一句话摘要

Edge-deployed AI operate under dynamically changing power budgets, reliability requirements, and input distributions, requiring continuous adaptation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge-deployed AI operate under dynamically changing power budgets, reliability requirements, and input distributions, requiring continuous adaptation. Such conditions arise in long-running edge AI applications, including autonomous systems, industrial monitoring, and satellite onboard intelligence. Existing fault-tolerant methods assume static operating conditions, whereas continual learning techniques neglect concurrent hardware faults during online adaptation. Moreover, the practical deployment of runtime-adaptive reliability frameworks on programmable AI accelerators remains largely unexplored. This paper presents WARD, a runtime-adaptive Vision Transformer framework that combines channel-wise subnetwork partitioning, reliability-aware continual learning, and dynamic operating-mode scheduling to jointly optimize performance, fault tolerance, and adaptation according to runtime conditions. Two physically isolated subnetworks execute under four operating modes (i.e. Full-Precision Mode, Low-Power Mode, High-Reliability Mode, and Adaptive Mode) that dynamically adjust computational cost and reliability while ensuring uninterrupted inference for real-time requirements. To validate the practical deployability of the proposed framework, WARD is implemented on a lightweight FPGA-based accelerator extended with runtime hardware support for mode scheduling and resource management. Experimental results demonstrate that the proposed split architecture achieves a network-level failure rate of only 1.79% under high Bit Error Rates. The hardware implementation incurs less than 5% area overhead and supports runtime mode transitions within few clock cycles, demonstrating that adaptive reliability management can be integrated into programmable edge AI accelerators with negligible implementation overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fault tolerance
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mahdi Taheri, Pramit Kumar Bhaduri, Mohammad Masoumi, Ali Mahani
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
