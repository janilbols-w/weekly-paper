---
title: "Resource-Efficient Speculative Decoding for Long-Context LLM Serving"
description: "Speculative decoding reduces sequential Target model calls by verifying multiple tokens from the Draft model in parallel."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](http://arxiv.org/abs/2609.33184v1) · [PDF](https://arxiv.org/pdf/2609.33184v1)

## 一句话摘要

Speculative decoding reduces sequential Target model calls by verifying multiple tokens from the Draft model in parallel.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding reduces sequential Target model calls by verifying multiple tokens from the Draft model in parallel. Yet KV Cache growth limits long-context serving under constrained GPU memory. Offloading KV to CPU memory relieves this pressure. However, existing offloading schemes restore the full KV history before attention and fail to fully exploit the benefits of KV sharing across queries within a verification round. Existing parallel speculative decoding methods also overlook idle GPU compute capacity while memory-bandwidth-bound Target verification waits for historical KV. We present SpecStream, a speculative decoding system that begins verification without waiting for the full KV history to be restored and exploits compute bubbles during KV transfers for concurrent drafting on the same GPUs. It offloads only Target-committed history, keeping candidate rollback local to the GPUs. Each streamed KV chunk serves all queries in the round, with online softmax preserving full attention. Target-priority scheduling controls Draft concurrent execution under resource limits to constrain interference with Target verification. Experiments show that SpecStream maintains task quality close to SGLang speculative decoding while supporting more concurrent requests under limited GPU memory. Across different datasets, it achieves average throughput speedups of 1.41$\times$ and 1.32$\times$ over the offloading baseline for Qwen3 and InternLM2.5, respectively. Compared with parallel speculative decoding on separate Target and Draft GPUs, SpecStream improves output throughput per GPU by an average of 55.4%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fei Li, Song Liu, Shiqiang Nie, Jinyu Wang, Weiguo Wu
- 发布：2026-09-27；更新：2026-09-27
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
