---
title: "Predicting Program Exit Code with LLMs and Programming Language Semantics"
description: "Large language models (LLMs) have shown proficiency in various software engineering tasks, such as code generation and translation."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.00579) · [PDF](https://arxiv.org/pdf/2609.00579)

## 一句话摘要

Large language models (LLMs) have shown proficiency in various software engineering tasks, such as code generation and translation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have shown proficiency in various software engineering tasks, such as code generation and translation. However, a key limitation in their performance may be their (lack of) understanding of programming-language semantics. Even when explicit semantics are given, it remains unclear whether LLMs apply those rules or lean on priors learned during pre-training instead. We study if LLMs lean on priors or given semantics with a novel task--Program Executability Prediction (PrEx)--that asks models to predict whether a program is semantically valid or invalid (and, if invalid, which formal rule it violates) given the program's syntax and operational semantics. Because PrEx requires both valid and invalid programs, we build a dataset with systematically generated invalid transformations derived from valid programs. We evaluate open-source coding LLMs under two semantic formalisms and two semantic shifts across Human-Written, LLM-Translated, and Fuzzer-Generated program splits. Our findings show that LLMs lean on pre-training priors rather than systematically applying the given rules, performing especially poorly on modified semantics and degrading further as program complexity increases. PrEx is available at https://github.com/EngineeringSoftware/prex.

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

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Lara Marinov, Aditya Thimmaiah, Jayanth Srinivasa, Junyi Jessy Li, Milos Gligoric
- 发布：2026-09-01；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/EngineeringSoftware/prex](https://github.com/EngineeringSoftware/prex)
- 阅读深度：metadata
