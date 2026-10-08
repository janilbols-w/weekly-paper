---
title: "Continuous-Utility Direct Preference Optimization"
description: "Large language model reasoning is often treated as a monolithic capability, relying on binary preference supervision that fails to capture partial progress or fine-grained reasoning quality."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2602.00931) · [PDF](https://arxiv.org/pdf/2602.00931)

## 一句话摘要

Large language model reasoning is often treated as a monolithic capability, relying on binary preference supervision that fails to capture partial progress or fine-grained reasoning quality.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model reasoning is often treated as a monolithic capability, relying on binary preference supervision that fails to capture partial progress or fine-grained reasoning quality. We introduce continuous utility direct preference optimization (CU-DPO), a framework that aligns models to a portfolio of prompt-based cognitive strategies by replacing binary labels with continuous scores that capture fine-grained reasoning quality. We prove that learning with K strategies yields a Theta(K log K) improvement in sample complexity over binary preferences and that DPO converges to the entropy-regularized utility-maximizing policy. To exploit this signal, we propose a two-stage pipeline: (i) strategy selection, which optimizes the model to choose the best strategy via best-vs-all comparisons, and (ii) execution refinement, which trains correct execution using margin-stratified pairs. The framework is domain-agnostic: any task admitting cognitively distinct solution strategies and a decomposable continuous utility signal can be incorporated into the portfolio. On mathematical reasoning benchmarks, CU-DPO improves strategy selection accuracy from 35-46% to 68-78% across seven base models, yielding downstream reasoning gains of up to +6.6 points on in-distribution datasets with effective out-of-distribution transfer. CU-DPO demonstrates consistent gains on code generation and causal reasoning benchmarks, confirming generalization beyond the mathematical domain.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Muhammad Ahmed Mohsin, Muhammad Umer, Emily Fox
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
