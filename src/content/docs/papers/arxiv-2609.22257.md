---
title: "Strategy Accumulation and Guided Execution for Automated LLM Fine-Tuning"
description: "Producing task-specific large language models requires discovering effective training strategies through experimentation."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.22257) · [PDF](https://arxiv.org/pdf/2609.22257)

## 一句话摘要

Producing task-specific large language models requires discovering effective training strategies through experimentation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Producing task-specific large language models requires discovering effective training strategies through experimentation. Automated fine-tuning systems have made this experimentation feasible with far less manual effort. However, these systems are stateless: each search discards its discovered strategies, dataset insights, and hyperparameter findings once it ends. Every new task must then repeat this costly search from a cold start. To address this, we propose Strategy Accumulation and Guided Execution (SAGE), a two-stage framework that makes automated fine-tuning search cumulative. In the first stage, a multi-agent pipeline performs Monte Carlo Tree Search-based exploration. A parallel Distillation Agent extracts task-specific exploration records and confidence-scored cross-task insights, which together constitute a structured experience repository. In the second stage, SAGE retrieves relevant experience from this repository and selects what applies to guide training on the new task. We evaluate SAGE on nine unseen tasks spanning both single- and cross-category settings. In single-round execution, SAGE's accumulated experience raises the average relative improvement over baseline from 3.2% to 15.6%, a 12.4-percentage-point gain over the same pipeline without it. These results show that persistent strategy experience provides effective guidance for automated fine-tuning on unseen tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haoran Zhao, Wei Du, Dingwen Yang, Jixuan Huang, Junlin Shang, Lingyong Fang, Ya Guo, Tao Gui, Qi Zhang, Xuanjing Huang
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
