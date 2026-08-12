---
title: "REATS: LLM Reasoning-based Ensemble Learning for Adaptive Time Series Forecasting"
description: "Due to the diversity of real-world time series, no single forecasting model consistently dominates across all samples."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 数据管线

[论文原文](https://arxiv.org/abs/2608.10149) · [PDF](https://arxiv.org/pdf/2608.10149)

## 一句话摘要

Due to the diversity of real-world time series, no single forecasting model consistently dominates across all samples.

## 为什么值得关注

待编辑增强。

## 摘要原文

Due to the diversity of real-world time series, no single forecasting model consistently dominates across all samples. Ensemble learning addresses this by combining complementary model strengths, yet existing methods rely on fixed rules or black-box models based solely on numerical inputs, failing to leverage LLM reasoning for interpretable weighting decisions. We propose REATS, which leverages LLM reasoning capabilities as an intelligent ensemble router that jointly processes textual temporal pattern descriptions and numerical features to produce interpretable, sample-adaptive ensemble weights through chain-of-thought reasoning. To enable effective LLM-based ensembling, we study its key design choices and propose: (i) a structured input pipeline that transforms raw time series into hybrid textual--numerical representations with fixed token cost, enabling rule-based chain-of-thought construction without API dependency, augmented with retrieved similar-sample priors; (ii) a diverse multi-row weight supervision scheme coupled with a token-efficient percentage-table format that reduces numerical complexity and mitigates LLM hallucinations; and (iii) a two-stage fine-tuning framework combining SFT with GRPO, where a reciprocal reward mapping transforms the continuous unbounded MSE gap into bounded signals with amplified near-oracle sensitivity, addressing the uniform sensitivity and outlier-dominated advantage compression inherent in naive reward designs for regression-based GRPO. Experiments on eight benchmarks demonstrate that REATS outperforms competitive ensemble baselines while providing natural language explanations and demonstrating strong transfer learning and out-of-domain generalization to unseen candidate models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: input pipeline
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xu Zhang, Chang Xu, Hui Sun, Nan Ma, Zijian Zhang, Peng Wang, Wei Wang, Li Zhao
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
