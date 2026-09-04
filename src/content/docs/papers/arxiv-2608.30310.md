---
title: "Tail-Replay: Escaping the Curse of Linear Attention in Prefix Caching for Hybrid LLMs"
description: "Hybrid large language models interleave full-attention layers with linear-attention layers to reduce the cost of long-context inference."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.30310) · [PDF](https://arxiv.org/pdf/2608.30310)

## 一句话摘要

Hybrid large language models interleave full-attention layers with linear-attention layers to reduce the cost of long-context inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid large language models interleave full-attention layers with linear-attention layers to reduce the cost of long-context inference. This structure complicates prefix caching: full-attention key-value caches are token-addressable, whereas linear-attention layers maintain recurrent states that cannot be rolled back to arbitrary prefix boundaries. Existing hybrid prefix caching methods address this mismatch by storing recurrent-state checkpoints. As a result, token-level matches are directly usable only at positions aligned with stored checkpoints, constraining prefix reuse to a discrete set of boundaries. We present Tail-Replay, a prefix caching mechanism that enables unconstrained token-level prefix reuse in hybrid large language models. The key insight is that linear-attention mechanisms such as Gated DeltaNet can be viewed as a structured, lossy compression of the input prefix: gated recurrent updates progressively attenuate the contributions of earlier inputs. Consequently, the recurrent state of a matched prefix can be well approximated by replaying only a short, recent suffix of that prefix. Tail-Replay exploits this property by caching the exact full-attention key-value cache while omitting recurrent-state checkpoints. On a cache hit, it reconstructs the linear-attention states by replaying a short, recent suffix of the matched prefix. As a result, the reuse boundary is determined by the shared tokens rather than by recurrent-state checkpoints. We evaluate Tail-Replay on three Gated DeltaNet-based hybrid models using the LongBench and RULER benchmarks. With only a 5--10\% replay budget, it retains 92.8--99.9\% of full-prefill quality on LongBench and RULER. For serving efficiency, we evaluate time-to-first-token speedups across multiple matched-prefix lengths---8K, 16K, and 32K. The speedup grows with prefix length, reaching $9.1$--$14.3\times$ over full prefill at 32K.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yirui Liu, Ruoling Qi, Xuaner Wu, Penghang Liu, Jian Chen
- 发布：2026-08-31；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
