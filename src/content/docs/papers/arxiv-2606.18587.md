---
title: "Dual Dimensionality for Local and Global Attention"
description: "Decoder-only Transformers compute attention over the KV cache of preceding tokens."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.18587) · [PDF](https://arxiv.org/pdf/2606.18587)

## 一句话摘要

Decoder-only Transformers compute attention over the KV cache of preceding tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Decoder-only Transformers compute attention over the KV cache of preceding tokens. Keys and Values are typically represented with the same dimensionality, regardless of their distance from the prediction target. In natural language, however, the next word is most strongly influenced by the immediately preceding tokens. We hypothesize that local and distant tokens impose asymmetric demands on representational capacity: local tokens are more critical for predicting immediate outputs and thus require richer representations, whereas distant tokens primarily serve as long-range memory, for which lower-dimensional representations may suffice. We formalize this idea as Distance-Adaptive Representation (DAR), which preserves full-dimensional representations within a local context window while assigning reduced-dimensional representations (e.g. 1/2 or 1/4 of the original dimensionality) to tokens beyond that window. Across multiple pretraining scales (70M to 410M parameters), as well as continued supervised fine-tuning on a 1B-scale model, this approach closely matches the performance of full-dimensional baselines. In contrast, uniformly reducing dimensionality across all token positions leads to worse performance. These results challenge the common assumption that key and value dimensionality should be uniform across token positions. We further develop an efficient realization of DAR that achieves model quality comparable to the MLA baseline while reducing the average KV-cache size by 68.8\% at 8K context and achieving up to a $1.9\times$ decoding speedup at 128K context on the evaluated models. Our findings suggest a new direction for designing attention architectures that allocate representational capacity according to token distance to reduce KV-cache during inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiyuan Wang, Xuan Luo, Sirui Zeng, Xifeng Yan
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
