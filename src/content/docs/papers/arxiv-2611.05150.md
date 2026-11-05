---
title: "What Sets the Serving Speed of Looped Language Models? Measurements and Optimizations Graded by Exactness"
description: "Looped language models apply one block of layers many times per token, so a serving engine pays every per-layer overhead once per loop; we measure serving for Ouro and Huginn-0125 in an open-source looped-model engine and grade our optimizations from bitwise-identical changes to those that require an accuracy check."
---

**评分：39/100** · LLM 高效推理 > Serving 与分布式推理 > Prefill-Decode 解耦

[论文原文](https://arxiv.org/abs/2611.05150) · [PDF](https://arxiv.org/pdf/2611.05150)

## 一句话摘要

Looped language models apply one block of layers many times per token, so a serving engine pays every per-layer overhead once per loop; we measure serving for Ouro and Huginn-0125 in an open-source looped-model engine and grade our optimizations from bitwise-identical changes to those that require an accuracy check.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped language models apply one block of layers many times per token, so a serving engine pays every per-layer overhead once per loop; we measure serving for Ouro and Huginn-0125 in an open-source looped-model engine and grade our optimizations from bitwise-identical changes to those that require an accuracy check. At batch 1, fusing all loop submissions leaves Ouro throughput at 0.99x; the 5689 small kernels per token are the real cost, and fusing them behind rounding fences raises throughput 1.11-1.59x while 1014/1014 requests remain identical. An approximate fusion is no faster and misses a one-point GSM8K rule on 87 questions (61 and 62 correct versus 64), so we do not ship it. Huginn's released defaults avoid dead KV slots, reuse prefix-cache pages, and serve 1.77-3.16x faster than the base engine; Ouro reaches 1.65-2.15x and agent sessions 1.91-3.21x, while Huginn's noise and prefix-reuse changes stay within one point on all 1319 Huginn test questions; Huginn's packed prefill, -0.61 points on the same questions, meets that rule only on its point estimate. Position-keyed noise makes CPU cache reuse exact but still leaves 20 of 128 GPU full hits different, while loop fusion delays prefill admission and a 64-graph cache prevents eager fallbacks. Under prefill-decode disaggregation ExactLoop reaches up to 3.3x the base throughput with peer error handling disabled, and 3.1x in two of three runs with it enabled. Its transfer budget, sized to hold one request's KV in flight, cuts the commit tail from about one second under the earlier budget to 16 ms (base: 2.8 s), removing the polling rounds that the engine's interval would otherwise impose.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefill-decode
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dezhen Lu, Runguo Li, Zixiang Ni, Yuchen Tang, Xingquan Kong, Jiaxing Yang, Jiarui Guo, Lingxiang Gao
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
