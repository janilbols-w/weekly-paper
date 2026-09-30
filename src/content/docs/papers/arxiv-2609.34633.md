---
title: "GenMem: Generative Symbolic Memory for Self-Evolving Harness"
description: "Long-term memory supports the self-evolution of LLM agents by retaining experience and skills across tasks and enabling their retrieval, reuse, and revision in subsequent long-horizon decision-making."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.34633) · [PDF](https://arxiv.org/pdf/2609.34633)

## 一句话摘要

Long-term memory supports the self-evolution of LLM agents by retaining experience and skills across tasks and enabling their retrieval, reuse, and revision in subsequent long-horizon decision-making.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-term memory supports the self-evolution of LLM agents by retaining experience and skills across tasks and enabling their retrieval, reuse, and revision in subsequent long-horizon decision-making. Yet existing memory management approaches remain limited to discriminative retrieval and to address the sparse, hierarchical, and highly redundant structure of reusable experience: only a small, task-dependent subset of trajectories and memories warrants retention, retrieval, or revision. Learning these operations is further complicated by sparse, delayed, and indirect task-level feedback, with weak supervision across the memory lifecycle. Moreover, continual memory evolution introduces an architectural tension as addressing invariance: stored experience is perpetually revised, yet the addressing interface consumed by learned retrieval policies must remain stable. To address, we present GenMem, which reformulates memory management as generative symbolic addressing. Its core mechanism is the Symbolic Identifier (SID), a multi-level discrete token tuple drawn from a Cartesian-product address space that factorizes a million-scale sparse memory space using fewer than one hundred discrete symbols. Instead of generating ever-changing raw content, the memory agent learns to generate SIDs, while memory evolution rewrites the payload at a fixed address without shifting the address itself. Architecturally, GenMem couples a MemRetriever and a MemEvolver within a multi-agent harness, trained via GRPO with dense process and outcome rewards with two-channels optimization. Under offline memory evolution, experiments spanning ALFWorld, WebShop, multi-hop QA, medical reasoning, and deep research evaluate GenMem against strong memory-augmented baselines...

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xinke Jiang, Tao Feng, Weixuan Xu, Zhixin Zhang, Zhibang Yang, Wentao Zhang, Runchuan Zhu, Xu Chu, Junfeng Zhao, Yasha Wang
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
