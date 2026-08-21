---
title: "ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents"
description: "Agentic language models repeatedly encode tool and skill schemas that recur across requests in different combinations and orders, preventing standard prefix caching from reusing their key--value (KV) states."
---

**评分：57/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.19662) · [PDF](https://arxiv.org/pdf/2608.19662)

## 一句话摘要

Agentic language models repeatedly encode tool and skill schemas that recur across requests in different combinations and orders, preventing standard prefix caching from reusing their key--value (KV) states.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic language models repeatedly encode tool and skill schemas that recur across requests in different combinations and orders, preventing standard prefix caching from reusing their key--value (KV) states. We introduce \textbf{ReCache}, a framework for independently caching resource representations while reducing their inference-time computational and memory overhead. Resource-wise attention removes cross-resource interactions and assigns resource-local positions, producing composition-invariant KV blocks. ReCache then restricts resource visibility to contribution-selected layer--KV-head-group routes and retains only invocation-critical fields through structural and semantic pruning. We evaluate ReCache on a benchmark assembled from seven public tool- and skill-use datasets, including resource-disjoint tests. Resource-wise attention matches dense invocation performance (82.3\% versus 82.4\% Inv-F1) while providing a 3.655$\times$ time-to-first-token speedup. The complete framework reduces allocated KV-tensor memory by 92.43\% and accelerates attention by 1.423$\times$. These results show that separating reusable schema encoding from selective resource access substantially reduces agentic inference costs with limited effectiveness loss. The code is available at https://github.com/EIT-NLP/ReCache.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, prefix caching
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yichu Fang, Sitong Wei, Haozhe Hu, Xiaoyu Shen
- 发布：2026-08-20；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/EIT-NLP/ReCache](https://github.com/EIT-NLP/ReCache)
- 阅读深度：metadata
