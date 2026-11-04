---
title: "Architecture-Aware Mixed Precision for Replica-Exchange Training of Geometry-Aware Neural Operators with Uncertainty Quantification"
description: "Geometry-aware neural operators face substantial computational and memory demands when learning across complex physical domains."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.02427) · [PDF](https://arxiv.org/pdf/2611.02427)

## 一句话摘要

Geometry-aware neural operators face substantial computational and memory demands when learning across complex physical domains.

## 为什么值得关注

待编辑增强。

## 摘要原文

Geometry-aware neural operators face substantial computational and memory demands when learning across complex physical domains. We introduce Architecture-Aware Mixed Precision (AA-MP), a replica-exchange training strategy that allocates numerical precision according to replica roles and architecture-specific operations. By retaining FP32 for refinement while selectively employing BF16 for exploration, AA-MP preserves predictive accuracy while improving training efficiency. Across fluid dynamics and three-dimensional structural mechanics benchmarks, AA-MP achieves comparable accuracy to full-precision training over an ensemble of runs, while reducing hot-replica peak GPU memory by 46.9% and training time by up to 25.8%. It also outperforms naive Automatic Mixed Precision (AMP) in memory efficiency and computational cost, with increasing memory advantages at larger model and geometry scales. Ablation studies show that retaining FP32 in the cold-replica is important for predictive accuracy, while additional FP32 operations in the exploratory replica provide limited benefits relative to their computational cost. Finally, conformal prediction for uncertainty calibration shows that AA-MP achieves near-nominal coverage with narrower prediction intervals than the alternatives. These results advance the scalability of geometry-aware scientific machine learning by reducing computational costs without compromising predictive accuracy or uncertainty quantification.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixed precision
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ujin Jeon, Michael Penwarden, Wenqian Chen, Guang Lin
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
