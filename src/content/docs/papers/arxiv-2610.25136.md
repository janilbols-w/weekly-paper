---
title: "Visual Cache Reuse for Efficient Multimodal Inference"
description: "Vision-language model (VLM) inference incurs substantial prefill latency and memory overhead due to the long visual token sequences of large visual inputs."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.25136) · [PDF](https://arxiv.org/pdf/2610.25136)

## 一句话摘要

Vision-language model (VLM) inference incurs substantial prefill latency and memory overhead due to the long visual token sequences of large visual inputs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language model (VLM) inference incurs substantial prefill latency and memory overhead due to the long visual token sequences of large visual inputs. Existing serving systems typically exploit exact cache reuse through prefix caching or position-independent caching, overlooking the potential of approximate caching in real-world workloads. However, directly reusing an approximate cache entry may introduce spurious visual information, which naive approaches that select a subset of important visual tokens for recomputation fail to adequately mitigate this risk. We present VisMemo, an efficient serving system that enables approximate KV cache reuse for modern VLMs. Its core is a system-algorithm co-design that combines an entropy-aware KV cache reuse algorithm with differentiated cache management. Specifically, VisMemo uses patch entropy to identify reuse candidates and warmup attention to prioritize recomputation based on the current query. To support the large cache capacity across GPU memory, CPU memory, and SSD storage, VisMemo applies distinct I/O and cache policies to exact and approximate hits: sparse patch-level I/O for approximate hits, prioritized retention for exact hits, and a reserved CPU victim cache for preset entries selected using offline workload priors and online reuse observations. VisMemo further optimizes the memory access path between the inference engine and the storage backend, eliminating redundant caching and unnecessary data movement. Experiments on multiple public datasets show that VisMemo preserves output quality under approximate reuse. On a real-world production trace, VisMemo increases the overall cache hit rate from 27.78% to 61.45% and reduces prefill latency by up to 48.3% at 8K input tokens.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shuheng Gao, Yuankai Fan, Jiaqiang Ma, Jiawei Shao, Yongkun Li, Xuelong Li
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
