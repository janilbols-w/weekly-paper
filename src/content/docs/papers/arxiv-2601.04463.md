---
title: "Beyond Static Summarization: Proactive Memory Extraction for LLM Agents"
description: "Memory management is vital for LLM agents in long-term and personalized interactions."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2601.04463) · [PDF](https://arxiv.org/pdf/2601.04463)

## 一句话摘要

Memory management is vital for LLM agents in long-term and personalized interactions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Memory management is vital for LLM agents in long-term and personalized interactions. Most previous work studies how to retrieve and use memory, but pays less attention to how memory is extracted. We find two main limitations in existing methods. First, extraction is "ahead-of-time": the agent saves information before it knows future tasks. A single summary prompt often mixes details, events, and relations, so useful information is lost. Second, extraction is usually one-off. Without verification, errors and hallucinations may stay in memory for a long time. To address these limitations, we propose ProMem, a proactive memory extraction framework. It separates details, events, and relations, and uses different extraction strategies for each type. It also checks completeness to recover missed events and verifies facts at the atomic level to reduce hallucinations. Experiments show that ProMem improves memory completeness and QA accuracy, while keeping a good balance between quality and token cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chengyuan Yang, Zequn Sun, Wei Wei, Wei Hu
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
