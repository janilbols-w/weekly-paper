---
title: "LoopCache: Accelerating Long-Context Self-Speculative Decoding for Looped Transformers"
description: "Looped Transformers achieve large effective depth with compact models by repeatedly applying a weight-shared block across R recurrent steps, each maintaining a loop-specific key-value (KV) cache."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.24301) · [PDF](https://arxiv.org/pdf/2611.24301)

## 一句话摘要

Looped Transformers achieve large effective depth with compact models by repeatedly applying a weight-shared block across R recurrent steps, each maintaining a loop-specific key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped Transformers achieve large effective depth with compact models by repeatedly applying a weight-shared block across R recurrent steps, each maintaining a loop-specific key-value (KV) cache. To accelerate sequential loop execution, recent wave-style self-speculative methods like WaveFront Decoding (WFD) and LoopSpec pipeline draft and target tokens across loops in a single step. However, they face two critical limitations. First, they draft only at fixed loops and ignore intermediate prediction changes, wasting computation on stale trajectories. Second, batching tokens from different loops loads up to Rx the KV cache per step, severely amplifying memory traffic in long-context scenarios. To address these challenges, we propose LoopCache, an efficient self-speculative decoding framework for long-context Looped Transformers. Based on the correlation between prediction switches and output confidence, LoopCache introduces confidence-guided dynamic draft updating to refine drafts in flight across all intermediate loops. Furthermore, LoopCache employs a cyclic loop KV cache strategy that rotates through loop-specific KV caches, restricting per-step KV traffic to a single loop while batching tokens at the nearest matching cycle for lossless verification. By also selectively retaining independent KV caches for a few loop-sensitive shallow layers, LoopCache improves acceptance rates with negligible overhead. Experiments show that LoopCache achieves average 10.25x and 14.56x speedup over WFD and LoopSpec.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zizhuo Fu, Haochen Huang, Shengxuan Qiu, Linye Wei, Ziyu Tang, Runsheng Wang, Meng Li
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
