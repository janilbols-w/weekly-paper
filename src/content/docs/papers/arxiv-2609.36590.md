---
title: "SEED: Self-Speculative Decoding via Implicit Encoder-Decoder"
description: "Self-speculative decoding accelerates large language model (LLM) inference by drafting tokens from the target model itself, but faces a sharp tradeoff between the quality and cost of the draft."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.36590) · [PDF](https://arxiv.org/pdf/2609.36590)

## 一句话摘要

Self-speculative decoding accelerates large language model (LLM) inference by drafting tokens from the target model itself, but faces a sharp tradeoff between the quality and cost of the draft.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-speculative decoding accelerates large language model (LLM) inference by drafting tokens from the target model itself, but faces a sharp tradeoff between the quality and cost of the draft. Early-exit methods produce drafts cheaply by terminating computation at intermediate layers, but forgo the deeper representations that later layers provide and thus suffer in draft quality. Multi-token prediction preserves draft quality by emitting from the model's final hidden states, but pays for a full forward pass to produce those states at every drafting step. We propose self-speculative encoder-decoder (SEED), a self-speculative method that obtains high-quality drafts cheaply by reusing the deep contextual representations already computed during verification. We reinterpret the standard decoder-only transformer as an implicit encoder-decoder: the first layers (encoder) build deep contextual representations, and the last few layers (decoder) emit tokens from them. Encoding and verification are merged into a single step: verification is performed by the full encoder-decoder, and the contextual representations of the verified prefix are cached for reuse during drafting. Drafting is therefore very fast: between verifications, the lightweight decoder drafts multiple tokens autoregressively, each conditioned on the cached representations and on preceding drafts. Experiments across multiple benchmarks show that SEED achieves up to 2.7$\times$ average speedup on 4B-scale models, outperforming both early-exit and MTP-style self-speculative baselines and running 28% faster than the state-of-the-art EAGLE-3, while preserving or even improving the generation quality of standard autoregressive fine-tuning. Code is available at https://github.com/lhk2004/SEED.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hankun Lin, Patrick Pynadath, Ruqi Zhang
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/lhk2004/SEED](https://github.com/lhk2004/SEED)
- 阅读深度：metadata
