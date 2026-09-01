---
title: "QAQ: Bidirectional Semantic Coherence for Selecting High-Quality Synthetic Code Instructions"
description: "Synthetic data has become essential for training code generation models, yet it introduces significant noise and hallucinations that are difficult to detect with current metrics."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2603.12165) · [PDF](https://arxiv.org/pdf/2603.12165)

## 一句话摘要

Synthetic data has become essential for training code generation models, yet it introduces significant noise and hallucinations that are difficult to detect with current metrics.

## 为什么值得关注

待编辑增强。

## 摘要原文

Synthetic data has become essential for training code generation models, yet it introduces significant noise and hallucinations that are difficult to detect with current metrics. Existing data selection methods like Instruction-Following Difficulty (IFD) typically assess how hard a model generates an answer given a query ($A|Q$). However, this metric is ambiguous on noisy synthetic data, where low probability can distinguish between intrinsic task complexity and model-generated hallucinations. Here, we propose QAQ, a novel data selection framework that evaluates data quality from the reverse direction: how well can the answer predict the query ($Q|A$)? We define Reverse Mutual Information (RMI) to quantify the information gain about the query conditioned on the answer. Our analyses reveal that both extremes of RMI signal quality issues: low RMI indicates semantic misalignment, while excessively high RMI may contain defect patterns that LLMs easily recognize. Furthermore, we introduce a selection strategy based on the disagreement between strong and weak models to identify samples that are valid yet challenging. Experiments across three datasets spanning code generation (WarriorCoder, Magpie-Qwen2.5-Coder-Pro-300K) and math reasoning (OpenR1-Math-220k) demonstrate that selecting just 25\% of data using stratified RMI matches full-data performance while being consistently competitive with or better than existing data selection methods. Our approach highlights the importance of bidirectional semantic coherence in synthetic data curation, offering a scalable pathway to reduce computational costs without sacrificing model capability. Code is available at https://github.com/XXSg559/QAQ.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jiayin Lei, Ming Ma, Yunxi Duan, Chenxi Li, Tianming Yang
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/XXSg559/QAQ](https://github.com/XXSg559/QAQ)
- 阅读深度：metadata
