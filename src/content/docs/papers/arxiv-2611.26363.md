---
title: "HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs"
description: "Attention in large language models (LLMs) scores every query against every key with a full dot product."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2611.26363v1) · [PDF](https://arxiv.org/pdf/2611.26363v1)

## 一句话摘要

Attention in large language models (LLMs) scores every query against every key with a full dot product.

## 为什么值得关注

待编辑增强。

## 摘要原文

Attention in large language models (LLMs) scores every query against every key with a full dot product. We investigate whether this dot product must be computed completely for attention to be effective. We propose Hidden Sparse Attention (HiSA), which keeps the query and key projections intact but only computes a partial dot product, following a static, parameter-free rule set by the token positions: attention becomes sparse in the hidden (feature) dimension, an axis much less explored than token sparsity, rather than over tokens as in almost all sparse attention methods. Based on the structure of rotary position embeddings (RoPE), we decompose keys and queries into parts which can be omitted when computing attention. By training LLMs from scratch with HiSA, we find that this partial dot product does not hurt but improves performance compared with the complete product while computing only about a third of the query-key products. During inference HiSA improves decoding speed and shrinks memory footprint. We also extend HiSA to FlashAttention-3 kernels for training and inference. Finally, we motivate our approach by showing that dense attention learns to suppress the attention score parts that HiSA drops. Code is available at https://github.com/ambroise-b/hisa.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/ambroise-b/hisa](https://github.com/ambroise-b/hisa)
- 阅读深度：metadata
