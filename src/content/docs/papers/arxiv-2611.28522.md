---
title: "DisSparse: Pipelined Top-$p$ Sparse Attention for Long-Context LLM Serving"
description: "Long-context LLM inference is bottlenecked by the memory demands of the key-value (KV) cache, whose size scales linearly with context length."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.28522) · [PDF](https://arxiv.org/pdf/2611.28522)

## 一句话摘要

Long-context LLM inference is bottlenecked by the memory demands of the key-value (KV) cache, whose size scales linearly with context length.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM inference is bottlenecked by the memory demands of the key-value (KV) cache, whose size scales linearly with context length. Dynamic sparse attention reduces this bottleneck by fetching and attending only to a critical subset of tokens. The dominant primitive in dynamic sparse attention research and deployment is fixed-budget top-$k$ selection, which is favored because its deterministic block count aligns with the static memory allocation that systems like vLLM rely on. Top-$k$ uses a fixed budget regardless of how attention mass is distributed across heads, layers, and decode steps, leading to either wasted bandwidth on heads with peaky attention or dropped context on heads with diffuse attention. Top-$p$ (nucleus) selection adapts naturally to this variation but has seen limited adoption in production serving systems due to two system-level challenges: variable block counts that break deterministic block allocation and computationally expensive selection kernels that exceed the cost of attention itself. We present DisSparse, a serving system that integrates top-$p$ sparse attention into vLLM end-to-end. DisSparse decouples block selection from the scheduler's critical path, hides selection latency behind layer computation via a two-stream pipeline, and introduces a single-pass histogram-based top-$p$ kernel. We further observe intra-block sparsity, the inflation of selection budgets caused by mixing high- and low-importance tokens within fixed-size KV cache blocks, and address it with a token relocation kernel guided by accumulated prefill attention scores. Across long- and medium-context benchmarks on multiple models, DisSparse achieves 1.17x to 1.80x speedup in sparsity analysis (block selection) over state-of-the-art top-$p$ methods with negligible accuracy loss and supports up to 8x larger maximum batch sizes than dense vLLM under the same memory budget.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Nurlan Nazaraliyev, Elaheh Sadredini, Nael Abu-Ghazaleh
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
