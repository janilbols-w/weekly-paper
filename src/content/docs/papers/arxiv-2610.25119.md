---
title: "Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents"
description: "Large language model (LLM) agents increasingly rely on external memory to accumulate past experiences for continual adaptation."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.25119) · [PDF](https://arxiv.org/pdf/2610.25119)

## 一句话摘要

Large language model (LLM) agents increasingly rely on external memory to accumulate past experiences for continual adaptation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) agents increasingly rely on external memory to accumulate past experiences for continual adaptation. However, effectively reusing memory requires accurately assessing its value, as retrieved experiences may become unreliable when transferred across task contexts. Despite its importance, memory valuation remains largely underexplored, with existing methods relying on historical retrieval success rates that overlook the context dependency of memory usefulness and the varying reliability of estimates under different amounts of evidence. Inspired by the Bayesian brain hypothesis, we propose BEAM (Bayesian-style Evolutionary Agentic Memory), a framework that reformulates memory value evaluation as a parameterized cognitive inference process, where memory value is represented as a context-conditioned dynamic belief rather than a passive historical statistic. Specifically, BEAM infers memory value beliefs from current task contexts and continuously calibrates them using execution feedback as empirical evidence, transforming memory from passive storage into an adaptive cognitive mechanism for continual self-evolution. Extensive experiments across reasoning and code generation benchmarks demonstrate that BEAM consistently improves memory utilization and enables continual self-evolution of LLM agents.

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

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiming Xu, Qian Yang, Zihan Chen, Yuefei Wu, Wenhan Zeng, Bin Shi, Bo Dong
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
