---
title: "Structural Rationale Distillation via Reasoning Space Compression"
description: "When distilling reasoning from large language models (LLMs) into smaller ones, teacher rationales for similar problems often vary wildly in structure and strategy."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.07139) · [PDF](https://arxiv.org/pdf/2605.07139)

## 一句话摘要

When distilling reasoning from large language models (LLMs) into smaller ones, teacher rationales for similar problems often vary wildly in structure and strategy.

## 为什么值得关注

待编辑增强。

## 摘要原文

When distilling reasoning from large language models (LLMs) into smaller ones, teacher rationales for similar problems often vary wildly in structure and strategy. Like a chef who makes the same dish differently each time, this inconsistency burdens the student with noisy supervision that is hard to internalize. We propose Distillation through Reasoning Path Compression (D-RPC), which constrains the teacher to follow a compact, dynamically maintained bank of reusable high-level reasoning paths. For each training question, D-RPC retrieves the most relevant path and conditions the teacher to follow it, producing rationales that are consistent across similar problems yet diverse enough to cover different problem types. A PAC-Bayes analysis formalizes a trade-off between bank size and coverage, with smaller banks limiting path diversity at the risk of coverage gaps. Our ablations favor an intermediate bank size, consistent with this trade-off. Across five math and commonsense reasoning benchmarks with two student models, D-RPC achieves the highest average accuracy among the evaluated distillation methods, while using fewer tokens than template-heavy alternatives.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jialin Yang, Jiankun Wang, Jiajun Wu, Henry Leung, Jiayu Zhou, Steve Drew
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
