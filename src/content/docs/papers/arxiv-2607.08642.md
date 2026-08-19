---
title: "DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding"
description: "Speculative decoding accelerates LLM inference by drafting tokens and verifying them in parallel."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2607.08642) · [PDF](https://arxiv.org/pdf/2607.08642)

## 一句话摘要

Speculative decoding accelerates LLM inference by drafting tokens and verifying them in parallel.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates LLM inference by drafting tokens and verifying them in parallel. Block-diffusion drafters such as DFlash model only per-position marginals, and tree methods such as DDTree expand candidate trees from those marginals. The released Domino drafter adds a GRU-based causal correction making each draft token's distribution path-dependent, a structure DDTree's factorized formulation cannot represent. We introduce DominoTree, a training-free best-first draft tree scored by Domino's conditional (non-factorized) correction along each root-to-node path, made practical by restricting the per-node correction to a candidate top-M. We evaluate it on eight benchmarks in a single-stream harness, and in SGLang, where it runs as an out-of-tree plugin against AR, DFlash, EAGLE-3 and Domino under identical flags. DominoTree attains the highest mean accepted length in every serving cell - two model sizes, single-request and concurrent load, context to 32K - and the highest Overall accepted length at every temperature in the research harness (21 of 24 per-dataset cells). A three-arm decomposition holding drafter, budget and verifier fixed separates the gain from applying the correction at all (+10.1% accepted length) from that of recomputing it along each candidate's realized path (+4.7% more), the part this paper adds. Where the round is verify-dominated, throughput follows: up to 7.3x over AR on Qwen3-8B, beating the released Domino decoder at its CUDA-graph best at every temperature, and inside SGLang winning single-request throughput by +12% over Domino on Qwen3-8B. On HELMET long context it beats Domino by +29-36% accepted length and +10-34% throughput at every length and both model sizes. Past a memory-constrained card's admission cap the chain wins goodput, and at our longest context, where prefill dominates, our lead over EAGLE-3 narrows to a tie.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Saw S. Lin (Zhiqi Zhang), Jyh-Shing Roger Jang
- 发布：2026-08-19；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
