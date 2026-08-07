---
title: "FinPerMA: A Theory-Informed, Event-Grounded Personalized-Memory Benchmark for LLM Agents"
description: "Large language model (LLM) agents are increasingly used as personalized assistants in high-stakes domains such as financial advising, yet it remains unclear whether they can maintain and update an individualized user model over long horizons."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](http://arxiv.org/abs/2608.04095v1) · [PDF](https://arxiv.org/pdf/2608.04095v1)

## 一句话摘要

Large language model (LLM) agents are increasingly used as personalized assistants in high-stakes domains such as financial advising, yet it remains unclear whether they can maintain and update an individualized user model over long horizons.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) agents are increasingly used as personalized assistants in high-stakes domains such as financial advising, yet it remains unclear whether they can maintain and update an individualized user model over long horizons. Existing personalized-memory benchmarks primarily test factual retention or rely on weakly constrained model-generated trajectories, leaving event-driven preference adaptation underexplored. We introduce FinPerMA, an event-grounded benchmark that evaluates personalized memory against frozen longitudinal investor trajectories. Its generation pipeline combines deterministic, theory-informed impact rules, controlled LLM narration, and automated quality screening; a Post-Shock checkpoint isolates whether an agent has integrated a material event into its persistent user model. On 2,994 questions from 276 personas, seven frontier LLMs and up to seven memory configurations remain far from saturated: no full-context configuration exceeds approximately 0.47 overall accuracy or approximately 39% on multiple-choice questions. Attribution analysis shows that summary-based memory often preserves factual details while losing the preference signals needed for personalization; simple retrieval can therefore outperform purpose-built memory systems, with the gap widening after shocks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ben Wang, Kang Zhou, Lifan Guo, Feng Chen, Chi Zhang
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
