---
title: "Where Activation Sparsity and KV-Cache Sparsity Cross in LLM Decoding"
description: "At each step, decoding one sequence with a large language model rereads the projection weights, whose traffic is fixed, and the key-value (KV) cache, whose traffic grows with context."
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.33889) · [PDF](https://arxiv.org/pdf/2609.33889)

## 一句话摘要

At each step, decoding one sequence with a large language model rereads the projection weights, whose traffic is fixed, and the key-value (KV) cache, whose traffic grows with context.

## 为什么值得关注

待编辑增强。

## 摘要原文

At each step, decoding one sequence with a large language model rereads the projection weights, whose traffic is fixed, and the key-value (KV) cache, whose traffic grows with context. Activation sparsity trims the first term and KV-cache sparsity the second, yet their reported speedups are hard to compare because each depends on context length and on the dense attention kernel it is measured against. We derive a byte crossover, the context length at which the two savings are equal, together with ideal speedup bounds for each branch and for their composition, from model dimensions and keep ratios alone. We then time both branches and their composition from 2K to 128K tokens on two GPUs after a dense prefill of real text, with dense and sparse modes reading the cache through the same split-K attention kernel. The projection branch leads at short context and the KV branch at long context, with speedups that follow their byte bounds up to fixed kernel costs. Adding these costs, measured in separate sweeps, lets the byte account predict the measured crossings of three keep-ratio pairs, a second model, and a second GPU to within 4.1K tokens. Timing the dense baseline with masked instead of split-K attention inflates the apparent speedup of the same KV policy about fivefold. An attention-scored KV selection answers the same passkey and multi-key placements as dense decoding up to 127K tokens, whereas a KV window misses most of them. Under matched perplexity budgets, activation sparsity composed with this selection decodes 14 to 26% faster than the best single branch on both GPUs. Code is available at https://github.com/js-lee-AI/ByteCross.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel, kv-cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jungseob Lee, Seungyoon Lee, Seongtae Hong, Sugyeong Eo, Heuiseok Lim
- 发布：2026-09-27；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/js-lee-AI/ByteCross](https://github.com/js-lee-AI/ByteCross)
- 阅读深度：metadata
