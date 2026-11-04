---
title: "Unlearning by Extrapolating a Shrink-and-Heal Lookahead"
description: "Unlearning aims to make a large language model behave like one retrained without its forget set."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.00374) · [PDF](https://arxiv.org/pdf/2611.00374)

## 一句话摘要

Unlearning aims to make a large language model behave like one retrained without its forget set.

## 为什么值得关注

待编辑增强。

## 摘要原文

Unlearning aims to make a large language model behave like one retrained without its forget set. Prevailing likelihood-suppression objectives, however, lack an explicit forgetting target: they continually reward lower forget-set likelihood, making forgetting sensitive to the optimization budget. We address this limitation by estimating the direction toward the oracle without training it. Our key idea is to shrink the fine-tuned model toward its pre-fine-tuning weights and briefly re-learn the retain set, thereby removing the forget-specific contribution; in the linearized regime, this shrink-and-heal lookahead moves the model a fixed fraction of the way to the retrained model, its unique fixed point. Our method, SHIFT, extrapolates the lookahead's per-token changes into distillation targets and iteratively refines them. Evaluated against eleven baselines under a unified OpenUnlearning protocol, SHIFT achieves the highest aggregate score across all TOFU settings and the closest oracle alignment, 3.7x closer on average than the next-best method; on MUSE, it preserves the most retain knowledge. Under larger optimization budgets, baselines overshoot the oracle, while SHIFT remains near it, even under relearning attacks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hoang-Chau Luong, Lingwei Chen
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
