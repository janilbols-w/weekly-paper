---
title: "SparseEngine: Sparse-First Inference Engine"
description: "Long-context LLM agents accumulate interaction histories that strain KV-cache memory and attention computation."
---

**评分：55/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.39068) · [PDF](https://arxiv.org/pdf/2609.39068)

## 一句话摘要

Long-context LLM agents accumulate interaction histories that strain KV-cache memory and attention computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM agents accumulate interaction histories that strain KV-cache memory and attention computation. Although sparse attention reduces these costs, heterogeneous cache representations and workflows hinder integration with existing inference engines, while prior sparse-serving abstractions support only specific layouts or workflows. We present SparseEngine, a ground-up, sparse-first inference engine whose shared lifecycle contract lets each method control its KV representation and computation while coordinating state transitions with common serving infrastructure. SparseEngine supports 15 methods across four categories and enables cross-request state management through Chain Cache, which resumes KV-eviction methods from retained history, and controllable Prefix-Cache Pruning, which removes KV from selected history regions while preserving logical-prefix matching. While maintaining method quality, SparseEngine delivers over 10x higher throughput with KV eviction, over 2.5x faster decoding at matched concurrency than vLLM, and over 2x end-to-end speedup on agent benchmarks. The code is available at https://github.com/CURRENTF/SparseEngine.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Jitai Hao, Quansheng Gu, Qiang Huang, Jun Yu
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/CURRENTF/SparseEngine](https://github.com/CURRENTF/SparseEngine)
- 阅读深度：metadata
