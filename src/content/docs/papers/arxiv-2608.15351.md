---
title: "Spectral Rank Certification for Foundation Model Adapters"
description: "Nominal LoRA rank is a design parameter; calibrated spectral evidence is a separate inferential quantity."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.15351) · [PDF](https://arxiv.org/pdf/2608.15351)

## 一句话摘要

Nominal LoRA rank is a design parameter; calibrated spectral evidence is a separate inferential quantity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Nominal LoRA rank is a design parameter; calibrated spectral evidence is a separate inferential quantity. This article develops a finite-sample framework for inferring effective rank structure in public foundation-model adapters. The theoretical core is an exact chi-square divergence for the fixed-dimensional Gaussian rank-one reference experiment, with an unknown signal direction integrated under a rotation-invariant reference prior. The resulting series yields a computable finite-sample Le Cam bound at concrete layer sizes, an explicit remainder bound for numerical truncation, and the rectangular Baik-Ben Arous-Peche (BBP) limit. A compact-manifold Laplace expansion shows that finite-sample likelihood evidence also depends on leading spectral gaps through the factor $s_1^{|m-n|}\prod_{i\ge2}(s_1^2-s_i^2)$, motivating joint calibration of clustered singular values. Building on these results, we introduce an empirical-null workflow for PEFT LoRA adapters: factor reconstruction, Monte Carlo $p$-values, stagewise and block testing, and module-wise and corpus-level BH reporting. In an audit of 26 public adapters, 684 modules, six architecture families, and 31,770 public-checkpoint spectra rows, calibrated effective rank is typically much smaller than nominal rank and differs systematically from 95\% energy retention. A measured RoBERTa-RTE slice on $n=24$ examples illustrates the measurement path from calibrated ranks to task evaluation, without treating the slice as a utility study. The main empirical finding is that calibrated effective rank is usually far below nominal rank, and that energy retention and statistical surprise answer different questions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mohammed Ahnouch, Lotfi Elaachak
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
