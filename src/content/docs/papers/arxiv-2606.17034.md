---
title: "KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing"
description: "Post-hoc context erasing over the KV cache is challenging because a local edit has a global consequence: once a span has been processed, its influence propagates into the cached states of all subsequent tokens."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.17034) · [PDF](https://arxiv.org/pdf/2606.17034)

## 一句话摘要

Post-hoc context erasing over the KV cache is challenging because a local edit has a global consequence: once a span has been processed, its influence propagates into the cached states of all subsequent tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-hoc context erasing over the KV cache is challenging because a local edit has a global consequence: once a span has been processed, its influence propagates into the cached states of all subsequent tokens. This issue arises naturally in long-context LLM applications, where stale, incorrect, or harmful context may be identified only after prefill. Exact erasing must then recompute all tokens after the deleted span, making its computational cost depend on suffix length rather than erased-span length. We introduce KVEraser, a learned KV-cache editing method for efficient localized context erasing. KVEraser replaces the KV states of the erased interval with learned steering states while reusing the remaining cache unchanged. To learn a transferable erasing mechanism, we use a two-stage pipeline: generic span-neighbor pre-training followed by task-specific fine-tuning. Experiments show that KVEraser nearly matches full recomputation in post-erasure performance on in-domain tasks across 1K-32K contexts, while its latency increases by only 29.6% compared with a 17.6x increase for full recomputation. KVEraser also generalizes to unseen long-document QA with harmful factual distractors and tool-selection with malicious skill-file injections, achieving the best performance among approximate baselines with a 2.9-10.7x speedup over full recomputation. Notably, full-parameter eraser training is unnecessary: a rank-16 LoRA eraser, which trains only approximately 0.6% as many parameters as the generator, performs comparably to or better than its full-parameter counterpart.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mufei Li, Shikun Liu, Dongqi Fu, Haoyu Wang, Yinglong Xia, Hong Li, Hong Yan, Pan Li
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
