---
title: "Physics-Informed Foresight Pruning for Sparse PINN Solvers of Nonlinear PDEs"
description: "Physics-informed neural networks (PINNs) often rely on over-parameterized models to optimize coupled solution and differential-residual objectives, leaving unclear how much capacity is necessary and what pruning should preserve."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.25564) · [PDF](https://arxiv.org/pdf/2608.25564)

## 一句话摘要

Physics-informed neural networks (PINNs) often rely on over-parameterized models to optimize coupled solution and differential-residual objectives, leaving unclear how much capacity is necessary and what pruning should preserve.

## 为什么值得关注

待编辑增强。

## 摘要原文

Physics-informed neural networks (PINNs) often rely on over-parameterized models to optimize coupled solution and differential-residual objectives, leaving unclear how much capacity is necessary and what pruning should preserve. We study foresight pruning at initialization for sparse PirateNet PDE solvers. Standard neural tangent kernel spectrum-aware pruning (NTK-SAP) aims to preserve output-side training dynamics but may overlook parameters whose main influence arises through derivatives in the governing equations. We introduce physics-informed spectrum-aware pruning (PI-SAP), which assigns saliency using sensitivity of the PDE residual. Experiments on the Gray-Scott equations, complex Ginzburg-Landau equation, Burgers' equation, and linear convection equation show that PI-SAP more consistently preserves Gray-Scott residual fidelity and is competitive under aggressive sparsity. However, no criterion is uniformly optimal across equations or sparsity levels. Small-batch PINN-NTK diagnostics further show that residual fidelity, solution accuracy, and kernel conditioning are distinct objectives, motivating pruning methods that explicitly balance solution-side and residual-side training dynamics during optimization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ahmad Ishaque Karimi, Uvini Balasuriya Mudiyanselage, Kookjin Lee
- 发布：2026-08-26；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
