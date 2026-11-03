---
title: "How to Score Experts for One-Shot MoE Expert Pruning: A Systematic Formulation and Selection Principle"
description: "Mixture-of-Experts (MoE) language models reduce per-token computation through sparse expert activation, yet deployment still requires storing the full expert pool, making one-shot expert pruning a practical approach for reducing memory usage."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.15716) · [PDF](https://arxiv.org/pdf/2606.15716)

## 一句话摘要

Mixture-of-Experts (MoE) language models reduce per-token computation through sparse expert activation, yet deployment still requires storing the full expert pool, making one-shot expert pruning a practical approach for reducing memory usage.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) language models reduce per-token computation through sparse expert activation, yet deployment still requires storing the full expert pool, making one-shot expert pruning a practical approach for reducing memory usage. Although effective, existing criteria are largely heuristic, and no single criterion is universally optimal. Thus, establishing a principle for selecting pruning criteria suited to different deployment objectives remains an important yet largely underexplored problem in one-shot expert pruning. To this end, we introduce a systematic formulation for one-shot MoE expert pruning organized around three factors: routing frequency, gate weighting, and activation strength. The formulation yields a criteria selection principle: task-agnostic pruning should favor routed-token-averaged, gate-free activation-based criteria, whereas task-specific pruning can benefit from retaining routing-frequency and gate-weight information. Beyond this principle, the formulation also provides a systematic view of existing heuristic criteria and gives rise to two new task-agnostic criteria, Mean Activation Norm (MAN) and Mean Squared Activation Norm (MSAN). Across four representative MoE models and 16 diverse benchmarks, MAN and MSAN are consistently strong in the task-agnostic setting, obtain the top-two average ranks, and improve average performance by 4.0 points on average and up to 8.8 points over the strongest baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zongfang Liu, Jinghui Zhang, Zijian Ma, Guangyi Chen, Xin Yuan
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
