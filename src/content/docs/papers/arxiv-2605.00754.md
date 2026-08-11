---
title: "Themis: Training Robust Multilingual Code Reward Models for Flexible Multi-Criteria Scoring"
description: "Reward models (RMs) have become an indispensable fixture of the language model (LM) post-training playbook, enabling policy alignment and test-time scaling."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2605.00754) · [PDF](https://arxiv.org/pdf/2605.00754)

## 一句话摘要

Reward models (RMs) have become an indispensable fixture of the language model (LM) post-training playbook, enabling policy alignment and test-time scaling.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reward models (RMs) have become an indispensable fixture of the language model (LM) post-training playbook, enabling policy alignment and test-time scaling. Research on the application of RMs in code generation, however, has been comparatively sparse, with existing work largely focusing on execution feedback. This choice constrains post-training to optimizing functional correctness over self-contained executable code. In this work, we examine the training and evaluation of multilingual, multi-criteria code RMs. To this end, we first compile Themis-CodeRewardBench, a benchmark to evaluate code RMs across five preference dimensions (i.e., criteria) and eight programming languages, on which we profile 50+ code, math, and general-purpose RMs. Observing the limited proficiency of current RMs beyond scoring for functional correctness, we develop Themis-CodePreference, the largest open-source collection of code preferences to date (more than 350k preference pairs), and use it to train Themis-RM, a suite of multilingual code reward models for flexible multi-criteria scoring, ranging in size from 600M to 32B parameters. Our experiments and ablations demonstrate positive scaling trends, strong cross-lingual transfer when training on diverse preferences, and the importance of multi-criteria training for reliable code reward modeling.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Indraneil Paul, Goran Glava\v{s}, Iryna Gurevych
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
