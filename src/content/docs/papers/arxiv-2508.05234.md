---
title: "Resource-Limited Joint Multimodal Sentiment Reasoning and Classification via Chain-of-Thought Enhancement and Distillation"
description: "Current approaches for Multimodal Sentiment Analysis (MSA) primarily leverage the knowledge and reasoning capabilities of parameter-heavy (Multimodal) LLMs for classification, overlooking autonomous multimodal sentiment reasoning generation in resource-constrained environments."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2508.05234) · [PDF](https://arxiv.org/pdf/2508.05234)

## 一句话摘要

Current approaches for Multimodal Sentiment Analysis (MSA) primarily leverage the knowledge and reasoning capabilities of parameter-heavy (Multimodal) LLMs for classification, overlooking autonomous multimodal sentiment reasoning generation in resource-constrained environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Current approaches for Multimodal Sentiment Analysis (MSA) primarily leverage the knowledge and reasoning capabilities of parameter-heavy (Multimodal) LLMs for classification, overlooking autonomous multimodal sentiment reasoning generation in resource-constrained environments. In this paper, we focus on the Resource-Limited Joint Multimodal Sentiment Reasoning and Classification task, JMSRC, which simultaneously performs multimodal sentiment reasoning chain generation and sentiment classification only with a lightweight model. We propose a Multimodal Chain-of-Thought Reasoning Distillation model, MulCoT-RD, designed for JMSRC that employs a "Teacher-Assistant-Student" distillation paradigm to address deployment constraints in resource-limited environments. We first leverage a high-performance Multimodal Large Language Model (MLLM) to generate the initial reasoning dataset and train a medium-sized assistant model with a multi-task learning mechanism. A lightweight student model is jointly trained to perform efficient multimodal sentiment reasoning generation and classification. Extensive experiments on four datasets demonstrate that MulCoT-RD, with only 3B parameters, achieves strong performance on JMSRC while exhibiting robust generalization and enhanced interpretability.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haonan Shangguan, Xiaocui Yang, Shi Feng, Daling Wang, Yifei Zhang, Ge Yu
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
