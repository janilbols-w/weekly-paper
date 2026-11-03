---
title: "ElTab: Elastically Looped Tabular Transformers"
description: "Tabular transformer models such as TabPFN achieve strong predictive performance but incur substantial inference costs, making them difficult to deploy in resource-constrained settings."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.41819) · [PDF](https://arxiv.org/pdf/2610.41819)

## 一句话摘要

Tabular transformer models such as TabPFN achieve strong predictive performance but incur substantial inference costs, making them difficult to deploy in resource-constrained settings.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tabular transformer models such as TabPFN achieve strong predictive performance but incur substantial inference costs, making them difficult to deploy in resource-constrained settings. While looped transformers reduce parameter count through weight sharing, they can lose significant predictive power when stopped early. To address this challenge, we introduce the Elastically Looped Tabular Transformer (ElTab), a single model trained to operate across different computational budgets through supervision at randomly sampled early exits. Across 30 OpenML classification datasets, a single ElTab model matches six depth-specific looped models while cutting training cost by more than half, and matches a 12-layer TabPFN-style baseline with 25% fewer inference FLOPs. These results show that elastic-depth training yields a single model that adapts to the deployment budget at hand, offering a favorable trade-off among predictive performance, storage, and computational cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: weight sharing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mieszko Komisarczyk, Saurabh Mathur, Maurice Kraus, Sriraam Natarajan, Kristian Kersting
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
