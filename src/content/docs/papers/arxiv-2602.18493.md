---
title: "Learning to Remember: End-to-End Training of Memory Agents for Long-Context Reasoning"
description: "Long-context LLMs and Retrieval-Augmented Generation defer state tracking and evidence consolidation to query time, which is brittle when facts evolve and answers depend on latent states."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2602.18493) · [PDF](https://arxiv.org/pdf/2602.18493)

## 一句话摘要

Long-context LLMs and Retrieval-Augmented Generation defer state tracking and evidence consolidation to query time, which is brittle when facts evolve and answers depend on latent states.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLMs and Retrieval-Augmented Generation defer state tracking and evidence consolidation to query time, which is brittle when facts evolve and answers depend on latent states. We introduce Unified Memory Agent (UMA) for a one-to-many setting: query-agnostic external memory is constructed once from a stream and reused across multiple future QA sessions. A single policy maintains a structured Memory Bank through CRUD operations and answers using both the Memory Bank and raw context. Task-Stratified GRPO uses the mean reward of QA trajectories branching from each sampled memory state to supervise memory maintenance, while normalizing memory and per-question QA groups separately. We also introduce Ledger-QA, a diagnostic benchmark for long-horizon state tracking over accumulated updates. At the 16k budget, UMA-Generalist achieves the highest average score among compared methods across the test-time-learning and accurate-retrieval benchmarks and transfers to Ledger-QA without task-specific training; UMA-Specialist further improves long-horizon tracking after task adaptation. These results support learned proactive memory management for long-context reasoning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management, unified memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kehao Zhang, Shangtong Gui, Sheng Yang, Wei Chen, Yang Feng
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
