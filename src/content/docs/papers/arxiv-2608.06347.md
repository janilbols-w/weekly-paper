---
title: "RP-OPSD: Reasoning-Pivot-Guided On-Policy Self-Distillation for Multilingual Reasoning Transfer"
description: "Multilingual reasoning transfer is crucial for extending reasoning capabilities of large language models (LLMs) beyond high-resource languages."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.06347) · [PDF](https://arxiv.org/pdf/2608.06347)

## 一句话摘要

Multilingual reasoning transfer is crucial for extending reasoning capabilities of large language models (LLMs) beyond high-resource languages.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multilingual reasoning transfer is crucial for extending reasoning capabilities of large language models (LLMs) beyond high-resource languages. On-policy self-distillation (OPSD) and its variants have emerged as a promising paradigm, providing dense token-level supervision on student-generated rollouts, yet their objectives do not explicitly prioritize reasoning signals most critical to cross-lingual transfer. We characterize that target-language reasoning comprises the generation of both surface text and reasoning pivots, which are decisions that advance or redirect the reasoning process and shape subsequent inference. This motivates concentrating privileged distillation around such pivots. We therefore propose RP-OPSD, Reasoning-Pivot-guided On-Policy Self-Distillation, using the distributional shift between matched teacher views with and without an English reference solution as an operational proxy to guide privileged distillation and reference anchoring. Experiments on mathematical reasoning benchmarks covering 17 languages and multiple difficulty levels show that our method outperforms strong multilingual reasoning baselines and OPSD variants. Further analysis reveals that RP-OPSD concentrates privileged distillation on reasoning-control and problem-condistioned state-update tokens, while downweighting it for tokens that mainly support surface realization. Our code is available at https://github.com/NJUNLP/RP-OPSD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xinye Wang, Junxiao Liu, Shujian Huang
- 发布：2026-08-06；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/NJUNLP/RP-OPSD](https://github.com/NJUNLP/RP-OPSD)
- 阅读深度：metadata
