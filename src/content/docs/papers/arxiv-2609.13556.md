---
title: "Domain-Specific Jargon in Large Language Models: A Comparative Analysis between General-Purpose and Specialist Models"
description: "Large Language Models (LLMs) have shown remarkable proficiency on general-purpose tasks, yet their performance often degrades in highly-specialized technical domains."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.13556) · [PDF](https://arxiv.org/pdf/2609.13556)

## 一句话摘要

Large Language Models (LLMs) have shown remarkable proficiency on general-purpose tasks, yet their performance often degrades in highly-specialized technical domains.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have shown remarkable proficiency on general-purpose tasks, yet their performance often degrades in highly-specialized technical domains. Moreover, little is known about how parametric knowledge of domain-specific terms is encoded within these models. We address this gap by contributing two novel medical jargon evaluation benchmarks and evaluate a general-purpose Llama-3.1 model against a variant fine-tuned on medical-domain data. Surprisingly, the general-purpose model outperforms the medically fine-tuned model on both tasks. Using mechanistic interpretability tools, we find systematic patterns of miscalibration for the medically fine-tuned model. Instead of reorganizing parametric knowledge, the fine-tuned model places greater emphasis on a small subset of model components associated with jargon-favoring predictions. We find that applying component reweighting strategies against the benchmark tasks successfully suppresses these components and closes the gap with the general-purpose baseline. We also observe that some jargon-sensitive components transfer knowledge to the same tasks involving materials science jargon, suggesting they encode a partially domain-agnostic notion of specialized terminology. Our results provide a case study in which a medically fine-tuned checkpoint does not improve jargon comprehension over its general-purpose counterpart, highlighting that domain adaptation should not be assumed to yield better performance on specialized terminology.

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

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Darin Keng, Zhewei Sun
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
