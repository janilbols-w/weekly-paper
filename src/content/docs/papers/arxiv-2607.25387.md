---
title: "Learned, Relied Upon, or Necessary? Separating Checkpoint Dependence from Task-Level Value in Sheaf GNNs"
description: "Learned restriction maps in sheaf graph neural networks are often treated as proof that the model has discovered useful edge geometry."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2607.25387) · [PDF](https://arxiv.org/pdf/2607.25387)

## 一句话摘要

Learned restriction maps in sheaf graph neural networks are often treated as proof that the model has discovered useful edge geometry.

## 为什么值得关注

待编辑增强。

## 摘要原文

Learned restriction maps in sheaf graph neural networks are often treated as proof that the model has discovered useful edge geometry. That conclusion does not follow from parameter movement or from a post-hoc ablation: both can show how one checkpoint is organized while leaving open whether learned transport still helps after the rest of the model adapts. We separate these claims with two estimands. Checkpoint reliance intervenes on the maps of a fixed predictor; protocol-relative replacement retrains matched families that remove map capacity, edge variation, or persistent edge assignment. A task-null theorem shows why the claims can diverge: labels identify only the transported classifier directions, leaving $d^2-d$ invisible degrees of freedom in every full $d\times d$ map. An exact frame model then gives the boundary at which reliance becomes unreplaced task value. Label-only training realizes the predicted separation, while audits of public NSD, DNSD, and Directed Sheaf Neural Network (DSNN) implementations recover both replaceable and unreplaced transport regimes on real graphs. All five DNSD benchmarks exhibit fixed-checkpoint reliance. After retraining, assignment-breaking or shared-map controls recover Full performance on four; Roman-Empire retains a $.0675$ advantage over continually resampled assignment and a $.0391$ advantage over a parameter-matched shared map across ten official splits. Thus, a learned map can govern a fitted computation without constituting indispensable edge geometry. Claims of learned transport should pair checkpoint interventions with matched retraining.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yi Liu
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
