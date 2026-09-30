---
title: "SEABench: Benchmarking Endogenous Misalignment In Self-Evolving Agents"
description: "Self-evolving LLM agents have gained prominence for their ability to improve after deployment by modifying their harness, including their controller instructions, memory management protocols, and reusable tools and skills, in response to user and environment feedback."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.35596) · [PDF](https://arxiv.org/pdf/2609.35596)

## 一句话摘要

Self-evolving LLM agents have gained prominence for their ability to improve after deployment by modifying their harness, including their controller instructions, memory management protocols, and reusable tools and skills, in response to user and environment feedback.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-evolving LLM agents have gained prominence for their ability to improve after deployment by modifying their harness, including their controller instructions, memory management protocols, and reusable tools and skills, in response to user and environment feedback. However, locally useful updates may persist into later tasks where they produce unsafe behavior, even without direct adversarial influence. To study this risk, we introduce SEABench, a benchmark for studying endogenous misalignment arising from agent self-evolution, with 48 longitudinal task sequences that span multiple evolution surfaces, task domains, and harm types in a rich personal-assistant environment. To account for the stochasticity inherent in agentic operations, we provide an adaptive trajectory discovery pipeline that probes for failures while preserving original task intent and supports causal attribution through paired non-evolving agents and attribution scores. Our evaluation across multiple recent LLMs, evolution surfaces, and harm types reveals that self-evolution indeed increases task completion rates but often at the cost of safety failures that are absent for paired non-evolving baseline agents. We also show that qualitatively different safety behaviors emerge across evolution surfaces and harm types. Further, we show that this divergence in safety behavior is reflected in agents' chain-of-thought reasoning, which yields an effective monitoring strategy that can mitigate unsafe behavior with a low false positive rate.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saswat Das, Parvati Viswanathan, Daniel Donnelly, Chang Huang, Sahar Abdelnabi, Ferdinando Fioretto
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
