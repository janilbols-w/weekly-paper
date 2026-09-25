---
title: "Learning to Fluctuate: Statistical Foundations for Causal Tabular Pretraining"
description: "Causal tabular foundation models amortize effect estimation across synthetic mechanisms, but latent-effect supervision rewards posterior shrinkage rather than encoding the repeated-sample response needed in a fixed deployment population."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.26290) · [PDF](https://arxiv.org/pdf/2609.26290)

## 一句话摘要

Causal tabular foundation models amortize effect estimation across synthetic mechanisms, but latent-effect supervision rewards posterior shrinkage rather than encoding the repeated-sample response needed in a fixed deployment population.

## 为什么值得关注

待编辑增强。

## 摘要原文

Causal tabular foundation models amortize effect estimation across synthetic mechanisms, but latent-effect supervision rewards posterior shrinkage rather than encoding the repeated-sample response needed in a fixed deployment population. We introduce fluctuation-supervised pretraining (FSP): each synthetic table is labeled by its average treatment effect plus its efficient influence-function fluctuation; deployment remains a frozen forward pass. Along the path $T_{\lambda,P}=\theta(P)+\lambda P_n\psi_P$, we prove an endpoint transition: every fixed $\lambda<1$ retains label ambiguity of order $(1-\lambda)^2/n$, whereas full fluctuation makes the Gaussian label observable and reduces optimal finite-stratum causal label-prediction risk to order $n^{-2}$. A finite-pretraining bound combines label, network, episode-sampling, and optimization errors; its sampling defect controls fixed-mechanism bias, mean squared error, variance, Gaussian approximation, and, with variance-head accuracy, studentized coverage. Complementary lower bounds separate local $n^{-1}$ ATE risk from the $\log N/M$ excess risk of generic finite-dictionary episode learning. Experiments trace the learned sampling response. Across 24 nonlinear continuous-covariate cells at trained context lengths, continuous-row FSP lowers checkpoint-mean macro RMSE by 7.0% versus S-learner and wins all 12 weak-overlap cells; validation-selected Summary FSP deploys $11.6\times$ faster per table in our warm one-thread benchmark. Under effect shift, matched Raw FSP lowers mean-checkpoint RMSE by 54.2% and teacher defect by 99.0% versus latent-effect supervision, and RMSE by 10.2% versus the released CausalPFN-S checkpoint. Known-effect semisynthesis tests coverage; two randomized-study evaluations show that lower RMSE can coexist with residual attenuation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiheng Zhang
- 发布：2026-09-22；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
