---
title: "Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning"
description: "Large language models achieve superior performance on tasks that require extended reasoning, but long chains of thought make the KV cache a severe memory bottleneck."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.03430) · [PDF](https://arxiv.org/pdf/2609.03430)

## 一句话摘要

Large language models achieve superior performance on tasks that require extended reasoning, but long chains of thought make the KV cache a severe memory bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models achieve superior performance on tasks that require extended reasoning, but long chains of thought make the KV cache a severe memory bottleneck. Existing KV cache compression methods share one paradigm: score each cached token by some estimate of how much it will matter later, and keep the top-scoring ones. We show that the selection signal contributes almost nothing. Random Attention keeps the prompt and evicts uniformly at random within each attention head, computing no score at all; across four models and six reasoning tasks it matches the strongest prior evictor while serving 32-43% higher throughput than it in vLLM deployment. Controlled experiments explain this by showing that 1) the prompt is the fragile part of the cache, and most of the gap between selectors is just whether their selection signal happened to keep it; 2) the reasoning trace protects itself against eviction with redundancy at two levels, in the text (the model restates what it still needs as it works) and across attention heads (each keeps its own copy of the trace), so once the prompt is safe, a random draw retains enough copies of what the model still needs, and no score is required to pick them. Our code is publicly available at https://github.com/SalesforceAIResearch/Random-Attention.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Heng Wang, Jielin Qiu, Wenting Zhao, Cheng Qian, Liangwei Yang, Jiawei Han, Heng Ji, Silvio Savarese, Shelby Heinecke, Huan Wang
- 发布：2026-09-03；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/SalesforceAIResearch/Random-Attention](https://github.com/SalesforceAIResearch/Random-Attention)
- 阅读深度：metadata
