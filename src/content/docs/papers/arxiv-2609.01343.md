---
title: "SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers"
description: "Looped Transformers increase effective depth by iterating a shared block of layers, but most evaluations compare at fixed model size, conflating architectural advantage with extra FLOPs."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.01343) · [PDF](https://arxiv.org/pdf/2609.01343)

## 一句话摘要

Looped Transformers increase effective depth by iterating a shared block of layers, but most evaluations compare at fixed model size, conflating architectural advantage with extra FLOPs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped Transformers increase effective depth by iterating a shared block of layers, but most evaluations compare at fixed model size, conflating architectural advantage with extra FLOPs. We study looping on Mixture-of-Experts Transformers while closely matching per-token FLOPs, total non-embedding parameters, and KV cache. Through a series of ablations, we arrive at a recipe we call SMELT (Sparse MoE Transformer, middle layers Loop Twice), which loops the middle half of layers twice while matching the unlooped Baseline on all three budgets. We scale SMELT across four sizes up to 54B non-embedding parameters and fit a separate Chinchilla-style scaling law for each architecture. SMELT's loss drops faster with compute, saving 6.8--18.0\% of training FLOPs on the compute-optimal frontier. The advantage transfers to downstream benchmarks beyond what validation loss predicts, is largest on Code, and grows with sample length and the number of in-context examples. Mechanistic analysis shows that the second visit reduces the attention sink and redirects mass toward content-relevant tokens, an inductive bias that may underlie the observed performance gains. These results show that looping can improve Transformers even under budget matching, offering a practical recipe that turns depth reuse into measurable gains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shaowen Wang, Ge Zhang, Kairong Luo, Yuhao Wu, Shaofan Liu, Jiaheng Liu, Wenhao Huang, Shen Yan, Jian Li
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
