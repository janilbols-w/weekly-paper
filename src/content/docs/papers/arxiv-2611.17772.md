---
title: "Antidistillation is Cheap: Lightweight Distillation-Resistance via Stylistic Corruption"
description: "Knowledge distillation (KD) is a highly effective paradigm for transferring capabilities from large language models (LLMs) to smaller, more specialized student models."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.17772) · [PDF](https://arxiv.org/pdf/2611.17772)

## 一句话摘要

Knowledge distillation (KD) is a highly effective paradigm for transferring capabilities from large language models (LLMs) to smaller, more specialized student models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation (KD) is a highly effective paradigm for transferring capabilities from large language models (LLMs) to smaller, more specialized student models. In commercial deployment where frontier models are restricted behind black-box APIs, sequence-level distillation remains a potent vector for competitors to clone proprietary capabilities at a fraction of the development cost. Existing defenses mostly rely on surrogate models to manipulate next-token sampling, which increases computational overhead and real-time inference latency. In this work, we propose a lightweight defense that dynamically injects style-steering vectors into the teacher model's activations upon malicious queries. This framework offers exceptional flexibility, allowing hosts to customize target defensive styles and dynamically blend them to maximize stylistic variance. Crucially, this inference-time intervention preserves semantic utility and fluency during malicious queries, misleading adversaries into believing that they are extracting pristine teacher outputs, while standard consumers continue to receive original, unmodified responses. Our experiments demonstrate that this framework successfully disrupts student learning, achieving substantial anti-distillation performance while incurring negligible overhead and preserving text naturalness. Our code is available at https://anonymous.4open.science/r/distill-resist-38C6/.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anh Tu Ngo, Anupam Chattopadhyay
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
