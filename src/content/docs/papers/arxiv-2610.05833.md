---
title: "Request Order Matters: Cache-History Sensitivity in Selective KV-Cache Reuse for Rolling Agents"
description: "Long-running agents repeatedly call an LLM while retaining most of their document window, evicting old documents, and appending new ones."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.05833) · [PDF](https://arxiv.org/pdf/2610.05833)

## 一句话摘要

Long-running agents repeatedly call an LLM while retaining most of their document window, evicting old documents, and appending new ones.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-running agents repeatedly call an LLM while retaining most of their document window, evicting old documents, and appending new ones. These rolling updates break exact prefix caching and motivate non-prefix KV-cache reuse with selective recomputation. We show that persistent KV-cache reuse with selective recomputation can be history-dependent: in our rolling-agent workload, an unchanged prompt can produce different answers depending on the requests processed before it. At a matched 5% recomputation budget, document-aligned recomputation reduces answer variation across request orders from 69.0% with CacheBlend's token top-$k$ policy to 26.1%. When each prompt is evaluated after a different sequence of preceding requests, document-aligned recomputation improves fidelity to full prefill by 34.5-52.5 percentage points over token top-$k$, while both policies achieve approximately 5.7$\times$ median TTFT speedup. Our ablation study shows that, in our rolling-agent workload, contiguity is the main factor associated with robust selective recomputation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache, prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tiffany Gu, Annie Guan, Manshu Huang, Nitin Rao, Siddhant Shah, Margaret Capetz
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
