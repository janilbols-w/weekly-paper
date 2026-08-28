---
title: "TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving"
description: "Prefix caching introduces a fundamental tradeoff in multi-agent large language model (LLM) serving: retaining a long system-prompt key-value (KV) cache for an agent accelerates future calls, yet it reduces the GPU memory available for batching concurrent requests."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.25523) · [PDF](https://arxiv.org/pdf/2608.25523)

## 一句话摘要

Prefix caching introduces a fundamental tradeoff in multi-agent large language model (LLM) serving: retaining a long system-prompt key-value (KV) cache for an agent accelerates future calls, yet it reduces the GPU memory available for batching concurrent requests.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prefix caching introduces a fundamental tradeoff in multi-agent large language model (LLM) serving: retaining a long system-prompt key-value (KV) cache for an agent accelerates future calls, yet it reduces the GPU memory available for batching concurrent requests. In multi-stage workflows, existing schedulers tend to prioritize either immediate prefix locality or overall workflow progress. However, under a shared KV cache budget, optimizing either objective in isolation can prolong tasklevel job completion time (JCT) through downstream delays or frequent prefix replacement. To strike a balance, we here propose TOPAS, a Task-Oriented Prefix-Aware Scheduler that jointly decides which agent prefixes to keep in the cache and which requests to schedule for execution. TOPAS scores candidate post-decision states by trading off the expected reduction in each task's longest remaining service path against the near-term benefit of downstream prefix reuse, accounting for the costs of prefix movement and preemption. A task-level aging mechanism is also incorporated to prevent starvation. We implement TOPAS within the SGLang framework and assess its performance on three synthetic DAGs and two MetaGPT software-development workflows. Compared with the best performing baseline for each workload and metric, TOPAS reduces the mean/p99 JCT by up to 39.8%/49.4% on the synthetic workloads, while lowering mean JCT by 9.8% on MetaGPT-SOP and mean/p99 JCT by 22.0%/26.6% on MetaGPT-TL.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongqiu Ni, Han Tian, Chi Zhang, Guopeng Li, Haisheng Tan
- 发布：2026-08-26；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
