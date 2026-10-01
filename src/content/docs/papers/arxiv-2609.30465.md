---
title: "RAZOR: Pruning Replaceable Experts in LLMs"
description: "Mixture-of-experts (MoE) models activate only a few experts per token but store the entire expert pool."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.30465) · [PDF](https://arxiv.org/pdf/2609.30465)

## 一句话摘要

Mixture-of-experts (MoE) models activate only a few experts per token but store the entire expert pool.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-experts (MoE) models activate only a few experts per token but store the entire expert pool. Pruning this pool requires identifying experts whose removal preserves model behavior. Routing frequency and output magnitude do not fully describe deletion damage, which also depends on how the surviving and replacement experts compensate for the removed output. We introduce RAZOR, a training-free pruning method based on consensus residuals, the deviations of expert outputs from their original weighted mixture. At a fixed layer input, these residuals give the exact output change for a single deletion under survivor renormalization and router refill. RAZOR aggregates this damage by conditional root mean square and selects experts under a layerwise budget using forward computation alone, without gradients, subset search, or recovery training. Against frequency, activation-norm, and REAP baselines on GLM-4.7-Flash and Qwen3.6-35B-A3B at 25% and 50% expert removal, it attains the highest macro average over nine reasoning-intensive tasks in all four model-budget settings, gaining 2.12-5.59 points over REAP and lowering reverse KL in all four. On DeepSeek-V4-Flash-0731 and Hy3, it also achieves the highest macro average among the three residual criteria. Local exactness does not guarantee better joint pruning. Generation analyses show changes in diversity, formatting, and termination despite higher task scores.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mingyang Song, Mao Zheng
- 发布：2026-09-28；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
