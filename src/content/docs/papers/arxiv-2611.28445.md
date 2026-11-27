---
title: "Muted Distillation: Sealing Reasoning from Teacher Unlocks Token-Efficient Agents"
description: "On-policy distillation (OPD) is commonly adopted as one of the components in post-training of large language models (LLMs), but in multi-turn agentic tasks we find that the student model increases their reasoning lengths after training."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.28445) · [PDF](https://arxiv.org/pdf/2611.28445)

## 一句话摘要

On-policy distillation (OPD) is commonly adopted as one of the components in post-training of large language models (LLMs), but in multi-turn agentic tasks we find that the student model increases their reasoning lengths after training.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) is commonly adopted as one of the components in post-training of large language models (LLMs), but in multi-turn agentic tasks we find that the student model increases their reasoning lengths after training. Our empirical analysis shows that the reasoning token lengths is affected by how much the student can distract the teacher's scores. We introduce Muted Distillation (MD), a simple variant of OPD that hides the student's reasoning from the teacher, so the teacher judges what the student does without the interference of student's reasonings. MD takes a few lines of code and adds no extra data or hyperparameters. On the knowledge-work benchmarks OfficeQA Pro and SpreadsheetBench, it reduces output tokens per episode by 57\% and 53\% compared with standard OPD, making the student more concise than it was before training. At the same time, it matches OPD's accuracy on OfficeQA Pro and improves pass@1 by 4.8 points on SpreadsheetBench.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuwei Zhang, Ian Miao, Wentao Zhang, Chen Qu, Bill Bi, Jingbo Shang, Donna Schut
- 发布：2026-11-21；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
