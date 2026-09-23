---
title: "PatchKV: Efficient KV Cache Recovery for Dynamically Edited LLM Contexts"
description: "Long-running LLM agent workflows often revise interior context spans while retaining long suffixes."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.26219) · [PDF](https://arxiv.org/pdf/2609.26219)

## 一句话摘要

Long-running LLM agent workflows often revise interior context spans while retaining long suffixes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-running LLM agent workflows often revise interior context spans while retaining long suffixes. Although suffix tokens remain unchanged, altered causal histories and rotary positions prevent exact reuse of their offloaded key-value (KV) states. Full suffix recomputation wastes prefill work, while indiscriminate reuse propagates stale states and full-precision restoration adds data movement. We present PatchKV, a profile-guided recovery system for suffix-preserving revisions. PatchKV decomposes adjacent context versions into an exact prefix, an updated span, and an aligned suffix. It predicts an edit-local dirty region using an offline length-conditioned drift model, augments this region with sparse nonlocal blocks selected from stored attention, and block-rounds their union into a fixed repair set. The remaining suffix blocks are restored from CPU memory using frozen per-block precision tags and a fused path for dequantization, RoPE correction, and KV-page placement. Across three models and three long-context question-answering workloads, PatchKV achieves a $2.51$-$3.85\times$ speedup in mean resume time-to-first-token over full suffix recomputation and a $1.26$-$2.06\times$ speedup over CacheBlend, while matching or exceeding CacheBlend's F1 score in six of nine settings and remaining within 1.36 points in the others.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guotao Yang, Rui Guo, Siwei He, Sheng Chen, Yitao Hu, Keqiu Li
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
