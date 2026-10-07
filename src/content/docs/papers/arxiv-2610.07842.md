---
title: "Privileged Context as Drift in On-Policy Self-Distillation"
description: "On-policy self-distillation (OPSD) trains a language model to match a copy of itself conditioned on privileged context."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.07842) · [PDF](https://arxiv.org/pdf/2610.07842)

## 一句话摘要

On-policy self-distillation (OPSD) trains a language model to match a copy of itself conditioned on privileged context.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy self-distillation (OPSD) trains a language model to match a copy of itself conditioned on privileged context. Existing work varies what privileged context contains and how it is produced while also changing models, data, and training setups, making the effects of privileged context design difficult to isolate. Motivated by efforts in continual learning to reduce catastrophic forgetting, we study how the choice of privileged context affects policy drift. Specifically, we vary two axes: content (a demonstration, feedback, or rephrase) and source (external, self-generated with a verifier, or self-generated without a verifier). We train Qwen2.5-7B with OPSD across these nine combinations and three datasets, measuring target-task accuracy, prior-task retention, reverse KL from the base policy, and parameter-update geometry. Holding source fixed, changing content spans a wider median KL range than holding content fixed and changing source. The ratio between these ranges is $5.1\times$ for per-token KL and $2.2\times$ for per-sequence KL. Parameter-update geometry shows the same pattern: updates from adapters that share content are more closely aligned (mean cosine $0.571$) than updates from adapters that share source ($0.255$). For continual learning, these findings suggest that privileged context should be treated as part of OPSD's stability design because it is associated with how far and in what direction the policy moves.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ravenor Davion, Nick Rui
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
