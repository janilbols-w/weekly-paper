---
title: "Introspective Uncertainty Estimation for LLM-Based Code Generation"
description: "Large Language Models (LLMs) are increasingly used for code generation but can produce fluent yet functionally incorrect outputs, which limits trust in their usage for practical software engineering workflows."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.13975) · [PDF](https://arxiv.org/pdf/2609.13975)

## 一句话摘要

Large Language Models (LLMs) are increasingly used for code generation but can produce fluent yet functionally incorrect outputs, which limits trust in their usage for practical software engineering workflows.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) are increasingly used for code generation but can produce fluent yet functionally incorrect outputs, which limits trust in their usage for practical software engineering workflows. This thesis investigates whether Introspective Uncertainty Estimation (IUE), based on internal hidden-state representations of LLMs, can reliably indicate correctness at the response and line levels for code generation tasks. The objective is to determine the extent to which hidden states encode information about functional code correctness and how this can be leveraged for practical risk assessment and fault localization. Methodologically, this thesis combines response-level evaluation on LiveCodeBench (LCB) and BigCodeBench (BCB) with an augmentation pipeline that derives token- and line-level labels from incorrect programs. In this setup, it compares static and dynamic response-level features, evaluates generalization across tasks, programming domains, and token positions, and studies line-level fault localization. The results show that hidden states contain a strong response-level correctness signal. Static single-token probes perform best, while more elaborate dynamic strategies yield no consistent gains. While generalization across tasks, domains, and token positions is feasible, setting-dependent degradation largely remains for real-world software projects. At a fine granularity, line-level prediction is substantially harder than response-level estimation. However, in a conditional localization setup with known-incorrect programs, Top-K point-of-failure ranking remains effective. Overall, the findings suggest that hidden states are a robust and informative resource for estimating functional code correctness, supporting a two-stage workflow that combines response-level risk screening with targeted line-level prioritization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Thomas Klassert
- 发布：2026-09-12；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
