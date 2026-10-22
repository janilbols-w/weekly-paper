---
title: "Accelerating CPU Speculative Decoding via Unified Graph Execution and Transactional KV Isolation"
description: "Speculative decoding accelerates LLM inference, but deploying it on CPUs introduces severe systems bottlenecks: context-swapping latency between draft and target graphs, and memory allocation overhead during KV cache rollbacks."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.28671) · [PDF](https://arxiv.org/pdf/2610.28671)

## 一句话摘要

Speculative decoding accelerates LLM inference, but deploying it on CPUs introduces severe systems bottlenecks: context-swapping latency between draft and target graphs, and memory allocation overhead during KV cache rollbacks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates LLM inference, but deploying it on CPUs introduces severe systems bottlenecks: context-swapping latency between draft and target graphs, and memory allocation overhead during KV cache rollbacks. We introduce SubTernary, an execution framework that eliminates these costs through Unified Graph Caching and Transactional KV-Cache Isolation. By compiling both models into a single memory arena with a persistent thread pool and routing speculative tokens to a static scratchpad for zero-copy pointer resets, SubTernary avoids dynamic reallocation and thread synchronization entirely. We integrate a 256-bit AVX2 ternary SIMD kernel as a low-bit case study. Ablations reveal our systems runtime drives 35.0% of the throughput gains, while the ternary kernel adds 6.0%. SubTernary achieves a $1.35\times$ speedup over llama.cpp speculative decoding and $3.99\times$ over autoregressive decoding, maintaining $O(1)$ rollback latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhangdie Yuan
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
