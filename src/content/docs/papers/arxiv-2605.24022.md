---
title: "Adaptive KV Cache Reuse for Fast Long-Context LLM Serving"
description: "In long-context Large Language Model (LLM) inference, the Time-To-First-Token (TTFT) latency incurred by the prefill stage has become the foremost bottleneck limiting interactive performance and deployment cost."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.24022) · [PDF](https://arxiv.org/pdf/2605.24022)

## 一句话摘要

In long-context Large Language Model (LLM) inference, the Time-To-First-Token (TTFT) latency incurred by the prefill stage has become the foremost bottleneck limiting interactive performance and deployment cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

In long-context Large Language Model (LLM) inference, the Time-To-First-Token (TTFT) latency incurred by the prefill stage has become the foremost bottleneck limiting interactive performance and deployment cost. KV Cache reuse offers a direct path to reduce redundant prefill, yet traditional prefix caching applies only to strict-prefix scenarios; directly reusing KV Cache in non-prefix settings breaks the cross-chunk global attention relationships and causes significant degradation in generation quality. When reusable KV Cache is offloaded to GPU-external cache pools, I/O overheads across heterogeneous hardware tiers further emerge as a new TTFT bottleneck. Efficient non-prefix KV Cache reuse therefore requires both semantic-consistency recovery and compute-I/O co-optimization. This paper presents CacheTune, a frequency-guided and hardware-aware KV Cache reuse system for long-context LLM serving. CacheTune first identifies, offline, the KV pairs most critical to cross-attention recovery through frequency-domain analysis, and then selectively recomputes only these semantic-critical tokens online while reusing the remaining KVs. To turn this semantic selection into end-to-end latency reduction, CacheTune further combines sparse KV transfer, multi-stream asynchronous overlap, deferred positional-encoding recovery, and hardware-aware adaptive recomputation-ratio tuning to balance computation and data movement across heterogeneous cache pools. Evaluations on mainstream LLMs and long-context tasks show that CacheTune achieves 3.72x-4.86x TTFT speedup and 3.93x-6.21x higher throughput while maintaining generation quality close to full recompute. Even when caches are offloaded to I/O-bound SSD/HDD storage, CacheTune sustains 2.34x-2.36x TTFT speedup through adaptive recomputation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, prefix caching
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Fei li, Song Liu, Yan Liu, Jinhua Cui, Shiqiang Nie, Jinyu Wang, Weiguo Wu
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
