---
title: "From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models"
description: "Long-context capability has become essential for large language models (LLMs) to handle complex tasks, yet continuously expanding the context window does not remove the computational, storage, and information-selection pressures incurred at inference time."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.21165) · [PDF](https://arxiv.org/pdf/2610.21165)

## 一句话摘要

Long-context capability has become essential for large language models (LLMs) to handle complex tasks, yet continuously expanding the context window does not remove the computational, storage, and information-selection pressures incurred at inference time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context capability has become essential for large language models (LLMs) to handle complex tasks, yet continuously expanding the context window does not remove the computational, storage, and information-selection pressures incurred at inference time. Existing work on prompt compression, KV-cache management, efficient serving, retrieval augmentation, and agent memory is usually discussed in isolation, leaving the flow of information between storage and computation insufficiently understood. This survey reframes long-context compression as a memory-management problem for allocating inference-time resources. We distinguish compute-active memory, which directly participates in model computation, from compute-inactive memory, which lies outside the computation path but can be stored, retrieved, updated, or forgotten, and we characterize offloaded KV caches, persistent prefix caches, and precomputed KV states as intermediate states on the activation path. On this basis, we formulate writing, offloading, recall, retrieval-and-injection, materialization, eviction, consolidation, and forgetting as state transitions within an information lifecycle, and introduce a budgeted cost model that places these operations in a single cost account. The resulting framework unifies short-term context compression, long-term memory management, and the transitions between them, and shows that the central challenge is not merely reducing information volume but deciding which information should participate in costly inference, when, and in what form. We further summarize evaluation dimensions, benchmark gaps, and open challenges, and argue that future research should move from static, pointwise compression toward dynamic, governable, lifecycle-aware memory management.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management, offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chaogui Gou
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
