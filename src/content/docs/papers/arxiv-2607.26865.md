---
title: "Think Short, Defer Smart, Act, and Repeat: Calibrated Reasoning and Uncertainty-Aware Deferral for Edge LLM Agents"
description: "LLM agents following the ReAct paradigm are promising enablers of complex multi-step tasks, including multi-hop question answering, code generation, and control of physical AI systems."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2607.26865) · [PDF](https://arxiv.org/pdf/2607.26865)

## 一句话摘要

LLM agents following the ReAct paradigm are promising enablers of complex multi-step tasks, including multi-hop question answering, code generation, and control of physical AI systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents following the ReAct paradigm are promising enablers of complex multi-step tasks, including multi-hop question answering, code generation, and control of physical AI systems. Yet, when deployed at the edge, they must tightly manage their reasoning budget while remaining reliable and deferring to a cloud-side model only when local uncertainty is too high to act safely. We propose Think Short, Defer Smart (TSDS), a framework that synergistically integrates a lightweight convergence probe, which halts on-device reasoning once the intended action has stabilized, with a perplexity-based deferral rule that escalates uncertain actions to a cloud-side model. Both mechanisms are jointly calibrated on end-to-end episode trajectories via a multi-objective Learn-Then-Test (LTT) procedure, providing simultaneous finite-sample guarantees on expected episode reward and cloud-call rate. We evaluate TSDS on four ReAct benchmarks spanning arithmetic reasoning (GSM8K), multi-hop question answering (HotpotQA), code generation (MBPP), and multi-step embodied planning (household robot), and compare against thought-calibration-only and calibrated-deferral-only standalone baselines. TSDS reduces per-episode thinking compute by 43%-65% over deferral-only baselines across HotpotQA, MBPP, and the household robot task, while maintaining certified reward and cloud-call rate guarantees.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Amirmohammad Farzaneh, Osvaldo Simeone
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
