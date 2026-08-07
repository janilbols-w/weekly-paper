---
title: "From Chains to Trees: Parent-Conditioned Drafting for Semi-Autoregressive Speculative Decoding"
description: "Speculative decoding accelerates LLM inference only when drafted continuations survive target-model verification."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.02123) · [PDF](https://arxiv.org/pdf/2608.02123)

## 一句话摘要

Speculative decoding accelerates LLM inference only when drafted continuations survive target-model verification.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates LLM inference only when drafted continuations survive target-model verification. Semi-autoregressive drafters such as DSpark predict an entire token block with one backbone forward and refine it with a lightweight Markov head. However, DSpark decodes this block as a single chain, so an early mismatch invalidates the remaining suffix and limits the benefit of large draft blocks. We show that the conditional structure already learned by DSpark can support multiple parent-consistent continuations without retraining or additional backbone passes. We introduce Parent-Conditioned Drafting Tree (PCTree), which uses the pretrained Markov head to score alternative children separately for each concrete parent and allocates a fixed verification budget to the most probable paths. This converts DSpark's linear draft into a tree while preserving its one-pass parallel backbone. Across Qwen3-{4B,8B,14B} and nine benchmarks, at $B{=}7$, measured speedup gains over autoregressive (AR) decoding, relative to matched DSpark, range from $3.1\%$ to $29.5\%$. On Qwen3-4B GSM8K at $B{=}16$, PCTree increases mean acceptance length from $9.41$ to $11.16$ and three-run mean AR speedup from $6.14{\times}$ to $6.60{\times}$. These show that parent-conditioned branching can turn conditional capacity already present in a semi-autoregressive drafter into end-to-end inference gains through an inference-only change.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zixian Li, Tong Li, Chi Xie, Xiaohui Song, Haonan Lu
- 发布：2026-08-03；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
