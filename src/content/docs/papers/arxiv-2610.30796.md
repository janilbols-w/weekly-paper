---
title: "GIFT: Gradient Informed Filtering for Distillation Augmented Reasoning RL"
description: "Training large language models for complex reasoning tasks relies on two complementary signals: sparse, outcome-grounded reinforcement learning (RL) for correctness, and dense, token-level distillation for guidance."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.30796) · [PDF](https://arxiv.org/pdf/2610.30796)

## 一句话摘要

Training large language models for complex reasoning tasks relies on two complementary signals: sparse, outcome-grounded reinforcement learning (RL) for correctness, and dense, token-level distillation for guidance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training large language models for complex reasoning tasks relies on two complementary signals: sparse, outcome-grounded reinforcement learning (RL) for correctness, and dense, token-level distillation for guidance. However, complementarity in supervision does not guarantee compatibility in optimization; imitation-focused distillation can conflict with the outcome-driven RL objective, and existing hybrids lack a principled resolution. We propose \textbf{GIFT} (\textbf{G}radient-\textbf{I}nformed \textbf{F}il\textbf{T}ering for Distillation-Augmented Reasoning RL), a novel method that directly addresses the allocation problem of which teacher updates to apply. GIFT performs a token-level geometric analysis, decomposing the distillation gradient into a component \textbf{parallel} to the RL gradient, which measures first-order conflict and provides a \textbf{safety} filter, and a component \textbf{orthogonal} to it, which quantifies novel directional guidance and provides a measure of \textbf{value}. This decomposition yields a principled scoring rule to rank token-level guidance. We combine this with a progressive \textbf{coverage annealing} schedule that shrinks the budget of tokens receiving distillation, ensuring that the most conflicting updates are discarded first while the most complementary ones are retained at full strength. This facilitates a smooth transition from dense, geometrically-filtered guidance to a pure, outcome-grounded objective at convergence. Extensive experiments on mathematical and logical reasoning benchmarks show that GIFT consistently outperforms strong baselines across multiple model scales, achieving relative gains of up to 9.5\% on difficult mathematical reasoning tasks. Code: https://github.com/lilifree/GIFT

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shijie Li, Yilin Gao, Tieyuan Chen, Yun Luo, Weiyao Lin, Hang Yu
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/lilifree/GIFT](https://github.com/lilifree/GIFT)
- 阅读深度：metadata
