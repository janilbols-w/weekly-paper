---
title: "Self-Indexing Attention for Compression-Compatible Sparse Long-Context LLM Inference"
description: "Sparse long-context inference requires efficient token retrieval in both prefill and decode."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.13205) · [PDF](https://arxiv.org/pdf/2609.13205)

## 一句话摘要

Sparse long-context inference requires efficient token retrieval in both prefill and decode.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse long-context inference requires efficient token retrieval in both prefill and decode. Existing methods often use different retrieval strategies for the two stages, preventing one retrieval representation from being reused throughout inference. We propose Self-Indexing Attention, a training-free framework built on a shared transform-domain sign-magnitude representation. The key signs provide a reusable token-level index for grouped prefill selection and decode retrieval, while the same representation remains compatible with external KV-cache compression without separate indexer metadata. This 1-bit index enables efficient retrieval through bitwise operations widely supported by modern accelerators. At 5% attention density, Self-Indexing Attention remains close to dense attention on LongBench and RULER and achieves up to 6.1x prefill and 10.3x decode attention-operator speedups. Experiments with TurboQuant and DeepSeekV4-Flash further demonstrate compatibility with low-bit KV-cache compression and pretrained sparse-attention indexers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xu Yang, Jiapeng Zhang, Zhangke, Changjian Chen, Yuxin Chen, Feiqiang Sun, Chengguang Xu, Feng Jin, Zhuo Tang
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
