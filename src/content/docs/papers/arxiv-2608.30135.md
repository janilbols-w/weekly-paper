---
title: "Verification-Aware Training for Speculative Decoding"
description: "Speculative decoding accelerates large language model inference by using a draft model to generate candidate tokens, which are verified by the target model in a single forward pass."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.30135) · [PDF](https://arxiv.org/pdf/2608.30135)

## 一句话摘要

Speculative decoding accelerates large language model inference by using a draft model to generate candidate tokens, which are verified by the target model in a single forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model inference by using a draft model to generate candidate tokens, which are verified by the target model in a single forward pass. Verification proceeds sequentially and discards every position from the first rejection onward, yet existing draft training relies on token-level imitation of the target with a fixed per-position weighting that reflects neither property. We introduce Verification-Aware Training (VAT), a plug-in framework that simulates verification at every training step and turns the resulting accept and reject patterns into supervision. VAT consists of two components: (i) a verification head, a lightweight jointly trained binary classifier that supervises the draft model on whether each position survives sequential verification; (ii) verification-adaptive weighting, which replaces the fixed weighting schedule by keeping full weight up to each sample's first rejection point and re-anchoring the decay to start there. VAT modifies only the training objective, so it can be layered on top of existing methods without changing the draft architecture, the target model, or the inference procedure. Applied to EAGLE-3 and DFlash on Qwen3-4B, Qwen3-8B, and LLaMA-3.1-8B, VAT improves average acceptance length by up to 11.4% and wall-clock speedup by up to 8.7%, with consistent gains across math, code, and chat benchmarks. Code will be available at https://github.com/naver-ai/vat

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Geonmo Gu, Byeongho Heo, HeeJae Jun, Yoohoon Kang, Sangmin Lee, Sangdoo Yun, Dongyoon Han
- 发布：2026-08-31；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/naver-ai/vat](https://github.com/naver-ai/vat)
- 阅读深度：metadata
