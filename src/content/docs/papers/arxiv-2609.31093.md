---
title: "Block Sparse Attention with Log-Linear Complexity"
description: "Scaling language models to long contexts is limited by the quadratic cost of self-attention."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.31093) · [PDF](https://arxiv.org/pdf/2609.31093)

## 一句话摘要

Scaling language models to long contexts is limited by the quadratic cost of self-attention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Scaling language models to long contexts is limited by the quadratic cost of self-attention. Block sparse attention offers an efficient alternative, but selecting the retained blocks remains a bottleneck. Conventional block selection requires scoring all query-block pairs and therefore remains quadratic in sequence length. To address this issue, we propose PISA, a block-sparse attention mechanism that employs a pyramid Top-$K$ selection strategy. The main idea is to gradually narrow down the candidates across different levels, making it more efficient to find the most relevant keys. Specifically, we construct a coarse-to-fine hierarchy of keys and perform selection from the coarsest level. At each level, LogSumExp scoring is applied to a bounded candidate set to select candidates for the next finer level, continuing until the finest level is reached. Through pooling, we construct $O(\log N)$ levels of keys, yielding an overall complexity of $O(N\log N)$, where $N$ denotes the sequence length. We develop hardware-aware Triton kernels for both training and inference, fusing hierarchical routing and LogSumExp scoring without materializing the query-key score matrix. We further evaluate our method on language modeling tasks. Compared with the baseline, our method achieves comparable performance on benchmarks such as commonsense reasoning while delivering better results on retrieval tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bohao Tang, Zhen Qin, Yuqi Pan, Zheng Li, Pengfei Liu
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
