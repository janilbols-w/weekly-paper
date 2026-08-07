---
title: "Understanding Sparse Attention Selectivity in Long-Context Foundation Models via Counterfactual Evaluation"
description: "Sparse attention is widely deployed in long-context serving stacks, yet no framework audits how discarding blocks changes the influence of specific content on model output."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.01676) · [PDF](https://arxiv.org/pdf/2608.01676)

## 一句话摘要

Sparse attention is widely deployed in long-context serving stacks, yet no framework audits how discarding blocks changes the influence of specific content on model output.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse attention is widely deployed in long-context serving stacks, yet no framework audits how discarding blocks changes the influence of specific content on model output. We first establish that the phenomenon is real and causal: Block Sparse Flash Attention (BSFA) route replay across four architectures changes output decisions in 13 of 16 cells, with zero identity-replay label flips. We then introduce a dense-calibrated counterfactual audit using matched probe cards---Gold (carrying the correct answer label), Poison (carrying a target wrong label), and Benign (filler only)---under six-layout position symmetry, isolating the sparsification-specific effect. Two patterns compete. Signal concentration: the selector preserves Gold and Poison blocks far above filler-matched Benign blocks (G$\approx$P$\gg$B across all model--task pairs). Integration loss: discarding blocks severs cross-block attention---confirmed by an ablation where isolating the probe block collapses its influence from 4.48 logits to zero. Compression ratio governs the balance: a full sweep from mild ($c=0.25$) to aggressive ($c=0.75$) compression across four model--task pairs reveals that three of four cells move toward stronger sparse amplification at higher compression, with two exhibiting sign reversals. Three independent arms---BSFA route replay, controlled block-top-$k$, and KV-cache eviction---converge: sparsification changes content influence in ways aggregate accuracy cannot detect. We provide an open measurement framework deployable on any model exposing block identities.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: flash attention, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xingyu Ren, Youran Sun, Chugang Yi, Haizhao Yang
- 发布：2026-08-03；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
