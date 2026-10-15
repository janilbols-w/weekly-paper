---
title: "FOLD: Position-Free Far Memory with Local Order for Long-Context Speculative Decoding"
description: "Speculative decoding accelerates LLM generation through lightweight drafting and parallel verification."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.20392) · [PDF](https://arxiv.org/pdf/2610.20392)

## 一句话摘要

Speculative decoding accelerates LLM generation through lightweight drafting and parallel verification.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates LLM generation through lightweight drafting and parallel verification. It is particularly promising for long inputs, where KV-cache access costs can be amortized over multiple accepted tokens. Yet most drafters are trained on short sequences and degrade on long inputs, while long-context training is costly. Existing training-free approaches restrict the context window, rescale positions, or augment recent context with retrieved distant entries. Drafters, however, read target hidden states that already encode contextual and positional information, and their lightweight architecture makes full-history attention affordable. We propose FOLD, a training-free method that preserves exact local positions and treats all distant entries as far memory at a shared position. To counter attention dilution as the memory grows, we sharpen attention within it to emphasize relevant entries while separately controlling its total weight relative to the local window. Across six target-drafter pairs and diverse benchmarks of up to 256K tokens, FOLD predominantly delivers the highest speedup, with the best case more than doubling the speedup over autoregressive decoding, from 2.08$\times$ to 4.22$\times$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shuxuan Li, Jialiang Kang, Yanghao Zhou, Ziye Zhu, Xiao Yang
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
