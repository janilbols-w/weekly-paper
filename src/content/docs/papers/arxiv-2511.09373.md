---
title: "Routesplain: Towards Faithful and Intervenable Routing for Software-related Tasks"
description: "LLMs now tackle a wide range of software-related tasks, yet we show that their performance varies markedly both across and within these tasks."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2511.09373) · [PDF](https://arxiv.org/pdf/2511.09373)

## 一句话摘要

LLMs now tackle a wide range of software-related tasks, yet we show that their performance varies markedly both across and within these tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLMs now tackle a wide range of software-related tasks, yet we show that their performance varies markedly both across and within these tasks. Routing user queries to the appropriate LLMs can therefore help improve response quality while reducing cost. Prior work, however, has focused mainly on general-purpose LLM routing via black-box models. We introduce Routesplain, the first LLM router for software-related tasks, including multilingual code generation and repair, input/output prediction, and computer science QA. Unlike existing routing approaches, Routesplain first extracts human-interpretable concepts from each query (e.g., task, domain, reasoning complexity) and only routes based on these concepts, thereby providing intelligible, faithful rationales. We evaluate Routesplain on 16 state-of-the-art LLMs across eight software-related tasks; Routesplain outperforms individual models both in terms of accuracy and cost, and equals or surpasses all black-box baselines, with concept-level intervention highlighting avenues for further router improvements.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Adam \v{S}torek, Vikas Upadhyay, Marianne Menglin Liu, Daniel W. Peterson, Anshul Mittal, Sujeeth Bharadwaj, Fahad Shah, Sujith Ravi, Dan Roth
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
