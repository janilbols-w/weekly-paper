---
title: "Margins, Not Windows: Training-Free Per-Step Lossy Speculative Decoding"
description: "Speculative decoding accelerates LLM inference by drafting candidate tokens and verifying them in parallel."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.02897) · [PDF](https://arxiv.org/pdf/2609.02897)

## 一句话摘要

Speculative decoding accelerates LLM inference by drafting candidate tokens and verifying them in parallel.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates LLM inference by drafting candidate tokens and verifying them in parallel. Tree-attention drafters such as EAGLE-3 are widely adopted, yet typically hold two decisions fixed: (1) a strict token-match verification rule and (2) a static draft-tree shape. Prior work relaxes each in isolation under limiting assumptions: long draft chains for training-free lossy verification, and adaptive tree shaping under a fixed token budget. We introduce AdaptiveSpec, a training-free per-step speculative decoding method that adapts both decisions from internal signals already produced during decoding. A per-step margin rule promotes a mismatched draft-proposed token when the ratio of the target's probability on the drafted token to its top-1 probability exceeds a threshold with no dependence on draft length or underlying drafter architecture. A per-step tree policy adjusts the draft tree's depth, width, and node count directly from a fused signal of draft top-1 confidence and a rolling acceptance history capturing recent draft-target agreement, allowing the total draft count to vary rather than only be redistributed. The two adaptations operate on orthogonal axes and compound in effect. Implemented on the SGLang production-grade serving engine, AdaptiveSpec improves throughput over the state-of-the-art autoregressive speculative decoding method EAGLE-3 by up to 56%, recovering 93% to fully lossless task accuracy across GSM8K, MATH-500, and HumanEval on three target models (DeepSeek-R1-Distill-Llama-8B, Llama-3.1-8B-Instruct, Qwen3-8B).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Oszk\'ar Urb\'an, Young D. Kwon, Stylianos I. Venieris, Cecilia Mascolo
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
