---
title: "ARM: Attention with Routed-Memory for Learnable Sparse Control"
description: "Despite advances in long-context inference, large language models (LLMs) remain fundamentally limited by the key-value (KV) caching mechanisms that are necessary for stable computation."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.24417) · [PDF](https://arxiv.org/pdf/2609.24417)

## 一句话摘要

Despite advances in long-context inference, large language models (LLMs) remain fundamentally limited by the key-value (KV) caching mechanisms that are necessary for stable computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Despite advances in long-context inference, large language models (LLMs) remain fundamentally limited by the key-value (KV) caching mechanisms that are necessary for stable computation. Techniques such as selective token eviction and pruning have vastly mitigated these issues, but often discard core information to manage the growing cache. In this paper, we propose Attention with Routed Memory (ARM) a novel KV caching structure that introduces a fully differentiable, fixed-size memory system organized as a hierarchical router. Via a Gumbel-Softmax, ARM learns to select memory slots and perform sigmoid-gated updates that softly combine new and stored information, avoiding hard eviction and reducing information loss. By further training a policy to dynamically select varying amounts of memory at inference, ARM adapts its accesses for both simple contexts and inputs that require deeper reasoning, enabling more scalable and effective retrieval on both short- and long-contexts. Experimental results on standard commonsense and long-context reasoning benchmarks demonstrate that ARM achieves superior performance and efficiency compared to fixed KV-caching approaches, while remaining efficient and scalable in terms of both memory and generation latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qiuhao Zeng, Jerry Huang, Peng Lu, Ruiyi Fang, Gezheng Xu, Zihao Jing, Yufei Cui, Charles Ling, Gang Niu, Boyu Wang
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
