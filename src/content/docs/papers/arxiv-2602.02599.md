---
title: "RAP: KV-Cache Compression via RoPE-Aligned Pruning"
description: "Long-context inference in large language models (LLMs) is bottlenecked by the memory and compute of the key-value (KV) cache."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2602.02599) · [PDF](https://arxiv.org/pdf/2602.02599)

## 一句话摘要

Long-context inference in large language models (LLMs) is bottlenecked by the memory and compute of the key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context inference in large language models (LLMs) is bottlenecked by the memory and compute of the key-value (KV) cache. Structured pruning is a direct way to shrink it: dropping the least useful channels of the W_k, W_v projection weights to reduce the output KV dimensions. However, modern LLMs apply Rotary Position Embedding (RoPE) after the QK projections, which rotates feature dimensions in pairs. Therefore, removing individual channels breaks these pairs, corrupting RoPE's positional semantics and rendering the pruned model unusable. We propose RoPE-Aligned Pruning (RAP), which constrains the pruning granularity to RoPE-aligned pairs rather than individual channels: removing whole pairs to keep the rotation intact. Our evaluation across Llama, Mistral, and Qwen models from 3B to 14B shows that RAP preserves accuracy at 30% KV compression (retain ratio \r{ho} = 0.7), far outperforms RoPE-blind channel pruning, stays near the strongest low-rank method at lower attention cost, and composes with orthogonal methods such as quantization.

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

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jihao Xin, Tian Lyu, David Keyes, Hatem Ltaief, Marco Canini
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
