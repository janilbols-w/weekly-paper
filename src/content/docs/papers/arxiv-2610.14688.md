---
title: "Accelerating Cross-Model LLM Inference via Attention Map Reuse"
description: "LLM-augmented data workflows often involve multiple heterogeneous models operating over substantial shared context, such as schemas, tool specifications, interaction history, and intermediate results."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.14688v1) · [PDF](https://arxiv.org/pdf/2610.14688v1)

## 一句话摘要

LLM-augmented data workflows often involve multiple heterogeneous models operating over substantial shared context, such as schemas, tool specifications, interaction history, and intermediate results.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-augmented data workflows often involve multiple heterogeneous models operating over substantial shared context, such as schemas, tool specifications, interaction history, and intermediate results. Although prefix caching can reduce prefilling overhead, existing approaches are largely limited to reuse within the same model because KV states are tightly coupled to model-specific architectures. We present MapFlow, a system for efficient heterogeneous LLM serving via cross-model attention map reuse. Instead of reusing KV states, MapFlow reuses attention maps, which capture token dependency patterns and are more transferable across models. To enable efficient and accurate reuse, we combine partial recomputation with lightweight linear translation across layers and heads. To make attention reuse practical for long contexts, we further introduce block-level sparse compression and a fused retrieval kernel. Experiments show that MapFlow reduces prefilling latency and improves end-to-end serving efficiency while preserving generation quality across heterogeneous model pairs and multi-turn routing workloads. These results suggest that attention maps provide an effective reusable state for heterogeneous LLM serving, especially in prefix-heavy data workflows. Our code is available: https://github.com/PKU-DAIR/MapFlow.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 6 |

## 证据与限制

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhan Jin, Yuze Luo, Bin Cui, Xupeng Miao
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：SIGMOD 2027
- 代码：[https://github.com/PKU-DAIR/MapFlow](https://github.com/PKU-DAIR/MapFlow)
- 阅读深度：metadata
