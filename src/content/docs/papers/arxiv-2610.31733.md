---
title: "Learning to Be Monitored: Causal Bounds and Intervention-Aware Post-Training Recipes for Chain-of-Thought Monitorability"
description: "Chain-of-thought (CoT) monitoring aims to detect potentially harmful behaviors in large language models (LLMs) from their CoTs."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.31733) · [PDF](https://arxiv.org/pdf/2610.31733)

## 一句话摘要

Chain-of-thought (CoT) monitoring aims to detect potentially harmful behaviors in large language models (LLMs) from their CoTs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Chain-of-thought (CoT) monitoring aims to detect potentially harmful behaviors in large language models (LLMs) from their CoTs. Intervention-based evaluations measure this property by asking whether a monitor can detect the role of an intervention from the CoT when the targeted behavior occurs, typically using minimal-criterion sensitivity ($\mathsf{TPR_{mc}}$) proposed by~\citep{guan2025monitoring}. However, a target behavior observed under intervention is not necessarily caused by it, and we show that this metric can overestimate how often a monitor detects target behaviors actually caused by the intervention. Specifically, we establish $\mathsf{TPR_{mc}}$ as an upper bound on this causal detection rate and derive a complementary lower bound, which provides a tighter evaluation framework for CoT monitorability. With this framework, we study whether LLMs can be trained to make their CoTs easier to monitor. We first construct a training dataset of paired control--intervention tasks spanning multiple intervention types. Using the dataset, we design and apply three intervention-specific training methods based on off-policy self-distillation, reinforcement learning, and on-policy self-distillation to train separate variants of each base model. Across various model-monitor configurations, all three methods generally improve CoT monitorability over the corresponding base models under our extended evaluation framework. Our code is available at https://github.com/xinyue-lxy/learning-to-be-monitored.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Qiang Fu, Xinyue Li, Andre Wibisono, Arman Cohan
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/xinyue-lxy/learning-to-be-monitored](https://github.com/xinyue-lxy/learning-to-be-monitored)
- 阅读深度：metadata
