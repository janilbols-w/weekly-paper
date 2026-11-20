---
title: "Some Memories Must Fade: Persistence and Decay of User Memories in Model Parameters"
description: "Parametric memory allows Large Language Models to internalize knowledge directly into their weights, offering a potentially powerful alternative to retrieval-based memory (RAG)."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](http://arxiv.org/abs/2611.25235v1) · [PDF](https://arxiv.org/pdf/2611.25235v1)

## 一句话摘要

Parametric memory allows Large Language Models to internalize knowledge directly into their weights, offering a potentially powerful alternative to retrieval-based memory (RAG).

## 为什么值得关注

待编辑增强。

## 摘要原文

Parametric memory allows Large Language Models to internalize knowledge directly into their weights, offering a potentially powerful alternative to retrieval-based memory (RAG). However, existing approaches to parametric memory are difficult to deploy as they largely mirror the Continual Learning (CL) objective of retaining information indefinitely. This is neither sustainable nor sufficient for a memory system, which must govern knowledge across its lifecycle by retaining stable facts, reinforcing recurring observations, updating changed beliefs, and allowing transient information to fade. We propose a system for parametric memory management consisting of a memory substrate (handling information storage and forgetting) and a learned policy (what to remember, how deeply, and for how long). Our substrate is a fixed-capacity LoRA adapter that consists of k-hot rank combinations which store facts without catastrophic interference and maintain an independently controlled temporal decay, enabling outdated information to fade while long-term facts persist. On this substrate, we train a lightweight controller that governs each incoming user event to ensure the memory system reflects the user's true, updated belief state. To evaluate how memory systems manage user memory, we introduce a controlled dataset of long-horizon user trajectories with varying persistence of facts based on changing belief states and user-behavioral shifts, and probe queries that test recall while information is valid and abstention after it expires. Our policy learns to effectively manage user memory over its entire lifecycle, balancing recall and abstention to achieve 86% of oracle performance, unlike CL and RAG baselines that primarily default to one of the two behaviors. By providing the first system to manage memory directly in model weights, this work establishes a foundation for long-horizon parametric memory.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sanidhya Vijayvargiya, Rahul Lokesh
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
