---
title: "Mitigating Rubric Interference in LLM Judges via On-Policy Self-Distillation"
description: "LLM judges increasingly evaluate responses against fine-grained rubric checklists."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.14684) · [PDF](https://arxiv.org/pdf/2608.14684)

## 一句话摘要

LLM judges increasingly evaluate responses against fine-grained rubric checklists.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM judges increasingly evaluate responses against fine-grained rubric checklists. When a sample requires multiple rubrics, current methods typically assess each in a separate inference call. Evaluating all rubrics in a single pass is a natural alternative with greater efficiency, but we find that it introduces rubric interference: the verdict on one rubric shifts depending on which other rubrics are co-present. In a preliminary study, only one-third of samples receive fully consistent verdicts when evaluated under rubric sets of varying composition. We develop a measurement framework that probes interference through four controlled operations: rubric set expansion, subsetting, reordering, and noise injection. To mitigate interference without external supervision, we propose Self-Anchored Rubric Alignment (SARA). SARA uses a model's own single-rubric judgments as stable anchors and aligns multi-rubric reasoning with these anchors through on-policy self-distillation. We validate SARA on three datasets (HealthBench, FLASK, ResearchQA) and two model families (Qwen3, Llama-3.1). SARA consistently improves evaluation consistency while maintaining agreement with both base models and GPT-4.1 as a reference judge. Furthermore, the learned consistency transfers across datasets, confirming that SARA teaches a general capability rather than fitting dataset-specific patterns.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dingyao Yu, Tong Zhang, Yutao Mou, Yunxiao Zhang, Wei Ye, Shikun Zhang
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
