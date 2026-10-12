---
title: "AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents"
description: "Tool-using agents increasingly require a common substrate for building, training, evaluating, distilling, and maintaining agentic systems, yet existing tooling typically addresses these stages in isolation."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.13335) · [PDF](https://arxiv.org/pdf/2610.13335)

## 一句话摘要

Tool-using agents increasingly require a common substrate for building, training, evaluating, distilling, and maintaining agentic systems, yet existing tooling typically addresses these stages in isolation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tool-using agents increasingly require a common substrate for building, training, evaluating, distilling, and maintaining agentic systems, yet existing tooling typically addresses these stages in isolation. We present AgentTune, a source-available Python library that provides a unified framework for developing and optimizing tool-using agents. At its core, AgentTune introduces a two-tier EventLog representation that preserves agent trajectories while supporting consistent projections for training, evaluation, and auditing. Building on this substrate, the library provides a shared agent runtime, tool-calling reinforcement learning, agentic distillation, retrieval-augmented generation, decision workflows, evaluation utilities, and a designed path toward self-healing agents. These components are exposed through composable interfaces so that agent strategies, training methods, evaluation procedures, and recovery mechanisms can be combined without requiring separate representations or pipelines. We demonstrate the framework across agentic tasks including legal contract search and domain-specific applications, illustrating its use for trajectory-based optimization, tool-use evaluation, and cross-task agent development. AgentTune is released as a source-available library at https://github.com/Lexsi-Labs/AgentTune

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：R E Zera Marveen Lyngkhoi, Abhivansh Gupta, Vidushee Vats, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu, Pratinav Seth
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Lexsi-Labs/AgentTune](https://github.com/Lexsi-Labs/AgentTune)
- 阅读深度：metadata
