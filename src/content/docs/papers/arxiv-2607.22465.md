---
title: "ORACLE: Agentic AI Orchestrator Routing Via Adaptive Verifier Calibration Feedback"
description: "Modern enterprise agent deployments consist of a heterogeneous pool of large language models (LLMs) having diverse capabilities and cost."
---

**评分：48/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2607.22465) · [PDF](https://arxiv.org/pdf/2607.22465)

## 一句话摘要

Modern enterprise agent deployments consist of a heterogeneous pool of large language models (LLMs) having diverse capabilities and cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern enterprise agent deployments consist of a heterogeneous pool of large language models (LLMs) having diverse capabilities and cost. Existing model routing strategies optimize the quality-cost trade-off, while providing request-level static decisions. More recent solutions address agentic routing as a task-level selection with a serial verifier based router feedback loop. However, their fixed verifier suitable for homogeneous workloads may not generalize to heterogeneous batches of agentic tasks (example: coding, general conversational). Additionally, due to the verifier placement in the critical path of the loop, serving quality may be affected during multiple concurrent requests routing. To mitigate these issues, we present ORACLE. It is a concurrency-aware online routing mechanism that aligns adaptive routing with adaptive verification for feedback. ORACLE acts as a training-free drop-in 'feedback loop' on top of any model-selection policy to first classify the task type and then dynamically assigns a task-appropriate verifier. Further, we develop a delayed feedback strategy for concurrent requests that largely removes verifier latency from the dispatch critical path. We then present a post-routing dispatch scheduler, namely DISC. DISC reserves each task's peak KV footprint at admission and dispatches to an alternate backend when the reward gain from reduced wait exceeds the reward loss from lower accuracy. Extensive evaluation on SWE-bench, tau2-bench, and Terminal-Bench 2.0 shows that ORACLE improves the accuracy-cost frontier by up to 7 percentage points over state-of-the-art routing baselines, while ORACLE with DISC improves program throughput by up to 1.8x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ritik Raj, Souvik Kundu, Dheemanth Joshi, Tushar Krishna
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
