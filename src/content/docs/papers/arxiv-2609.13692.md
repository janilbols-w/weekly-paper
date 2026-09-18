---
title: "Prefix Sharing Is a Sorting Problem"
description: "LLM serving reuses KV cache by exact prefix match, so when a prompt is assembled from a set of reusable pieces -- retrieved passages, tool definitions, few-shot exemplars -- the order chosen for those pieces determines how much computation can be shared."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2609.13692v1) · [PDF](https://arxiv.org/pdf/2609.13692v1)

## 一句话摘要

LLM serving reuses KV cache by exact prefix match, so when a prompt is assembled from a set of reusable pieces -- retrieved passages, tool definitions, few-shot exemplars -- the order chosen for those pieces determines how much computation can be shared.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM serving reuses KV cache by exact prefix match, so when a prompt is assembled from a set of reusable pieces -- retrieved passages, tool definitions, few-shot exemplars -- the order chosen for those pieces determines how much computation can be shared. Every deployed system fixes that order by a single global convention. We prove this is optimal only when requests contain at most two pieces, and asymptotically wrong in general. Our main result is a structure theorem: the minimum prefix-trie cost equals min_H sum_x w(x) t_x(H) over binary hierarchies H on the requests, where t_x(H) is the canonical decomposition size of the set of requests needing chunk x. Choosing chunk orders is therefore equivalent to choosing one hierarchy over requests. The identity yields an O(3^m) exact algorithm, identifies the two-chunk case as minimum vertex cover, and shows that on the leave-one-out family the optimum is the minimum external path length of a binary tree -- the merge-sort recursion -- so a global order pays Theta(n^2) against a true cost of Theta(n log n). Agglomerative clustering by common intersection is a tight 1/2-approximation for the achievable saving. On BM25 retrieval traces over three BEIR corpora the resulting layout reduces prefill by 17-36% against production RAG ordering, and the margin widens with retrieval depth as the theory predicts. Serving requests in the hierarchy's DFS order finally lets a cache holding one request's context attain the unbounded-cache optimum exactly, so cache capacity and reorder window act as substitutes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Rong He
- 发布：2026-09-12；更新：2026-09-12
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/Darrenus/prefix-sharing-is-sorting](https://github.com/Darrenus/prefix-sharing-is-sorting)
- 阅读深度：metadata
