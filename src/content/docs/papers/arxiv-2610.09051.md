---
title: "A Self-Pruning Transformer: Extreme KV-Cache Compression with Universal Attention"
description: "The large KV-cache size of modern LLMs creates a barrier to efficient deployment."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.09051) · [PDF](https://arxiv.org/pdf/2610.09051)

## 一句话摘要

The large KV-cache size of modern LLMs creates a barrier to efficient deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

The large KV-cache size of modern LLMs creates a barrier to efficient deployment. Recent work has explored replacing attention layers' RoPE positional embeddings with alternative decay-based mechanisms, which can then be used to prune KV-cache during inference. However, these decay functions have limited expressivity, and in practice devolve into sliding-window-like eviction patterns. In this work, we propose a unifying framework for complementary and novel decay mechanisms, capturing complex key statistics and interactions while preserving expressive RoPE embeddings and Softmax attention. The resulting Universal Attention is a highly expressive and end-to-end trainable architecture, whose composite decay mechanism acts as a natural, $\textit{adaptive}$ pruning criterion, removing tokens that contribute least to attention computation. Experimentally, Universal Attention achieves state-of-the-art $10\times$ compression on natural language and synthetic task data, while $\textit{improving}$ downstream performance compared to both state-of-the-art baselines and unpruned oracles. It further demonstrates superior long-context generalization with unprecedented $25\times$ compression at length 16k.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Davis Wertheimer, Haochen Shen, Ahan Gupta, Derrick Liu, Yu Chin Fabian Lim, Mudhakar Srivatsa, Raghu K. Ganti, Minjia Zhang, Naigang Wang
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
