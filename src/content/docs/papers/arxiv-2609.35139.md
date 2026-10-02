---
title: "CacheRepair: Learning to Repair Cross-Chunk Context in RAG for KV Cache Fusion"
description: "Multi-document retrieval-augmented generation (RAG) requires a language model to process multiple retrieved text chunks before answering a question."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.35139) · [PDF](https://arxiv.org/pdf/2609.35139)

## 一句话摘要

Multi-document retrieval-augmented generation (RAG) requires a language model to process multiple retrieved text chunks before answering a question.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-document retrieval-augmented generation (RAG) requires a language model to process multiple retrieved text chunks before answering a question. Precomputing each chunk's KV cache independently and concatenating the caches when the chunks are retrieved can accelerate this step. However, the assembled cache lacks cross-chunk attention information, reducing answer quality. Selective recomputation methods recover the missing cross-chunk context by rerunning the target LLM on selected tokens, incurring substantial online computation. We introduce CacheRepair, a lightweight network that learns the difference between independently computed KV caches and those produced by processing the chunks together. The network combines compressed KV features with token embeddings and uses attention that is bidirectional within each chunk and flows from earlier to later chunks. Each repair block receives the compressed cache features, and the predicted residual is added to every document token's cache. Each repair network is trained for a specific frozen target LLM on a generic retrieval corpus and reused across downstream datasets. Our analysis shows that repair reduces KV errors both near chunk boundaries and throughout chunk interiors. Evaluation across three target LLMs and four downstream datasets places CacheRepair on the measured answer-quality-latency Pareto frontier in eleven of twelve model-dataset combinations. Reported time to first token (TTFT) includes online cache transfer and repair. Across all twelve combinations, the largest repairers achieve 1.69-4.61$\times$ speedups in median TTFT over full prefill and improve mean F1 by 2.1-26.1 percentage points over direct cache reuse.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Genglin Wang, Wangsong Yin, Yeerzhati Abudunuer, Haoxuan Xu, Guoliang Xing, Zhenyu Yan
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
