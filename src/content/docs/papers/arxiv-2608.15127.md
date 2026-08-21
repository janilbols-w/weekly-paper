---
title: "From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems"
description: "Agentic applications are shifting AI serving from isolated model inference to long-running workloads in which LLMs coordinate tools, environments, and persistent state."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.15127) · [PDF](https://arxiv.org/pdf/2608.15127)

## 一句话摘要

Agentic applications are shifting AI serving from isolated model inference to long-running workloads in which LLMs coordinate tools, environments, and persistent state.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic applications are shifting AI serving from isolated model inference to long-running workloads in which LLMs coordinate tools, environments, and persistent state. However, the system behavior of these workloads---where latency, cost, and bottlenecks arise---remains poorly characterized, leaving serving systems to rely on assumptions built for conventional inference. We present AgentSysBench, a benchmark suite and measurement toolkit with ten representative agentic applications and unified systems-level instrumentation. Across controlled deployments and production traces, we identify six properties that distinguish agentic workloads from conventional LLM serving: (1) execution is heavyweight and stateful, with non-LLM components dominating latency in 5 of 10 applications and sandbox working-set memory peaking at 28 GB per session; (2) applications compose components with heterogeneous resource affinity---GPU-bound inference, memory-bound retrieval, CPU-bound sandboxes---whose task latencies diverge by up to 32x; (3) bottlenecks shift across requests, models, and deployments; (4) production sessions hold state idle for minutes to hours between active steps; (5) a control-plane tax---auxiliary LLM calls and context overhead from tool schemas and observations---crowds out productive compute and context; and (6) production traces from three applications reveal heavy cross-request redundancy in search queries and web fetches, exposing a large caching opportunity. Four design explorations demonstrate that these findings are actionable: task-aware serving reduces latency by 29--40%, communication-aware placement by up to 4.5x, state offloading reduces memory usage by 4.6x, and tool-result caching removes 35.2% of redundant search calls and saves 19.3% of aggregate search latency.

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

- taxonomy keywords: offloading
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Chaokun Chang, Yukun Zhou, Kaihua Fu, Dakai An, Tianyu Feng, Hanfeng Lu, Sheng Yao, Pu Guo, Yinghao Yu, Yizhou Shan, Bo Li, Binhang Yuan, Wei Wang
- 发布：2026-08-15；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
