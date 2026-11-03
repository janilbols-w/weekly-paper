---
title: "SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions"
description: "Retrieval-Augmented Generation (RAG) systems are increasingly evolving into agentic architectures where large language models autonomously coordinate multi-step reasoning, dynamic memory management, and iterative retrieval strategies."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2603.07379) · [PDF](https://arxiv.org/pdf/2603.07379)

## 一句话摘要

Retrieval-Augmented Generation (RAG) systems are increasingly evolving into agentic architectures where large language models autonomously coordinate multi-step reasoning, dynamic memory management, and iterative retrieval strategies.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-Augmented Generation (RAG) systems are increasingly evolving into agentic architectures where large language models autonomously coordinate multi-step reasoning, dynamic memory management, and iterative retrieval strategies. Despite rapid industrial adoption, current research lacks a systematic understanding of Agentic RAG as a sequential decision-making system, leading to highly fragmented architectures, inconsistent evaluation methodologies, and unresolved reliability risks. This Systematization of Knowledge (SoK) paper provides the first unified framework for understanding these autonomous systems. We formalize agentic retrieval-generation loops as finite-horizon partially observable Markov decision processes, explicitly modeling their control policies and state transitions. Building upon this formalization, we develop a comprehensive taxonomy and modular architectural decomposition that categorizes systems by their planning mechanisms, retrieval orchestration, memory paradigms, and tool-invocation behaviors. We further analyze the critical limitations of traditional static evaluation practices and identify severe systemic risks inherent to autonomous loops, including compounding hallucination propagation, memory poisoning, retrieval misalignment, and cascading tool-execution vulnerabilities. Finally, we outline key doctoral-scale research directions spanning stable adaptive retrieval, cost-aware orchestration, formal trajectory evaluation, and oversight mechanisms, providing a definitive roadmap for building reliable, controllable, and scalable agentic retrieval systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saroj Mishra, Suman Niroula, Umesh Yadav, Dilip Thakur, Srijan Gyawali, Shiva Gaire
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
