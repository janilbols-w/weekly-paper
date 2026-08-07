---
title: "Architectural Implications of Agentic AI Workflows"
description: "Agentic AI is emerging in datacenters, but its architectural implications remain unexplored."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.04458) · [PDF](https://arxiv.org/pdf/2608.04458)

## 一句话摘要

Agentic AI is emerging in datacenters, but its architectural implications remain unexplored.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic AI is emerging in datacenters, but its architectural implications remain unexplored. We organize agentic workflows in a taxonomy and present its first architectural characterization with a production study at Microsoft Azure and a controlled study of open-source frameworks. We show that agentic execution is fragmented and heterogeneous. Requests expand into a workflow of LLM inferences, tool invocations, and orchestration decisions that repeatedly cross the CPU-GPU boundary. Our taxonomy explains how this fragmentation turns into resource demand. As orchestration and tools run on the host, the CPU sits on the critical path. Execution structure sets the load over time, which stays low with sudden spikes. Model composition sets how evenly the workflow uses the GPUs. Diversity in tasks and tools widens this range even further. These characteristics expose architectural mismatches of conventional uniform servers. Fragmented execution strands CPU and GPU capacity despite bursty demand. Different software roles make homogeneous CPU provisioning inefficient. Finally, multiplexing many agents onto shared cores degrades microarchitectural locality. Guided by our findings, we derive implications for agentic servers and examine them through Agora, our prototype for commodity servers. Agora dynamically harvests idle CPU cores for co-located throughput work, while protecting agentic tail latency against tool spikes. It oversubscribes GPU memory by placing more agents on each GPU, prefetching the next agent's state to hide swap latency. To match the machine to the heterogeneous roles, Agora pools cores by role and applies affinity-aware scheduling to restore locality. It automatically tunes mechanisms to the workload. Agora improves utilization and server throughput while preserving agent tail latency. Our insights also identify key directions for future server architectures for agentic AI.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jirong Yang, Peizhe Liu, Chaojie Zhang, Jovan Stojkovic
- 发布：2026-08-05；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
