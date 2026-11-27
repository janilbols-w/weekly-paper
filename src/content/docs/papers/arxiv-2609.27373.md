---
title: "Attention Routing Stabilizes Early: Working-Set Inference for Recurrent Language Models"
description: "Recurrent-depth language models, such as looped Transformers, repeatedly apply shared network blocks to refine latent representations, enabling additional test-time computation without generating explicit intermediate reasoning tokens."
---

**评分：53/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.27373) · [PDF](https://arxiv.org/pdf/2609.27373)

## 一句话摘要

Recurrent-depth language models, such as looped Transformers, repeatedly apply shared network blocks to refine latent representations, enabling additional test-time computation without generating explicit intermediate reasoning tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recurrent-depth language models, such as looped Transformers, repeatedly apply shared network blocks to refine latent representations, enabling additional test-time computation without generating explicit intermediate reasoning tokens. However, recurrent inference repeatedly accesses long contexts: full attention incurs quadratic computation during prefill, while autoregressive decoding repeatedly reads large key-value (KV) caches, introducing substantial memory traffic and capacity pressure. We study how attention routing evolves across recurrent depth and uncover a consistent separation in convergence timescales: routing-related quantities, including the attention support and the attention distribution, stabilize substantially earlier than representation-related quantities such as hidden states and attention outputs. This suggests a two-stage structure in which the model discovers a sparse working set and then refines representations over largely the same routing support. Motivated by this structure, we introduce WISE (Working-set Inference with Support Exploitation), a training-free method that uses unrestricted global attention during early recurrent steps to discover a block-structured working set, and then reuses it as the routing support in later steps while keeping recurrent refinement and within-support attention computation dynamic. By combining sparse recurrent attention with compact KV-cache management, WISE reduces both redundant attention computation and memory movement during inference. Across reasoning and long-context benchmarks, WISE closely approaches full-attention accuracy on key evaluated workloads while outperforming early-static support baselines. At 64K context, our implementation achieves up to a 6.46x decode throughput improvement under GPU memory pressure. Our code is available at https://github.com/tbn5pj/WISE_code.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Ke Wan, Chen Chen
- 发布：2026-11-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/tbn5pj/WISE_code](https://github.com/tbn5pj/WISE_code)
- 阅读深度：metadata
