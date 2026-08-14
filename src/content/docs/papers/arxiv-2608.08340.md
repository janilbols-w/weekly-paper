---
title: "OpRAG: A Resource-Deterministic Runtime for GPU-Backed Multi-Stage RAG Workflows"
description: "Agentic retrieval-augmented generation (RAG) systems combine preprocessing, embedding, retrieval, memory access, context construction, generation, and vector-index updates."
---

**评分：43/100** · AI 基础设施 > 集群与资源系统 > 存储与数据平面

[论文原文](https://arxiv.org/abs/2608.08340) · [PDF](https://arxiv.org/pdf/2608.08340)

## 一句话摘要

Agentic retrieval-augmented generation (RAG) systems combine preprocessing, embedding, retrieval, memory access, context construction, generation, and vector-index updates.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic retrieval-augmented generation (RAG) systems combine preprocessing, embedding, retrieval, memory access, context construction, generation, and vector-index updates. Although LLM decoding is GPU-bound, the surrounding orchestration layer can still limit end-to-end performance through serialization overhead, fragmented scheduling, inefficient batching, and CPU--GPU pipeline stalls. Existing frameworks provide flexible control flow, while distributed runtimes provide scalable task parallelism, but neither exposes RAG stages as resource-aware operators with deterministic execution semantics. We present OpRAG, a resource-deterministic distributed runtime for GPU-backed multi-stage RAG workflows. OpRAG models embedding, retrieval, reasoning, memory, and upsert as first-class operators and lowers them into communication-aware execution graphs. It combines an Arrow zero-copy data plane, persistent workers, bounded queues, CPU tokenizer prefetching, batched GPU embedding, and overlapped retrieval/generation execution to reduce non-model overhead around LLM inference. We evaluate OpRAG using Llama3-8B and Mistral-7B with FlashAttention~2, BF16 execution, and 32K RAG chunks. In end-to-end GPU pipeline experiments, OpRAG improves over the nearest competitor by 16.16% for Llama3-8B and 15.66% for Mistral-7B, and over RayScalableRAG by 20.57% and 20.71%, respectively. Against LangChain, LangGraph, CrewAI, and AutoGen, OpRAG is 17.77% and 17.48% faster than the best framework baseline. In Higress-style query serving, OpRAG reduces hybrid retrieval latency by 59.20--59.62% and generation-scenario latency by 52.48--53.55%, while preserving 100% Recall@5. These results show that optimizing the distributed orchestration layer can substantially improve GPU-backed multi-stage RAG without modifying the LLM decoding kernel.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: data plane
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Arup Kumar Sarker, Mills Staylor, Aymen Alsaadi, Gregor von Laszewski, Shantenu Jha, Geoffrey Fox
- 发布：2026-08-08；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
