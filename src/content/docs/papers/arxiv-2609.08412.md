---
title: "Stochastically Perturbed Weights: Ensembles from Deterministic Machine-Learning Weather Models"
description: "Machine-learning weather models (MLWMs) now match or outperform operational numerical weather prediction (NWP) at global medium-range forecasting, at far lower inference cost."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](http://arxiv.org/abs/2609.08412v1) · [PDF](https://arxiv.org/pdf/2609.08412v1)

## 一句话摘要

Machine-learning weather models (MLWMs) now match or outperform operational numerical weather prediction (NWP) at global medium-range forecasting, at far lower inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Machine-learning weather models (MLWMs) now match or outperform operational numerical weather prediction (NWP) at global medium-range forecasting, at far lower inference cost. Many deployed MLWMs are deterministic, producing a single forecast with no estimate of its own uncertainty, whereas a growing family of trained-probabilistic models generate calibrated ensembles directly, at the price of a dedicated training run. We ask instead how much uncertainty can be extracted from a deterministic checkpoint that already exists, without retraining it. Where physical ensembles represent model uncertainty by stochastically perturbing parametrisation tendencies, we perturb the network's raw weight tensors at inference time, a scheme we call stochastically perturbed weights (SPW). We also ask whether it works, where and on which scales to inject the noise, and where it fails. A three-phase ablation across four deterministic backbones, Aurora, GraphCast, SFNO, and AIFS, selects one production baseline per model, benchmarked against the trained-probabilistic AIFS-ENS, FourCastNet 3 and Atlas as well as the operational ECMWF ensemble (IFS-ENS) over 112 initialisation times. At a 240 h (10-day) lead time the SPW ensembles reach continuous ranked probability skill scores (CRPSS) between 0.04 and 0.13 below the best trained-probabilistic baseline, at zero marginal training cost. No injection site works across models: the productive tensor group is architecture-specific, so SPW is at present a tuning procedure rather than a plug-and-play recipe. Its main failure mode is a coherent whole-field offset that overdisperses the domain mean, and restricting the noise to coarse scales or perturbing the initial conditions each repair part of it.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Simon Adamov, Oliver Fuhrer, Reto Knutti, Sebastian Schemm
- 发布：2026-09-08；更新：2026-09-08
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/MeteoSwiss/ai-models-ensembles](https://github.com/MeteoSwiss/ai-models-ensembles)
- 阅读深度：metadata
