---
title: "QVAC Genesis III: A Large-Scale, High-Quality Open Synthetic STEM Corpus for Efficient Language Model Pre-Training"
description: "High-quality pre-training data is a critical bottleneck for educational and STEM-specific language models targeting edge AI and on-device deployment where token budgets are tightly constrained."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.19513) · [PDF](https://arxiv.org/pdf/2609.19513)

## 一句话摘要

High-quality pre-training data is a critical bottleneck for educational and STEM-specific language models targeting edge AI and on-device deployment where token budgets are tightly constrained.

## 为什么值得关注

待编辑增强。

## 摘要原文

High-quality pre-training data is a critical bottleneck for educational and STEM-specific language models targeting edge AI and on-device deployment where token budgets are tightly constrained. While major organizations train ever-larger models on private corpora, the open ecosystem lacks STEM-focused synthetic datasets that deliver high per-token learning value efficiently for small models. To address this gap, we introduce QVAC Genesis III, a 191.43B-token, STEM-focused multi-domain synthetic corpus covering 19 domains across several difficulty levels and different educational styles. QVAC Genesis III is built via a dual generation strategy that performs targeted teacher distillation using a weak edge-scale student model as signal: the student's failures are converted into corrective explanations, while its successes are expanded into contrastive option-level reasoning over all answer choices. We further introduce an LLM-as-a-parser evaluation protocol that extracts final answers from free-form outputs and tracks both accuracy and answer validity. To validate the effectiveness of our QVAC Genesis III data, we conduct controlled from-scratch ablations with 1.7B-parameter models, showing that models trained with QVAC Genesis III consistently outperform both models trained with the open-source synthetic corpus Cosmopedia-v2 and the publicly released Cosmo-1B model across ARC, GPQA Diamond, and MMLU STEM benchmarks, achieving up to +28.57% on ARC-E and +21.35% on ARC-C, while reaching a Valid Answer Rate of up to 99.45%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Davide Vitabile, N. Ranjan, Akshay Nambiar, Kamal K. Gupta, Amril Nazir
- 发布：2026-09-18；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
