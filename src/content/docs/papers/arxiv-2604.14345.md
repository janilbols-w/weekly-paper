---
title: "PAC-CF: Calibrating Irreversible Frontier Pruning in LLM-Guided Search"
description: "LLM-guided search is usually adopted to solve complex tasks by ranking and pruning top-$K$ candidates based on evaluator scores."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.14345) · [PDF](https://arxiv.org/pdf/2604.14345)

## 一句话摘要

LLM-guided search is usually adopted to solve complex tasks by ranking and pruning top-$K$ candidates based on evaluator scores.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-guided search is usually adopted to solve complex tasks by ranking and pruning top-$K$ candidates based on evaluator scores. However, irreducible bias still exists even if popular methods, such as repeated sampling, are applied to reduce variance. Consequently, pruning may remove every continuation that can reach a valid solution. In this paper, we propose Probably Approximately Correct Conformal Filtering (PAC-CF), which formulates tree pruning as a PAC-guaranteed decision problem. Theoretical analysis establishes how irreducible bias reduces the score separation for certified elimination. Native-Trace path calibration derives a conformal margin from the score deficit of verifier-valid continuations on held-out Native traces. During deployment, PAC-CF uses this calibrated margin in a direct score-gap filtering rule. Across diverse domains and state-of-the-art controllers, PAC-CF improves utility at various budgets while reducing all five measured workload metrics. Especially on pruning-aware ToolTree under a 100-request budget, replacing native top-$K$ improves equal-domain utility by 4.38 points while reducing physical requests by $18.95\%$ with a $23.76\%$ token reduction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhao Qian, Jiayu Chen, Lixu Wang
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
