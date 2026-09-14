---
title: "RoofLang: Enabling AI-Driven Architecting of LLM Inference Systems"
description: "AI is beginning to make substantive contributions to LLM inference optimization."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.12551) · [PDF](https://arxiv.org/pdf/2609.12551)

## 一句话摘要

AI is beginning to make substantive contributions to LLM inference optimization.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI is beginning to make substantive contributions to LLM inference optimization. Existing AI optimizations are predominantly profiling-based. Profiling-bound feedback confines the search to the capabilities and performance of an existing software stack, preventing a fundamentally better architecture of LLM inference systems from being identified. To enable the AI-driven LLM inference system architecting loop, we argue that a general workload representation, a verifiable mutation space, and an implementation-independent evaluator are required. We present the RoofLang domain-specific language (DSL) that provides these features. In our evaluation, RoofLang reveals that DeepSeek V4-series models could achieve 3.5-39.5$\times$ higher peak decode throughput than other representative models. This gap is disproportionate to their total parameter counts and arises largely from compact KV-cache designs that support larger batches and reduce memory traffic. A persistent optimizer agent further discovered several new architectures that improved both throughput and interactivity of DeepSeek V4 Pro on NVIDIA B300 by 6.23-50.1%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ziyue Yang, Yuting Jiang, Lei Qu, Peng Cheng
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
