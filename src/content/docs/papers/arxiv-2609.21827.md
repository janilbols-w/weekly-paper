---
title: "RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative Decoding"
description: "Speculative decoding accelerates LLM inference by drafting multiple tokens in parallel, with tree-based methods further improving efficiency through hierarchical structures."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.21827) · [PDF](https://arxiv.org/pdf/2609.21827)

## 一句话摘要

Speculative decoding accelerates LLM inference by drafting multiple tokens in parallel, with tree-based methods further improving efficiency through hierarchical structures.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates LLM inference by drafting multiple tokens in parallel, with tree-based methods further improving efficiency through hierarchical structures. Dynamic-tree methods such as EAGLE-3 perform well under greedy decoding via deterministic top-K expansion and global pruning. However, in stochastic decoding (T>0), this mechanism collapses the draft distribution into one-hot probabilities, causing a severe drop in acceptance rate. This creates a dilemma: dynamic-tree methods sacrifice stochastic sampling to preserve context-aware topology, while static-tree methods preserve stochastic sampling with context-agnostic structures. The issue arises because the same probability distribution is used for two conflicting tasks: constructing the tree and verifying tokens. This coupling makes direct injection of randomness challenging due to the resulting stochastic process. We resolve this by decoupling these roles: RheoSampling assigns a token sampled from the draft distribution a proxy probability for tree expansion and pruning alongside its true sampling probability for verification. Specifically, we inject a sampled token among the deterministic top-K slots and treat it with different probabilities during construction and verification, making RheoSampling the first dynamic-tree method with both context-aware top-K construction and stochastic sampling while maintaining losslessness. We establish the lossless guarantee through an equivalence-class analysis that compresses the stochastic tree space into tractable classes. An OT-based verification strategy and a sparse draft mechanism ensure that theoretical gains translate into practical efficiency. Experiments across LLMs and benchmarks demonstrate improvements in acceptance rate and speedup over state-of-the-art dynamic tree methods. This framework may provide a template for analyzing stochastic tree structures.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qiao Hu, Yepeng Weng, Bo Zhang, Takehisa Yairi
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
