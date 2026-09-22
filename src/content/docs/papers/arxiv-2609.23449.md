---
title: "PSD: Pseudo Self-Distillation of Memory Representation Capabilities for LLM Agents"
description: "Memory systems are becoming a core component of LLM agents, but constructing and maintaining memory remains expensive because it relies on repeated calls to large proprietary language models."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.23449) · [PDF](https://arxiv.org/pdf/2609.23449)

## 一句话摘要

Memory systems are becoming a core component of LLM agents, but constructing and maintaining memory remains expensive because it relies on repeated calls to large proprietary language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Memory systems are becoming a core component of LLM agents, but constructing and maintaining memory remains expensive because it relies on repeated calls to large proprietary language models. This cost creates a major barrier to deploying memory-enhanced agents at scale. In this paper, we present Pseudo Self-Distillation (PSD), a framework that enables small language models (SLMs) to construct hierarchical memory representations by distilling behavior from a strong black-box oracle through a multi-stage training pipeline. Standard distillation methods require access to teacher logits or hidden states, which closed models do not expose. Unlike conventional self-distillation settings, where supervision is derived from a model's own predictions, sampled rollouts, or aggregated outputs, PSD enables a single-model distillation setup while channeling external oracle knowledge through the prompt. PSD uses a single small model in two roles: a teacher that sees a privileged prompt containing the oracle's answer as reference context, and a student that sees only the task prompt. The student learns to reproduce the teacher's output distribution, absorbing oracle-guided behavior into its own weights without accessing the oracle's internals. On LoCoMo, PSD-trained Qwen3-0.6B, 1.7B, and 4B match or exceed GPT-4.1-mini on downstream retrieval at a fraction of the deployment cost, with off-policy PSD achieving the strongest results across most conditions. We further show that this memory-construction capability transfers out-of-distribution to LongMemEval, despite the students being trained exclusively on LoCoMo with no exposure to LongMemEval data.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Pirzada Suhail, Menglin Xia, Xuchao Zhang, Mayukh Das, Chetan Bansal, Saravan Rajmohan
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
