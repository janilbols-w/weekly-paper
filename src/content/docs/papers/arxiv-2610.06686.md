---
title: "OVAL: Output-Aware Local Page Bases for KV Cache Retrieval"
description: "Long context inference with large language models becomes increasingly expensive as attention must operate over an ever growing KV cache."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.06686) · [PDF](https://arxiv.org/pdf/2610.06686)

## 一句话摘要

Long context inference with large language models becomes increasingly expensive as attention must operate over an ever growing KV cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long context inference with large language models becomes increasingly expensive as attention must operate over an ever growing KV cache. Page sparse attention reduces this cost by representing each KV page compactly and retrieving only a subset for each query. Existing retrieval methods are designed to estimate attention scores or page relevance, but their objectives do not directly account for how approximation errors affect the resulting value weighted attention output. We introduce \method{}, an output aware page encoding derived from the joint structure of keys and values while preserving the key information needed for accurate retrieval. \method{} is training free and requires no additional value dependent statistics at inference time. Once constructed, its stored representation has the same size and decode time scoring cost as a key only spectral representation. Across long reasoning, long context understanding, and long generation benchmarks, \method{} consistently improves over the key only spectral baseline and performs competitively with recent KV cache compression and retrieval methods. On long reasoning benchmarks, it achieves strong avg@\(k\) performance across model benchmark pairs, while matching or surpassing leading baselines on several long context understanding and generation settings with modest decoding overhead. Code is available at \url{https://github.com/Ashkan13776/oval-kv}.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ashkan Shahbazi, Chayne Thrash, Soheil Kolouri
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Ashkan13776/oval-kv}](https://github.com/Ashkan13776/oval-kv})
- 阅读深度：metadata
