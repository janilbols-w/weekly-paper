---
title: "Prism Attention: Proposal-Refined Index Sharing Mechanism for Efficient LLMs Inference"
description: "Long-context decoding in large language models (LLMs) is increasingly bottlenecked by the memory and computation required to attend over an ever-growing Key-Value (KV) cache at each autoregressive step."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.22985) · [PDF](https://arxiv.org/pdf/2610.22985)

## 一句话摘要

Long-context decoding in large language models (LLMs) is increasingly bottlenecked by the memory and computation required to attend over an ever-growing Key-Value (KV) cache at each autoregressive step.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context decoding in large language models (LLMs) is increasingly bottlenecked by the memory and computation required to attend over an ever-growing Key-Value (KV) cache at each autoregressive step. Although token-level sparse attention reduces this burden by restricting computation to a small subset of relevant past tokens, its practical gains are often offset by repeatedly recomputing layer-wise sparse indices as the context grows. A common remedy is to share sparse indices across layers by computing them only at designated anchor layers, but such static reuse ignores the layer-wise evolution of attention patterns, causing the reused indices to progressively deviate from the layer-specific optima and incur substantial attention loss. By revisiting cross-layer sparsity from the perspective of attention dynamics, we find that inter-layer salient token shift is highly localized: although the exact top-$\kappa$ indices differ across layers, the core high-attention tokens remain stable, with changes concentrated near the expanded boundary of previously selected regions. Motivated by this, we propose Prism Attention, a proposal-refined sparse attention framework. It replaces rigid cross-layer index reuse with a coarse-to-fine strategy, preserving layer-wise adaptability while retaining the efficiency benefits of cross-layer sharing. Extensive experiments show that Prism Attention achieves state-of-the-art performance among mainstream sparse attention methods on both reasoning and long-context benchmarks, while attaining a $3.4\times$ end-to-end decoding speedup over FlashAttention at 128K context length.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhenxu Tian, Kebin Liu, Zhengwu Yang, Yi Su, Qingqing Dang, Yanlin Sha, Kaipeng Deng, Dianhai Yu, Yanjun Ma, Juntao Li, Min Zhang
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
