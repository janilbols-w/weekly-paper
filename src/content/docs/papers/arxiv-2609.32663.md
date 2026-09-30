---
title: "Distance-KV: Exploiting Relative Distance for Efficient Long-Context Inference"
description: "The memory usage and decoding latency of LLM inference grow rapidly with context length."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.32663) · [PDF](https://arxiv.org/pdf/2609.32663)

## 一句话摘要

The memory usage and decoding latency of LLM inference grow rapidly with context length.

## 为什么值得关注

待编辑增强。

## 摘要原文

The memory usage and decoding latency of LLM inference grow rapidly with context length. To reduce these costs, key-value (KV) cache compression methods selectively retain cached states based on token importance or differences in attention patterns across heads. However, we discover that retrieval capability varies substantially with relative distance, even within the same attention head. To exploit this structure, we introduce Distance-KV, which learns a static KV retention pattern over the joint space of layers, attention heads, and relative distances. The pattern is learned offline with the language model frozen and reused across inputs to prune and compact the KV cache without online importance scoring. Across three backbone models and four long-context benchmarks, Distance-KV consistently achieves the best overall performance among competing KV cache compression methods, exceeding the strongest compression baseline by up to 9.3 points on RULER at 128K. On Llama-3.1-8B-Instruct at 128K, Distance-KV reduces KV cache memory by 65.4% and achieves a $1.66\times$ decoding speedup relative to Dense. Together, these results identify relative distance as an important structural dimension for understanding how LLMs retrieve information over long contexts and for designing more efficient inference methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xianpeng Shang, Canbin Huang, Jiang Li, Tian Lan, Qianyi Cai, Xiaojun Quan, Xiangdong Su
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
