---
title: "Matching Supervision to the Student's Learning Capacity: A Unified Framework for On-Policy Self-Distillation"
description: "On-policy self-distillation (OPSD) improves the reasoning abilities of LLMs by internalizing privileged context into model parameters through self-distillation."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.08176) · [PDF](https://arxiv.org/pdf/2608.08176)

## 一句话摘要

On-policy self-distillation (OPSD) improves the reasoning abilities of LLMs by internalizing privileged context into model parameters through self-distillation.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy self-distillation (OPSD) improves the reasoning abilities of LLMs by internalizing privileged context into model parameters through self-distillation. Two recent research lines promote vanilla OPSD by choosing which tokens to learn from and by controlling how much privileged information the teacher receives, respectively. However, we show that each line optimizes one variable while holding the other fixed, which leads to a suboptimal solution. We argue that the two variables are coupled through the student's learning capacity: the privileged information sets the per-token divergence the teacher prescribes, while token weighting selects which of these the student must absorb. We formalize the two lines of work into a unified optimization framework, which maximizes the aggregate teacher--student divergence, subject to a budget on the aggregate learning difficulty the student can absorb. Under this modelling, we propose Unified On-Policy Self-Distillation (USD), a lightweight online algorithm to solve the Lagrangian. USD reveals that a single dual variable governs both decisions: at one price for learning difficulty, it simultaneously sets the token-selection threshold and the direction of privileged-information adjustment, keeping supervision matched to the student's evolving capacity. Through extensive experiments, USD consistently demonstrates superior performance over OPSD and token- and PI-side baselines across various model scales on various reasoning benchmarks. Code is available at https://github.com/lauvlalala/USD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yongkang Yang, Zhezheng Hao, Hong Zhang, Yi Liu, Xiankun Lin, Wence Ji, Fanjunduo Wei, Jiarui Yu, Qiang Lin, Xiaoyun Liang, Hande Dong
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/lauvlalala/USD](https://github.com/lauvlalala/USD)
- 阅读深度：metadata
