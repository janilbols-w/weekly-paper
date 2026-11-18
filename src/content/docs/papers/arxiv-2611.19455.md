---
title: "Text Speeding Itself Up: Recency and Restraint in Session-Local Drafting"
description: "Speculative decoding lets a cheap draft model propose tokens that a large language model verifies in a single forward pass."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.19455) · [PDF](https://arxiv.org/pdf/2611.19455)

## 一句话摘要

Speculative decoding lets a cheap draft model propose tokens that a large language model verifies in a single forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding lets a cheap draft model propose tokens that a large language model verifies in a single forward pass. When the verifier keeps a KV cache, verification is cheap and drafting must be nearly free. Session-local drafters, which predict from the prompt and the text generated so far, meet that bar without training. We compare a recency-weighted, backing-off, confidence-gated session memory against prompt lookup decoding in its reference form, which copies from the earliest earlier match, and in a variant that copies from the most recent one, with paired per-prompt bootstrap intervals throughout. On general, medical, and legal text with a Mistral-7B verifier, recency accounts for the speed: most-recent lookup gains up to 0.09 in speedup over earliest-match lookup on 500-token generations, and session memory's weighting and backoff add nothing measurable on top, at 30 to 40 times the drafting cost. Energy tells a different story. On medical and legal text, unselective drafters are 14% faster than plain decoding yet use as much energy per token, while drafters that abstain on weak evidence save 3 to 4 joules per 100 tokens; a three-token minimum match length on prompt lookup matches the confidence-gated session memory. Outputs are token-identical to greedy decoding in 94% of generations, with every divergence at a numerical near-tie. Under a repetition penalty, long-generation speedups shrink from 1.4-1.7x to 1.1-1.2x, but recency still helps and the length floor is the only drafter that saves energy in both domains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Antal van den Bosch
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
