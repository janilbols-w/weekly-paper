---
title: "Uncovering the Memory Hierarchy of Modern NVIDIA GPUs for Accurate Simulation"
description: "Emerging artificial intelligence workloads, particularly Large Language Models (LLMs), place unprecedented demands on GPU memory systems."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.13860) · [PDF](https://arxiv.org/pdf/2611.13860)

## 一句话摘要

Emerging artificial intelligence workloads, particularly Large Language Models (LLMs), place unprecedented demands on GPU memory systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Emerging artificial intelligence workloads, particularly Large Language Models (LLMs), place unprecedented demands on GPU memory systems. Consequently, architectural innovations increasingly target the memory system to alleviate these bottlenecks. However, existing works still rely on outdated memory hierarchy models that fail to capture the complexities of modern hardware. This fidelity gap leads to inaccurate characterization and could misguide optimization strategies. To bridge this gap, we present GemAtlas, the first systematic reverse engineering of the memory hierarchy in modern NVIDIA GPUs. By developing fine-grained SASS-level benchmarking, we expose critical, previously undocumented micro-architectural details across different cache levels, including cache set associativity, slice-routing and set-indexing hash functions, replacement policies, coherence behavior, and interconnect topologies. We integrate these discovered micro-architecture details into the state-of-the-art GPU simulation framework. The final results demonstrate that GemAtlas reduces the mean absolute percentage error (MAPE) from 31.69% to 22.24% on average across four GPUs. Specifically, GemAtlas reduces the MAPE from 34.04% to 23.98% for real-world LLM operators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ziwen Wang, Jiapeng Zhou, Changxi Liu, Dongsheng Wang, Yun Chen
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
