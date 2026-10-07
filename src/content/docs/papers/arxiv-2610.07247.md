---
title: "Learning What to Distill: Bilevel Top-K Token Selection for Self-Distillation in Large Language Models"
description: "Large language models have shown strong reasoning capabilities, but their high inference costs make knowledge distillation an important approach for transferring such capabilities to compact models in resource-constrained scenarios."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.07247) · [PDF](https://arxiv.org/pdf/2610.07247)

## 一句话摘要

Large language models have shown strong reasoning capabilities, but their high inference costs make knowledge distillation an important approach for transferring such capabilities to compact models in resource-constrained scenarios.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models have shown strong reasoning capabilities, but their high inference costs make knowledge distillation an important approach for transferring such capabilities to compact models in resource-constrained scenarios. On-policy self-distillation further reduces the reliance on external large teacher models while improving the reasoning ability of compact language models. However, existing methods typically either distill all token positions uniformly or select tokens using fixed heuristic criteria, assigning the same distillation strength to the selected positions rather than adaptively learning which tokens are most beneficial for distillation. To address these limitations, we propose BiToK-SD (Bilevel Top-K Token Selection for Self-Distillation), a bilevel-optimization-based token selection method that learns where distillation should be applied during on-policy self-distillation. Specifically, BiToK-SD is formulated as a bilevel optimization problem, where the lower-level problem models Top-K token selection as a differentiable threshold-based relaxation, allowing the selected positions to adapt as the student policy evolves, while the upper-level problem performs knowledge distillation on the selected positions. Experiments on mathematical reasoning benchmarks show that BiToK-SD achieves the best average performance among all compared methods while requiring only lightweight additional computation.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Heng Liang, Xinwen Zhang, Hongchang Gao
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
