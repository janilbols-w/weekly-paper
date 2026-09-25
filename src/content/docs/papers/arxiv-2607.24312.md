---
title: "CONSISTRE: A Unified Consistency-Aware Framework for Document-Level Relation Extraction with Large Language Models"
description: "Document-level relation extraction (DocRE) aims to extract relations among multiple entities across extended contexts while maintaining consistency across predicted triples."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.24312) · [PDF](https://arxiv.org/pdf/2607.24312)

## 一句话摘要

Document-level relation extraction (DocRE) aims to extract relations among multiple entities across extended contexts while maintaining consistency across predicted triples.

## 为什么值得关注

待编辑增强。

## 摘要原文

Document-level relation extraction (DocRE) aims to extract relations among multiple entities across extended contexts while maintaining consistency across predicted triples. Although large language models (LLMs) show remarkable reasoning capabilities in information extraction, their predictions are typically generated independently for each candidate triple and may violate fundamental relational constraints such as transitivity, symmetry, and functional uniqueness, leading to contradictory and unreliable outputs. We propose CONSISTRE, a unified consistency-aware framework for DocRE that addresses this limitation through two complementary tracks. The first operates at inference time for black-box LLMs, combining constraint-aware prompting, constraint-based verification, and iterative self-reflection to refine predictions without task-specific fine-tuning. The second injects consistency knowledge into smaller open-source models via a knowledge distillation and reinforcement learning pipeline: reasoning traces from a powerful teacher are distilled into a student via supervised fine-tuning, followed by GRPO alignment using a composite reward that jointly optimizes extraction performance and relational consistency. Together, the two tracks cover both API-accessible and locally deployable scenarios under a unified consistency formulation. Experiments on DocRED show that both tracks outperform their baselines, with the inference-time track achieving competitive F1 using off-the-shelf black-box LLMs and the training-time track substantially narrowing the gap between 7--8B open-source models and state-of-the-art proprietary LLMs at a fraction of their inference cost. Ablation studies confirm that explicit consistency modeling mitigates relational contradictions and enhances the reliability of LLM-based DocRE across both deployment paradigms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mingxuan Sun
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
