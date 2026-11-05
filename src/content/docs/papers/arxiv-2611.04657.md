---
title: "Exploiting Biases in Attention for Transformers"
description: "Attention is known to be sparse in vision transformers."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.04657) · [PDF](https://arxiv.org/pdf/2611.04657)

## 一句话摘要

Attention is known to be sparse in vision transformers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Attention is known to be sparse in vision transformers. In particular, we analyze the unequal relevance of attention-matrix columns to the final computation and show that this phenomenon becomes increasingly pronounced with network depth. This can be interpreted as saying that tokens have an absolute importance for the attention process, independently of queries. Inspired by this, we propose a reformulation of the attention formula that makes this phenomenon explicit by adding an input-dependent bias to the query-key dot product. We show that this new term gives each token a scalar value indicating its anticipated influence on other tokens during the attention process, and can thus serve as a proxy for pruning attention maps. Across multiple transformer model sizes, this allows us to substantially reduce the computational cost of attention, in terms of both FLOPs and inference latency, while retaining most of the original classification accuracy. We publicly released the code and models at https://github.com/EIDOSLAB/AttentionWithBias.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Charles Herr, Gabriele Spadaro, Enzo Tartaglione
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/EIDOSLAB/AttentionWithBias](https://github.com/EIDOSLAB/AttentionWithBias)
- 阅读深度：metadata
