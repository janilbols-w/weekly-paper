---
title: "Not All Memories Are Equal: Hierarchical Collaborative Memory for Validity-Aware Retrieval in LLM Agents"
description: "In team collaboration scenarios, memory is heterogeneous and continually evolving."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.30289) · [PDF](https://arxiv.org/pdf/2609.30289)

## 一句话摘要

In team collaboration scenarios, memory is heterogeneous and continually evolving.

## 为什么值得关注

待编辑增强。

## 摘要原文

In team collaboration scenarios, memory is heterogeneous and continually evolving. Team memories capture collective decisions, protocols, and current consensus, while individual memories preserve member-specific observations, execution traces, and intermediate progress. Existing memory-augmented systems typically retrieve from all stored memories as a flat pool, ranking them by semantic relevance, importance, or recency without modeling hierarchical structure or evolving validity. As a result, they often surface semantically relevant but outdated or conflicting memories, especially individual memories that no longer align with current team consensus, instead of prioritizing currently valid memories. This is particularly problematic when collaborative LLM agents answer user questions, since their responses should be grounded in valid memories. We propose HiCoMER, a framework for hierarchical collaborative memory management and validity-aware retrieval in LLM agents. HiCoMER first maintains the validity of team and individual memories and then retrieves memories that remain valid, rather than retrieving directly from all stored memories. It consists of three components: a Hierarchical Memory Conflict Updater, a Validity-Aware Memory Retriever, and a Memory-Grounded Answer Generator. To evaluate HiCoMER, we construct two new datasets for memory-grounded question answering in collaborative settings. Experiments on both datasets show that HiCoMER consistently outperforms strong baselines by reducing outdated retrieval, preserving current team consensus, and improving downstream QA quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yufei Shi, Rujing Yao, Ang Li, Yang Wu, Zhuoren Jiang, Xiaozhong Liu
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
