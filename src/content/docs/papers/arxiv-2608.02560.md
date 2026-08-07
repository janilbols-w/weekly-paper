---
title: "Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection"
description: "Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.02560) · [PDF](https://arxiv.org/pdf/2608.02560)

## 一句话摘要

Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token. State-Space Models (SSMs) avoid the second cost by construction; we eliminate the first, collapsing prefill from $O(L_{context})$ to $O(1)$ per query. We introduce PRECOG (Pre-Computed Context Injection), a retrieval mechanism that exploits a property unique to SSMs: the fixed-size, position-agnostic recurrent hidden state is a complete summary of everything the model has read. PRECOG pre-encodes document corpora offline as SSM hidden states and injects the best-matching state directly at query time, bypassing in-context re-ingestion entirely. The same state-injection mechanism enables SMC (Structured Memory Consolidation): a hierarchical persistent memory with cognitive-domain clustering, an adjustable fidelity-vs-storage dial, and $O(1)$ session initialization, which consolidates short-term episodic states into long-term semantic memory and fuses both with retrieved corpus states at query time. We demonstrate the system on TENNs-LLM, a 1.2B-parameter gated-SSM language model with a 192 KB hidden state. PRECOG matches in-context RAG answer quality, reducing prefill latency from $\sim$27 s to $<$6 ms on edge hardware -- a $\sim$4500$\times$ speedup that crosses the threshold from unusable to interactive. The mechanism is architecturally impossible for Transformer KV-caches, which are position-entangled and grow linearly with context length.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anusha Madan Gopal, Aras Pirbadian, Kristofor D. Carlson, M Anthony Lewis, Jonathan Tapson
- 发布：2026-08-03；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
