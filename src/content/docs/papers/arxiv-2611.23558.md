---
title: "Towards Fair Resource Sharing in Agentic LLM Serving"
description: "As LLM agents increasingly execute complex, multi-step tasks on shared inference infrastructure, resource contention across the end-to-end LLM serving stack causes severe and uneven slowdowns across agents."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.23558) · [PDF](https://arxiv.org/pdf/2611.23558)

## 一句话摘要

As LLM agents increasingly execute complex, multi-step tasks on shared inference infrastructure, resource contention across the end-to-end LLM serving stack causes severe and uneven slowdowns across agents.

## 为什么值得关注

待编辑增强。

## 摘要原文

As LLM agents increasingly execute complex, multi-step tasks on shared inference infrastructure, resource contention across the end-to-end LLM serving stack causes severe and uneven slowdowns across agents. Existing agentic serving systems primarily optimize throughput and latency, with comparatively limited attention to fairness among concurrent agents. Although fairness has been studied in conventional LLM serving at the token and request levels, these approaches do not fully capture cumulative delays and stateful resource dependencies across successive LLM calls within an agent. Moreover, interference spans request routing, runtime scheduling, and hardware resources, making agent-level fairness challenging to define and optimize across an end-to-end serving stack. This paper presents a cross-layer framework to define agent-level fairness, attribute sources of unfairness, and optimize fairness while preserving throughput. To account for agents with widely varying execution demands, we build a theoretical foundation to define fairness using slowdown relative to standalone execution. Our empirical analysis reveals that routing, runtime scheduling, and hardware contention jointly determine fairness, with performance-oriented policies often leading to prolonged queuing delays. To optimize fairness, we introduce Duru, which monitors each agent's slowdown and uses this signal to guide admission and scheduling decisions across the router and runtime. Duru further alleviates starvation through admission exceptions and integrates slowdown-driven autoscaling to adhere to Service-Level Objectives (SLOs). Our evaluation across various benchmarks and hardware platforms shows that Duru reduces 99th-percentile normalized slowdown by a geometric mean of 44.4% (up to 79.5%) while delivering 91.8-127.4% of the state-of-the-art system's throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sehyeon Lee, Yuchen Xia, Zhaoyang Hong, Jinrui Hu, Anuradha Pandey, Evan Zhao, Ankita Nayak, Nishil Talati
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
