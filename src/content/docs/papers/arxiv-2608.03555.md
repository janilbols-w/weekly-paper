---
title: "Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention"
description: "This paper presents a heterogeneous decode-phase serving system that relocates the KV cache out of GPU memory, motivated by the retrieval-based sparse attention that recent frontier LLMs adopt to serve million-token contexts."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.03555) · [PDF](https://arxiv.org/pdf/2608.03555)

## 一句话摘要

This paper presents a heterogeneous decode-phase serving system that relocates the KV cache out of GPU memory, motivated by the retrieval-based sparse attention that recent frontier LLMs adopt to serve million-token contexts.

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper presents a heterogeneous decode-phase serving system that relocates the KV cache out of GPU memory, motivated by the retrieval-based sparse attention that recent frontier LLMs adopt to serve million-token contexts. It partitions a decode step by operation type: GPU nodes hold the model weights and execute the projections and MoE layers, while processing-near-memory (PNM) nodes hold the KV cache and index keys and execute every operation that reads them. We first show that the assumptions behind prior PIM and PNM designs no longer hold for these operations, and derive four design requirements for such a node. From these requirements, we propose KARAT (KV-cache-resident Accelerator for Retrieval-based ATtention), a general-purpose PNM design that is the design point meeting all four. A KARAT device combines large LPDDR capacity with general-purpose compute sized for the retrieval indexer, serving an operational intensity beyond what PIM/PNM designs built for low-intensity GEMV target while accommodating diverse sparse attention algorithms that fixed-function units cannot support as they evolve. To reduce pipeline bubbles as the two device types alternate between micro-batches, we further propose opportunistic, fine-grained micro-batch scheduling (OFMS), which hides expert all-to-all behind the other micro-batch's GEMMs, and context-length-aware micro-batch rebalancing (CMR), which equalizes their token counts despite the variance in context length. Across three state-of-the-art models and real agentic traces, our proposed system improves throughput per TDP under a service-level objective by 2.09-6.13x over a GPU-only baseline and runs training-free sparse attention methods with 1.36-3.21x improvements.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hyungkyu Ham, Junhyeong Bae, Seungheon Lee, Myeongjae Jeon, Gwangsun Kim
- 发布：2026-08-04；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
