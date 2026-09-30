---
title: "Does Execution Require Target KV Fidelity? A Mixed-Fidelity KV Runtime for LLM Serving"
description: "Large language model (LLM) serving is increasingly constrained by the GPU memory consumed by key-value (KV) caches."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.33536) · [PDF](https://arxiv.org/pdf/2609.33536)

## 一句话摘要

Large language model (LLM) serving is increasingly constrained by the GPU memory consumed by key-value (KV) caches.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving is increasingly constrained by the GPU memory consumed by key-value (KV) caches. Existing compression, eviction, and offloading techniques alleviate this pressure, but serving runtimes typically treat only the configured target KV representation as execution-ready. Under memory pressure, this target-only contract can turn KV shortage into request stalls and preemptions. We present ElasticKV, a mixed-fidelity KV runtime built on the observation that target fidelity need not gate execution. ElasticKV introduces a compact intermediate KV state, making fidelity a runtime-managed execution property. To realize this state in a paged serving runtime, ElasticKV combines (i) a pair-structured layout that turns fidelity reduction into reusable GPU capacity, (ii) a dual-mode attention backend that directly consumes the compact state while preserving the native target-only path, and (iii) pressure-aware fidelity management that adapts KV fidelity to memory pressure. Our extensive evaluation across diverse workloads, model families and scales, and GPU platforms demonstrates the effectiveness and generality of ElasticKV. Under high concurrency, ElasticKV achieves 3.8-4.0$\times$ lower time-to-first-token (TTFT) and 9.1$\times$ lower P90 TTFT than vLLM while preserving generation quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving, serving runtime
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiantong Jiang, Yue Yang, Peiyu Yang, Feng Liu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
