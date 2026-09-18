---
title: "TuiML: Machine Learning for AI Agents"
description: "Machine-learning libraries such as Weka and scikit-learn were designed for human programmers."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.17984) · [PDF](https://arxiv.org/pdf/2609.17984)

## 一句话摘要

Machine-learning libraries such as Weka and scikit-learn were designed for human programmers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Machine-learning libraries such as Weka and scikit-learn were designed for human programmers. Language-model agents now use these same libraries by recalling APIs from memory and writing code, an approach that hides what a library offers, delays errors until runtime, and loses experimental state between turns. We present TuiML, a self-contained machine-learning library built for AI agents, with native algorithms across supervised, unsupervised, time-series, data handling, tuning, and evaluation tasks. Every component describes itself through machine-readable metadata and parameter schemas, so an agent can search the library, inspect components, compose validated workflows, and register new ones that become discoverable in turn. Every call is validated, seeded, and traced, and sessions export as runnable notebooks, making experiments reproducible by construction. One specification layer drives the Model Context Protocol (MCP), agent-framework adapters, a Python API, a CLI, and local model serving, while data and models never leave the machine. Benchmarks show TuiML remains predictively competitive with scikit-learn and Weka. While looking like a conventional library to a human user, TuiML is designed for agents first, allowing them to read, extend, and operate machine learning autonomously. TuiML is open source, with documentation at https://tuiml.ai.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 4 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nilesh Verma, Nick Lim, Albert Bifet, Bernhard Pfahringer
- 发布：2026-09-16；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
