---
title: "aiXamine: Unified Black-Box Evaluation of Cross-Dimensional Trade-offs in LLM Safety, Security, and Privacy"
description: "The critical failure modes in deployed large language models (LLMs) are cross-dimensional: a model can score 99.3 in safety alignment while refusing one in three benign queries, or improve across every capability metric while losing 21 points in privacy."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.20554) · [PDF](https://arxiv.org/pdf/2608.20554)

## 一句话摘要

The critical failure modes in deployed large language models (LLMs) are cross-dimensional: a model can score 99.3 in safety alignment while refusing one in three benign queries, or improve across every capability metric while losing 21 points in privacy.

## 为什么值得关注

待编辑增强。

## 摘要原文

The critical failure modes in deployed large language models (LLMs) are cross-dimensional: a model can score 99.3 in safety alignment while refusing one in three benign queries, or improve across every capability metric while losing 21 points in privacy. Existing evaluation frameworks that assess safety, security, and privacy independently cannot detect these patterns. We introduce aiXamine, a unified black-box platform that evaluates LLM trustworthiness across safety, security, and privacy as interdependent properties. aiXamine orchestrates 46 tests across nine services through an automated red-teaming pipeline, producing hierarchical risk profiles, from prompt-level diagnostics to cross-service trade-off analytics, that enable reproducible comparison of proprietary and open-weight systems under identical conditions. Applying aiXamine to over 120 LLMs through more than 5,000 test runs, we conduct the largest joint safety, security, and privacy study to date and uncover three cross-dimensional phenomena invisible to single-axis evaluation. First, safety enforcement incurs a quantifiable safety tax: stronger alignment systematically increases over-refusal, forcing providers to choose between protection and utility. Second, privacy is near-orthogonal to other trustworthiness dimensions and not captured by standard alignment. Third, we identify and formally characterize distillation-induced robustness collapse: off-policy distillation without on-policy correction causes entropy collapse, catastrophically destroying robustness (56.9$\to$2.6) on the same base architecture. These findings, compounded by diminishing returns from scale and category-dependent safety behaviors, demonstrate that trustworthiness is inherently multi-dimensional: progress along one axis does not guarantee, and can actively undermine, progress along others, yet current alignment methods treat it as a single objective.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fatih Deniz, Yazan Boshmaf, Dorde Popovic, Issa Khalil
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
