---
title: "DCKV: Learned Transform Coding of the Prompt KV Cache in Hybrid Language Models"
description: "Hybrid language models keep a key-value (KV) cache only in their few full-attention layers, but this cache is still the part of a prompt's state that grows with the prompt and that must be stored or moved to reuse it."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.36950) · [PDF](https://arxiv.org/pdf/2610.36950)

## 一句话摘要

Hybrid language models keep a key-value (KV) cache only in their few full-attention layers, but this cache is still the part of a prompt's state that grows with the prompt and that must be stored or moved to reuse it.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid language models keep a key-value (KV) cache only in their few full-attention layers, but this cache is still the part of a prompt's state that grows with the prompt and that must be stored or moved to reuse it. We present DCKV, a differentiable codec for the KV cache and the first KV-cache codec that is trained end to end. Its transform, its quantizer and its entropy models, which are conditioned on the prompt tokens and on already decoded neighbouring positions, are optimized together against the frozen language model, both for the code length that the entropy models assign and for the change of the model's output. On Qwen3.5-2B, DCKV stores a compressed token in more than 55 times fewer bytes than bf16 at a loss of at most 1.8 points on three long-context benchmarks, and in more than 100 times fewer bytes at a loss of at most 3.6 points.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Egor Maximov, Aleksei Merkelov, Vasiliy Alekseev, Ivan Krivorotov, Valentin Beliaev, Nikita Arsenin, Dmitry Bocharov, Aleksei Goncharov
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
