---
title: "Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective"
description: "Key-Value (KV) caching is essential for large language model inference, yet its memory overhead poses a critical bottleneck for long-context generation."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2604.25975) · [PDF](https://arxiv.org/pdf/2604.25975)

## 一句话摘要

Key-Value (KV) caching is essential for large language model inference, yet its memory overhead poses a critical bottleneck for long-context generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Key-Value (KV) caching is essential for large language model inference, yet its memory overhead poses a critical bottleneck for long-context generation. Existing eviction policies predominantly rely on empirical heuristics, lacking a rigorous theoretical foundation. This work rethinks KV cache eviction through the lens of the Information Bottleneck principle. Under a linear-Gaussian surrogate of attention, we derive a closed-form mutual information objective that characterizes the effective information capacity of a retained KV cache subset. This formulation reveals that a wide range of existing eviction strategies can be interpreted as different approximations of the same capacity-maximization principle. Guided by this insight, we introduce CapKV, a capacity-aware eviction method that directly targets information preservation via a log-determinant approximation using statistical leverage scores. This approach replaces heuristic selection with a theoretically grounded mechanism that preserves the maximum predictive signal. Extensive experiments across multiple models and long-context benchmarks show that CapKV consistently outperforms prior methods, achieving a better trade-off between memory efficiency and generational fidelity. Our code is available at https://github.com/jiamingyy/CapKV

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jiaming Yang, Chenwei Tang, Liangli Zhen, Jiancheng Lv
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/jiamingyy/CapKV](https://github.com/jiamingyy/CapKV)
- 阅读深度：metadata
