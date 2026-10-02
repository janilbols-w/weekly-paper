---
title: "ATTUNER: Recomputation-Free KV Cache Reuse via Query-Side Adaptation"
description: "Large language model (LLM) agents repeatedly load reusable content, such as skills, documents, and memory entries, into the current context."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.36722) · [PDF](https://arxiv.org/pdf/2609.36722)

## 一句话摘要

Large language model (LLM) agents repeatedly load reusable content, such as skills, documents, and memory entries, into the current context.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) agents repeatedly load reusable content, such as skills, documents, and memory entries, into the current context. Re-encoding this content for every request wastes computation. Position-independent caching (PIC) alleviates this by encoding each artifact independently and reusing its key-value (KV) states at arbitrary positions, but it incurs a quality loss relative to full-context prefill. Existing methods repair this loss by restoring global position IDs or recomputing selected tokens. In this work, we isolate the source of the loss, finding that the positional mismatch has minor effect, and independently cached artifacts retain faithful representations: reading a provided artifact stays largely accurate, and performance degrades only when the model must select among multiple artifacts. Moreover, replacing PIC's attention scores with full-prefill scores recovers performance with the cached KV unchanged, localizing the failure to the attention rather than KV recomputation. Motivated by this, we propose \textsc{Attuner}, a query-side adaptation method that learns to read a frozen artifact cache. \textsc{Attuner} inserts low-rank adapters into the query projections and is trained by distilling full-prefill distribution into the student. It trains fewer than 0.05\% of the model parameters and, at inference, requires neither cache recomputation nor a full-context reference. On Qwen3-4B and Qwen3-8B across seven benchmarks covering skills, documents, memory, and code, \textsc{Attuner} substantially outperforms prior PIC baselines in both in-domain and out-of-domain settings, matches full-context prefill quality while providing up to $3.73\times$ speedup.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xinghao Chen, Junnan Dong, Cai Ke, Chak Tou Leong, Haocheng Sun, Keyu Chen, Siyu An, Ruizhi Qiao, Xing Sun, Wenjie Li, Xiaoyu Shen
- 发布：2026-09-29；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
