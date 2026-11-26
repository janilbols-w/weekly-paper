---
title: "Antidistillation is Cheap: Lightweight Distillation-Resistance via Stylistic Corruption"
description: "Knowledge distillation (KD) is a highly effective paradigm for transferring capabilities from large language models (LLMs) to smaller, more specialized student models."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.17772) · [PDF](https://arxiv.org/pdf/2611.17772)

## 一句话摘要

Knowledge distillation (KD) is a highly effective paradigm for transferring capabilities from large language models (LLMs) to smaller, more specialized student models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation (KD) is a highly effective paradigm for transferring capabilities from large language models (LLMs) to smaller, more specialized student models. In commercial deployments where frontier models are restricted behind black-box APIs, sequence-level distillation remains a potent vector for competitors to clone proprietary capabilities at a fraction of the development cost. Existing defenses mostly rely on surrogate models to manipulate next-token sampling, which increases computational overhead and real-time inference latency. In this work, we propose a lightweight defense that injects style-steering vectors into the teacher model's activations upon malicious queries. The framework allows hosts to customize the target defensive styles and switch among them per request, thereby making it harder for adversaries to identify a stable, learnable signature. Because this inference-time intervention largely preserves answer correctness and avoids the degenerate artifacts of prior defenses, adversaries are misled into believing they are extracting valid teacher outputs. Meanwhile, standard consumers continue to receive original, unmodified responses. Our experiments demonstrate that the framework consistently degrades student learning across model families, with minimal inference overhead. Our approach serves as a low-cost deterrent that raises the attacker's extraction and post-hoc sanitization costs. Code is available at https://github.com/anhtu96/distill-resist.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Anh Tu Ngo, Anupam Chattopadhyay
- 发布：2026-11-16；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/anhtu96/distill-resist](https://github.com/anhtu96/distill-resist)
- 阅读深度：metadata
