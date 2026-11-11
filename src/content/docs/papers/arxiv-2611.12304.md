---
title: "Evolving Infra: Agent-Adaptive LLM Serving at Scale"
description: "Agentic workloads are a major source of LLM inference demand."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.12304) · [PDF](https://arxiv.org/pdf/2611.12304)

## 一句话摘要

Agentic workloads are a major source of LLM inference demand.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic workloads are a major source of LLM inference demand. Existing prefill--decode (PD) disaggregated serving systems offer limited flexibility for runtime adaptation of compute allocation and KV cache management, and rely on coarse signals that only partly capture the diverse and dynamic agent workload. These limitations lead to load imbalance between prefill and decode nodes and eviction of KV caches that agents will reuse. We present Evolving Infra, an agent-adaptive serving framework that adapts compute allocation to agent workloads and KV cache management to agent context management at runtime. We decouple compute allocation from key--value (KV) cache management, allowing nodes to switch efficiently between prefill and decode. Building on this design, an online planner matches the PD split to workload composition, while an agent-aware distributed KV manager guides cache eviction and transfer with signals from agent context management. Across coding, math, and computer-use tasks with GLM-5.2 and Kimi K2.6 on up to 256 GB300 GPUs, Evolving Infra reduces mean end-to-end request latency and P95 TTFT by up to 4.1x and 14x over Dynamo, NVIDIA's production framework.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hao Kang, Weili Xu, Ziyang Li, Zheng Du, Hanchen Li, Tian Xia, Song Bian, Tushar Krishna, Huizi Mao, Ion Stoica, Song Han
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
