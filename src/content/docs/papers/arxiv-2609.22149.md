---
title: "Beyond the Stitching Assumption: A Unified Framework for Multimodal Synthetic Data Evaluation via Semantic Quantization"
description: "Multimodal synthetic datasets combine structured attributes with free text, but are often evaluated separately."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.22149) · [PDF](https://arxiv.org/pdf/2609.22149)

## 一句话摘要

Multimodal synthetic datasets combine structured attributes with free text, but are often evaluated separately.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multimodal synthetic datasets combine structured attributes with free text, but are often evaluated separately. Such metrics can remain high after tabular--text pairings are disrupted. We present a projection-based evaluator for tabular--text synthetic data. A fixed sentence encoder maps text to embeddings, \(k\)-means converts them to cluster states, and tabular variables are represented as categorical or quantile-binned states. Real and synthetic contingency tables are compared using Jensen--Shannon divergence (JSD), normalized mutual information (NMI), conditional JSD (cJSD), and joint-state entropy. We also report text-to-attribute (T2A) utility and a holdout-calibrated proximity flag rate (PFR) as a representation-level diagnostic. A text-permutation control preserves both marginal distributions while disrupting their pairing. Experiments on Amazon Reviews, Kiva Loans, and the Employment Scam Aegean Dataset show that modality-specific scores remain high under this control. The projection diagnostics detect disruption when real projected dependence exceeds a permutation baseline, but are less informative for weak or sparse projections. Some conditioned LLM baselines also exhibit stronger measured dependence than the corresponding real-data projections. These results support explicit cross-modal evaluation with permutation baselines and coverage reporting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yefeng Yuan, Zhan Shi, Liang Cheng, Yuhong Liu
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
