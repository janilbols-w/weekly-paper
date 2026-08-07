---
title: "DBLAST: Dependent Block Drafting for Stochastic Speculative Decoding"
description: "Speculative decoding accelerates large language models' inference by using a lightweight drafter to propose multiple future tokens and a target model to verify them."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.05448) · [PDF](https://arxiv.org/pdf/2608.05448)

## 一句话摘要

Speculative decoding accelerates large language models' inference by using a lightweight drafter to propose multiple future tokens and a target model to verify them.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language models' inference by using a lightweight drafter to propose multiple future tokens and a target model to verify them. While recent block and diffusion-style drafters can predict several positions in a single pass, their training and sampling procedures are typically optimized for greedy decoding or assume that positions in the draft block are conditionally independent. This assumption becomes brittle in non-greedy speculative decoding, where the target distribution is deliberately stochastic and multiple continuations become plausible. We study this mismatch for block diffusion drafters and show that the accepted draft length degrades as the entropy of the target sampling distribution increases. We propose a dependent block drafter based on a low-rank latent mixture over token positions, complemented by an acceptance-oriented training objective that directly targets the expected verified length. Experiments with Qwen3-4B and Qwen3-8B on GSM8K, MT-Bench, HumanEval, and creative-writing benchmarks show that our approach, namely DBLast, consistently improves accepted length over independent block sampling, especially in higher-entropy decoding regimes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Amirmohammad Karimi, Chao Gao, Negar Hassanpour
- 发布：2026-08-05；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
