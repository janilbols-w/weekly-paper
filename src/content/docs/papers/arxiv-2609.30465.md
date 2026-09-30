---
title: "RAZOR: Pruning Replaceable Experts in LLMs"
description: "Mixture-of-experts (MoE) models activate only a few experts per token yet store the entire expert pool."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.30465) · [PDF](https://arxiv.org/pdf/2609.30465)

## 一句话摘要

Mixture-of-experts (MoE) models activate only a few experts per token yet store the entire expert pool.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-experts (MoE) models activate only a few experts per token yet store the entire expert pool. Whole-expert pruning shrinks that pool, but for reasoning models it must remove experts without eroding reasoning ability. Common scores rank experts by routing frequency or output magnitude, which measures isolated contribution rather than deletion damage. What decides the damage is functional replaceability, whether the surviving computation can reproduce what is removed. A large contribution may be replaceable by the remaining mixture, whereas a small one may carry a direction the survivors cannot recover. We introduce RAZOR, a training-free method that scores replaceability from consensus residuals, the deviations of individual expert outputs from their original weighted mixture. Holding the layer input fixed, these residuals yield the exact output change from deleting one expert, including survivor reweighting and the replacement expert promoted by router refill. RAZOR aggregates this change over calibration tokens and prunes to a layerwise budget using forward passes alone, without gradients, subset search, or recovery training. On GLM-4.7-Flash, Qwen3.6-35B-A3B, DeepSeek-V4-Flash-0731, and Hy3 at 25% and 50% expert removal, RAZOR attains the highest macro average over nine reasoning-centered tasks among the evaluated pruning methods in all eight model-budget settings. Against REAP on GLM-4.7-Flash and Qwen3.6-35B-A3B, it gains 2.12-5.59 points on this average and lowers reverse KL in all four comparisons. Retained accuracy is not the whole picture, as pruned Qwen3.6-35B-A3B still shifts in response diversity, formatting, and termination.

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
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
