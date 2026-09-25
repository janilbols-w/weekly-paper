---
title: "Where Does the Energy Go? Profiling LLM Agent Inference on Blackwell GPUs"
description: "LLM agents that iteratively reason, plan, and invoke tools create workload profiles fundamentally different from single-pass inference, yet how their energy consumption is distributed across hardware components and workload phases remains poorly understood."
---

**评分：45/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](https://arxiv.org/abs/2609.29707) · [PDF](https://arxiv.org/pdf/2609.29707)

## 一句话摘要

LLM agents that iteratively reason, plan, and invoke tools create workload profiles fundamentally different from single-pass inference, yet how their energy consumption is distributed across hardware components and workload phases remains poorly understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents that iteratively reason, plan, and invoke tools create workload profiles fundamentally different from single-pass inference, yet how their energy consumption is distributed across hardware components and workload phases remains poorly understood. Characterizing these workloads therefore requires simultaneous visibility into both component-level power and phase-level execution. We conduct a full-stack energy profiling study combining NVML GPU counters, Intel RAPL CPU/DRAM counters, and Intelligent Platform Management Interface (IPMI) system-level sensors on 2x NVIDIA RTX PRO 6000 Blackwell GPUs, and profile three representative workloads with Qwen3.8-27B. For mathematical reasoning, we compare thinking-enabled and thinking-disabled modes. Our measurements reveal that GPU-only telemetry misses 41-45% of system energy across all three workloads, with non-GPU components accounting for the remainder. In our setup, the sequential agent workload consumes 63x more system energy per output token than saturated serving, reflecting the absence of batching, context growth across turns, and tool-induced idle periods. Extended thinking generates 21-75% more tokens per problem, while per-token energy differs by less than 1% between modes within each dataset, indicating that the resulting increase in energy is driven by output volume rather than a change in per-token efficiency. Continuous batching improves system-level energy efficiency by 3.2x from 1 to 16 requests per second, as GPU power plateaus while throughput continues to increase with batching depth. For the memory-bandwidth-bound reasoning workload, throughput remains unchanged under per-GPU power caps of 400-600 W but drops sharply at 300 W. These findings suggest that context-management techniques such as summarization and selective retrieval may help reduce energy consumption in agent deployments.

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

- taxonomy keywords: continuous batching
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Qi Luo, Kunlin Li, Ziwen Wang, Yun Chen
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
