---
title: "Local Conflict, Targeted Repair: A Perturbation Analysis of Multi-Domain RL"
description: "Reinforcement learning (RL) post-training improves large language models on individual domains but can degrade previously acquired capabilities."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2606.02398) · [PDF](https://arxiv.org/pdf/2606.02398)

## 一句话摘要

Reinforcement learning (RL) post-training improves large language models on individual domains but can degrade previously acquired capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) post-training improves large language models on individual domains but can degrade previously acquired capabilities. We study this interference in mathematical reasoning, code generation, question answering (QA), and creative writing (CW). Full-model domain gradients can be nearly orthogonal despite substantial selective degradation. Our structural analyses show sparse, weakly overlapping edits on computation routes that reasoning domains share, with directional alignment associated with transfer and conflict. A local perturbation model separates loss changes into a first-order term and a path-averaged curvature term, decomposes the latter along the actual rollback intervention, and provides a conditional explanation for recovery by short refresh. The experiments support this local sensitivity account. After Code $\rightarrow$ Math $\rightarrow$ QA $\rightarrow$ CW training, a short Re-Math refresh raises Math from 57.66 to 66.04 and achieves the highest average score among the evaluated baselines. A training-free rollback at a $9.8\%$ budget recovers $57.4\%$ of the QA-induced Math accuracy drop with a small QA change. Curvature probes at the Math checkpoint further show higher sensitivity along the selected direction than along matched random directions. Together, these results support sparse intervention and targeted refresh as effective ways to mitigate cross-domain degradation.

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

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lei Yang, Siyu Ding, Deyi Xiong
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
