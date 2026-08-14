---
title: "Training and Benchmarking Code Generation for Physics-Inspired Animations"
description: "Large language models (LLMs) have been widely studied in areas such as mathematical reasoning, complex coding, and scientific problem solving."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2602.10840) · [PDF](https://arxiv.org/pdf/2602.10840)

## 一句话摘要

Large language models (LLMs) have been widely studied in areas such as mathematical reasoning, complex coding, and scientific problem solving.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have been widely studied in areas such as mathematical reasoning, complex coding, and scientific problem solving. However, their ability to generate executable code that visually depicts physical scenarios and their qualitative dynamics remains underexplored. We propose SimuScene, the first systematic study that trains and evaluates LLMs on code generation for physics-inspired animations across 52 concepts spanning five physics domains. We build an automated data collection pipeline with human verification to ensure data quality. The resulting dataset contains 7,659 scenarios, including a 334-example human-verified test set. We evaluate 10 contemporary LLMs and find that even the strongest model achieves only a 21.5\% Avg@8 accuracy, demonstrating the difficulty of generating animations that are both executable and visually aligned with physical scenario descriptions. Finally, we introduce a reinforcement learning pipeline that uses visual rewards from code-generated videos to train text-only LLMs, with a vision-language model evaluating videos through verification questions. Experiments show that training with our data and video-based rewards improves LLM performance on physics-inspired animation generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yanan Wang, Renxi Wang, Yongxin Wang, Xuezhi Liang, Fajri Koto, Timothy Baldwin, Xiaodan Liang, Haonan Li
- 发布：2026-08-14；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
