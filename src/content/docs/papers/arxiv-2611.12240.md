---
title: "Prune, Don't Merge: Expert Compression of Mixture-of-Experts LLMs on Multilingual Production Tasks"
description: "Mixture-of-Experts language models are cheap to run per token but expensive to hold in GPU memory, which drives the cost of serving them in production."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.12240) · [PDF](https://arxiv.org/pdf/2611.12240)

## 一句话摘要

Mixture-of-Experts language models are cheap to run per token but expensive to hold in GPU memory, which drives the cost of serving them in production.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts language models are cheap to run per token but expensive to hold in GPU memory, which drives the cost of serving them in production. One-shot expert compression shrinks them after a single calibration pass. Its two current state-of-the-art methods are REAP for expert pruning, which deletes the least salient experts, and REAM for expert merging, which merges them into the most salient ones. Both have been evaluated only on academic benchmarks. We compare the two on five multilingual production tasks of a web-hosting company, from classification to the generation of marketing HTML email templates, with two 30B-parameter models (Qwen3-30B-A3B-Instruct-2507 and the hybrid Mamba-attention Nemotron-3.5-Lightning) at 25% and 50% of experts removed and the same calibration data. Pruning wins: on the same rows, REAP is significantly better in 16 of 20 comparisons and REAM in 2. At 25%, REAP keeps 93.6% of Qwen3-30B's generative quality and REAM 62.5%, although on benchmarks the two are within a point for the same model. The damage concentrates in the output contract rather than the content: 89.8-95.2% of each significant loss on email templates comes from hard-gate failures such as invalid JSON, broken mobile layouts and runaway generation, and most failed non-English domain descriptions copy the prompt's English opening phrase. Cross-perplexity and logit divergence, two diagnostics from the REAP paper, also track production quality, as does the rate of repetition loops; n-gram diversity does not. We close with practical guidance for compressing MoE models for production.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tomas Rasymas, Povilas Kvedaras
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
