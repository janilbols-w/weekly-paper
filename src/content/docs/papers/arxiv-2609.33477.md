---
title: "Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs"
description: "Hybrid LLMs interleave full-attention layers with linear-attention layers to reduce long-context inference cost, but this structure complicates prefix caching."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2609.33477v1) · [PDF](https://arxiv.org/pdf/2609.33477v1)

## 一句话摘要

Hybrid LLMs interleave full-attention layers with linear-attention layers to reduce long-context inference cost, but this structure complicates prefix caching.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid LLMs interleave full-attention layers with linear-attention layers to reduce long-context inference cost, but this structure complicates prefix caching. Full-attention KV caches are token-addressable, whereas linear-attention layers maintain recurrent states that cannot be rolled back to arbitrary prefix boundaries. Existing systems materialize recurrent-state checkpoints, restricting prefix reuse to checkpoint-aligned positions. We present SuffixReplay, the first prefix caching system that lets hybrid LLMs reuse cached prefixes at every cache-supported page boundary without materializing recurrent-state checkpoints. Our key insight is to just let linear states forget the distant past. Modern linear-attention mechanisms use recurrent decay and gating to attenuate the influence of old inputs. Therefore, instead of checkpointing every prefix boundary, SuffixReplay approximates the state at a matched boundary by replaying only a recent suffix of the layer's input hidden states, which we retain as anchors. At the algorithmic level, SuffixReplay combines layer-wise and token-wise anchor sparsity with a bounded replay budget to control storage, computation, and quality. At the system level, it uses an independently managed anchor sidecar and a pipelined replay path to overlap anchor movement and state reconstruction with the native serving pipeline. We evaluate SuffixReplay on three hybrid LLMs: OLMo-Hybrid-7B, Qwen3.5-4B, and Qwen3.6-27B-FP8. Across these models, SuffixReplay retains 91.4-100% of full-prefill quality on average across LongBench and RULER, while using only 0.36-0.51x the amortized per-token storage of SGLang's default 8192-token checkpoint cache. Integrated into SGLang, SuffixReplay reduces median TTFT by 15-70% on branching workloads, sustains 2.3-4.3x SGLang's throughput when the working set exceeds HBM, and matches SGLang on high-hit continuation traffic.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yirui Liu, Ruoling Qi, Xuaner Wu, Yuxin Jin, Jian Chen, Penghang Liu, Yafei Huang, Jiawei Shao, Xuelong Li
- 发布：2026-09-27；更新：2026-09-27
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
