---
title: "Lapras: Latent Reasoning for Time Series Language Models"
description: "Time Series Language Models (TSLMs) offer a promising path toward time series understanding by reasoning over temporal signals and producing natural language answers and explanations."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.11111) · [PDF](https://arxiv.org/pdf/2610.11111)

## 一句话摘要

Time Series Language Models (TSLMs) offer a promising path toward time series understanding by reasoning over temporal signals and producing natural language answers and explanations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Time Series Language Models (TSLMs) offer a promising path toward time series understanding by reasoning over temporal signals and producing natural language answers and explanations. A common approach is Chain-of-Thought (CoT), which generates step-by-step rationales linking relevant signal patterns to final answers. Although these models learn from reference CoT traces during post-training, generating faithful descriptions of input time series at inference remains challenging. Expressing high-dimensional, continuous temporal representations in discrete language tokens may cause the model to neglect task-relevant patterns or describe them inaccurately. Because later reasoning steps build on these descriptions, early errors propagate, leading to incorrect answers with plausible explanations that are inconsistent with the input signal. We propose Lapras (Latent Post-trained Reasoning Across Series), a post-training framework that equips TSLMs with latent reasoning. A model trained with Lapras reasons through a sequence of continuous thoughts in the joint time series-language space, producing text only for the final answer. It learns this through teacher-student self-distillation, where a teacher trained on CoT reference traces reasons explicitly through text. The student aligns its hidden states with the teacher's at the answer stage, transferring the teacher's reasoning ability into its latent computation. We evaluate Lapras across four TSLM backbones on five time series question answering benchmarks. Lapras improves average F1 by up to 10.79% over explicit CoT while generating 23.9x fewer tokens. Lapras's continuous thoughts can also be decoded into readable reasoning traces via standard language decoding, preserving textual explanations. Together, these results highlight Lapras as a promising post-training paradigm for efficient, effective, and interpretable TSLM reasoning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yuliang Chen, Yu Yvonne Wu, Patrick Langer, Arvind Pillai, Sudarshan Regmi, Martin Maritsch, Juncheng Liu, Robert Jakob, Thomas Kaar, Tess Z. Griffin, Lisa Marsch, Michael V. Heinz, Nicholas C. Jacobson, Andrew Campbell
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
