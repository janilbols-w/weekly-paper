---
title: "Model Compression with Exact Budget Constraints via Riemannian Manifolds"
description: "Assigning one of K options to each of N groups under a total cost budget is a recurring problem in efficient AI, arising in mixed-precision quantization, non-uniform pruning, and expert selection."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.00649) · [PDF](https://arxiv.org/pdf/2605.00649)

## 一句话摘要

Assigning one of K options to each of N groups under a total cost budget is a recurring problem in efficient AI, arising in mixed-precision quantization, non-uniform pruning, and expert selection.

## 为什么值得关注

待编辑增强。

## 摘要原文

Assigning one of K options to each of N groups under a total cost budget is a recurring problem in efficient AI, arising in mixed-precision quantization, non-uniform pruning, and expert selection. The objective (model loss) depends on all assignments jointly and does not decompose across groups, so combinatorial solvers can only optimize proxy objectives. Evolutionary search evaluates the actual loss but lacks gradients, while penalty-based methods enforce the budget only approximately and often require heavy hyperparameter tuning. We show that under softmax relaxation, the budget constraint defines a smooth Riemannian manifold in logit space with unusually clean geometry: the normal vector is available in closed form, shifting logits along the cost vector changes expected cost monotonically, and vector transport reduces to a single inner product. Building on this, we propose Riemannian Constrained Optimization (RCO), which wraps tangent projection, binary-search retraction, and momentum transport around a standard Adam step. Combined with Gumbel straight-through estimation and budget-constrained dynamic programming for discrete feasibility, RCO optimizes the actual loss with first-order methods, enforces the expected budget exactly at every iterate, and introduces no constraint-related hyperparameters. The same construction handles multiple simultaneous budgets with no additional coefficients. RCO matches or exceeds state-of-the-art methods on synthetic problems and realistic LLM compression settings, often at considerably lower wall-clock cost. Source code is available at https://github.com/IST-DASLab/RCO.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Michael Helcig, Dan Alistarh
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/IST-DASLab/RCO](https://github.com/IST-DASLab/RCO)
- 阅读深度：metadata
