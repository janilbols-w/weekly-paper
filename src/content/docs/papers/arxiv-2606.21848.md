---
title: "Keyless Attention: Value-Space Routing and Value-Only Caching for Efficient Transformers"
description: "Transformer architectures form the foundation of modern natural language processing, yet the Key-Value (KV) cache introduces substantial memory and bandwidth overhead during long-context generation, increasingly bottlenecking large-scale deployment."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.21848) · [PDF](https://arxiv.org/pdf/2606.21848)

## 一句话摘要

Transformer architectures form the foundation of modern natural language processing, yet the Key-Value (KV) cache introduces substantial memory and bandwidth overhead during long-context generation, increasingly bottlenecking large-scale deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer architectures form the foundation of modern natural language processing, yet the Key-Value (KV) cache introduces substantial memory and bandwidth overhead during long-context generation, increasingly bottlenecking large-scale deployment. We propose Keyless Attention, a novel attention mechanism that replaces the conventional key projection with a dedicated value-space routing projection, eliminating key representations from the attention computation entirely and yielding a Value-Only Cache that reduces KV-cache memory by 50% while improving decode throughput. Experiments across multiple models and architectures demonstrate that Keyless Attention achieves comparable perplexity and downstream task performance to standard QKV attention, while consistently reducing KV-cache memory by 50%. Furthermore, Keyless Attention exhibits slower validation loss degradation after the best epoch, indicating improved robustness against overfitting. Ablation studies confirm that the dedicated value-space routing projection is critical, with Keyless Attention outperforming KV-sharing methods that eliminate the key cache without replacing its routing role. Experiments in the pretraining regime further confirm the viability of Keyless Attention in industrial settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xin Gao, Xingming Xu
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
