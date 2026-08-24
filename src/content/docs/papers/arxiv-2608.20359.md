---
title: "Self-Speculation for Faster Reasoning Models"
description: "Large language models (LLMs) are deployed for increasingly complex tasks involving planning and multi-step decision making, but high-quality performance on these tasks often requires generating long reasoning traces."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.20359) · [PDF](https://arxiv.org/pdf/2608.20359)

## 一句话摘要

Large language models (LLMs) are deployed for increasingly complex tasks involving planning and multi-step decision making, but high-quality performance on these tasks often requires generating long reasoning traces.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are deployed for increasingly complex tasks involving planning and multi-step decision making, but high-quality performance on these tasks often requires generating long reasoning traces. This is a poor fit for latency-sensitive and interactive applications like voice assistants or coding agents, where generation latency can strongly affect user experience. Existing acceleration methods typically focus on token-level generation, without utilizing the structure of reasoning workflows. We introduce SSR: Self-Speculation for Reasoning Models, a training-free self-speculative decoding method that leverages the chain-of-thought (CoT) as a source of speculation. SSR uses the partial-CoT answer distribution as the drafter and the full-CoT distribution as the verifier, deriving both from the same model at different reasoning budgets. This builds on the observation that later partial-CoT responses often exhibit greater semantic and lexical overlap with the full-budget response. Due to this overlap, SSR can accept long draft prefixes at once, leading to large speedups on structured and long-form generation tasks. To further exploit draft-response overlap beyond the contiguous prefix accepted by standard speculative decoding, SSR also incorporates suffix decoding, using the draft to seed a suffix cache and recover useful spans beyond the accepted prefix, further reducing latency on tasks with high lexical overlap between the draft and the final response. We evaluate SSR on multiple structured and long-form generation tasks where it is most useful, and demonstrate a relative improvement of up to 24.1% on total generation latency for popular open-source models such as Qwen3.5 and Gemma-4.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ravisri Valluri, Tung Nguyen, Aditya Grover
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
