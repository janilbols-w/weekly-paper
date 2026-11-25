---
title: "Feedback Shortcut: Speculative Decoding for Latent Feedback Transformers"
description: "Feeding each position's top-layer hidden state back into the next position's input improves Transformer performance."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.28227) · [PDF](https://arxiv.org/pdf/2611.28227)

## 一句话摘要

Feeding each position's top-layer hidden state back into the next position's input improves Transformer performance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Feeding each position's top-layer hidden state back into the next position's input improves Transformer performance. However, this feedback breaks speculative decoding, since verifying a drafted token requires the top-layer state from its preceding position, which forces the draft to rely on an approximate stand-in. Training the model to adapt to this stand-in can lower the exact-decoding performance ceiling, while using it at inference time further introduces approximation error. We propose Feedback Shortcut to address both bottlenecks. First, state alignment trains a lightweight projection from multi-token prediction head states to stand-ins, leaving base model training untouched. Second, pipelined correction re-evaluates each draft using its predecessor's newly computed state, a much closer proxy to true feedback. Running this correction inside the verification pass of subsequent drafts improves accuracy with zero extra calls. Across 135M and 780M scales, Feedback Shortcut stays within $10^{-4}$ bits per byte of the exact-decoding ceiling on Paloma and accelerates decoding by 2.4-2.8x with about 2% more training compute than the latent feedback Transformer. At large batch sizes, skipping correction still preserves Transformer speed and over 80% of latent feedback's gains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Benhao Huang, Xuezhe Ma, Hector Liu
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
