---
title: "Nalar: Workflow-Aware Management of Agentic Applications"
description: "LLM-driven agentic applications automate complex, multi-step tasks, but serving them efficiently remains difficult due to heterogeneous components, dynamic model-driven control flow, long-lived state, and highly variable latencies."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2601.05109) · [PDF](https://arxiv.org/pdf/2601.05109)

## 一句话摘要

LLM-driven agentic applications automate complex, multi-step tasks, but serving them efficiently remains difficult due to heterogeneous components, dynamic model-driven control flow, long-lived state, and highly variable latencies.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-driven agentic applications automate complex, multi-step tasks, but serving them efficiently remains difficult due to heterogeneous components, dynamic model-driven control flow, long-lived state, and highly variable latencies. Nalar is a serving framework for agent workflows that separates workflow specification from execution while providing the runtime visibility and control needed for robust performance. Nalar preserves ordinary Python interfaces and control flow through lightweight auto-generated stubs that turn agent and tool invocations into futures carrying dependency and execution-context metadata. A two-level control architecture combines global policy computation with local event-driven enforcement to support adaptive routing, scheduling, and resource management across evolving workflows. A workflow-aware KV-cache layer enables the runtime to manage cache placement and lifetime. Together, these mechanisms enable scalable, efficient, policy-driven serving of heterogeneous agentic applications without burdening developers with orchestration logic. Across three agentic workloads, Nalar reduces tail latency by 34-74% and achieves up to 3.38x speedups.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Saurabh Agarwal, Marco Laju, Donghyun Son, Nitin Kedia, Myungjin Lee, Jayanth Srinivasa, Aditya Akella
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
