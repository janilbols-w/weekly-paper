---
title: "LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers"
description: "Looped Transformers improve parameter efficiency by repeatedly applying the same Transformer layers."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.19649) · [PDF](https://arxiv.org/pdf/2611.19649)

## 一句话摘要

Looped Transformers improve parameter efficiency by repeatedly applying the same Transformer layers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped Transformers improve parameter efficiency by repeatedly applying the same Transformer layers. During autoregressive decoding, however, generating each token requires several sequential passes through these layers, leading to high decoding latency. Pipelined self-speculative methods use shallow-loop predictions to process tokens at different loops in the same batch, but each token must reach the drafting depth before the next can enter the pipeline. We introduce LoopFill, a training-free speculative decoding algorithm for looped LLM that combines multi-token suffix drafts with shallow-loop predictions in a single draft tree. Both drafters contribute to one tree, so a suffix lookup can immediately extend a shallow prediction and several future tokens can enter the pipeline together. The shared block computes the highest-scoring draft candidates at different loop depths in one batch, and full-depth verification preserves the model's autoregressive output distribution. Across seven benchmarks, LoopFill's average speedup over greedy autoregressive decoding is $5.85\times$ on Ouro-2.6B and $5.13\times$ on Huginn-3.5B. The speedups exceed those of LoopAhead, the strongest baseline, by \(40\%\) on Ouro-2.6B and \(25\%\) on Huginn-3.5B.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Siqi Zhu, Suozhi Huang, Yi Zhao, Jiaxuan You
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
