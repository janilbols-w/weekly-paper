---
title: "Looping Deeper Without Growing the KV Cache: Recurrent Depth for Causal Encoder-Decoders"
description: "Looped language models deepen computation without adding parameters, yet caching full-context key-value (KV) states across layers and rounds severely bounds serving batch size."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.13378) · [PDF](https://arxiv.org/pdf/2611.13378)

## 一句话摘要

Looped language models deepen computation without adding parameters, yet caching full-context key-value (KV) states across layers and rounds severely bounds serving batch size.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped language models deepen computation without adding parameters, yet caching full-context key-value (KV) states across layers and rounds severely bounds serving batch size. We design a looped causal encoder-decoder (CED) that achieves recurrent depth with zero round-wise KV growth, addressing where and how to loop an asymmetric stack in which only sparse encoder layers generate global KV. We find that recurrence must be placed in the encoder to iteratively refine global KV representations rather than re-reading static decoder projections, which both drives language-modeling gains and preserves long-context scaling. Furthermore, training the encoder loop under stochastic recurrence depth induces a fixed-point equilibrium where every round losslessly shares the last round's KV cache. Compounding cross-layer and cross-round KV sharing, the resulting Looped CED matches an unlooped CED's minimal memory footprint and recovers 86-93% of a looped Transformer's gain with 1/6 of its global KV. To test serving at production scale, we loop the 552B-parameter DeepSeek-V4.1-Flash for 8 rounds on one 4xGB200 node: with per-layer and per-round KV the loop cannot fit a single 128K-token request, whereas Looped CED holds 36.8x less KV per token, fits 38 such requests (as many as the unlooped model), and serves 3.6x higher throughput on 8K-token prompts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiaqi Leng, Minshen Zhang, Zhaofeng Sun, Yu-Yang Qian, Peng Zhao, Hao Zhang
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
