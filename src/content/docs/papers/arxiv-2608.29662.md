---
title: "ACTD: Anchor-Based Cross-Tokenizer Distillation with Residual Regularization"
description: "Knowledge distillation effectively transfers reasoning capabilities from large language models to lightweight student models."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.29662) · [PDF](https://arxiv.org/pdf/2608.29662)

## 一句话摘要

Knowledge distillation effectively transfers reasoning capabilities from large language models to lightweight student models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation effectively transfers reasoning capabilities from large language models to lightweight student models. To enable knowledge transfer across disparate model families, researchers increasingly explore cross-tokenizer distillation. However, cross-tokenizer distillation remains challenging due to vocabulary and sequence misalignment, while approximate vocabulary alignment can introduce additional noise into distillation. To address these challenges, we propose Anchor-Based Cross-Tokenizer Distillation with Residual Regularization (ACTD). ACTD bridges structural heterogeneity through vocabulary and sequence alignment, while mitigating alignment noise via a novel anchor loss with residual regularization. We further extend this framework to a multi-teacher setting. Evaluated across five reasoning benchmarks with three distinct teacher models, ACTD achieves state-of-the-art performance. Moreover, its multi-teacher extension outperforms the strongest single-teacher and multi-teacher baselines, further demonstrating the robustness of our method.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Huiyi Zhang, Zijian Li, Xiaocheng Feng, Weitao Ma, Xiaoliang Yang, Yichong Huang, Bing Qin
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
