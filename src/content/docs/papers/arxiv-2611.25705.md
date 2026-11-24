---
title: "STARK: Moving towards Personalized Agents That Truly Learn and Remember"
description: "Long-term memory is essential for personalized agentic systems that interact with users over long time periods, yet current architectures only capture what happened while leaving the reasoning of why it happened to be derived later by underlying LLMs."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.25705) · [PDF](https://arxiv.org/pdf/2611.25705)

## 一句话摘要

Long-term memory is essential for personalized agentic systems that interact with users over long time periods, yet current architectures only capture what happened while leaving the reasoning of why it happened to be derived later by underlying LLMs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-term memory is essential for personalized agentic systems that interact with users over long time periods, yet current architectures only capture what happened while leaving the reasoning of why it happened to be derived later by underlying LLMs. These events can, however, convey not only what a user experienced but also how that experience shaped their behavioral patterns. We introduce STARK, a dual-graph memory architecture which treats these events not just as nodes but also as edges between behavioral insights. STARK maintains an Episodic Graph which records interactions as temporally, causally, and semantically linked episodes; and an Insight Graph which represents LLM-extracted behavioral signals scored by how many events support them, connected by the very events that led to them. At inference, behavioral knowledge is retrieved directly from insight nodes grounded by event-as-edges, eliminating repeated episodic traversal. The event-as-edge structure also naturally enables projecting the knowledge graph into a relational embedding space where cross-user transfer becomes possible under shared contextual circumstances, allowing the system to infer missing insights for cold-start users. Evaluations show that STARK improves by 1.48 judge score on LongMemEval information extraction and 0.93 on LoCoMo open domain questions over state of the art. On the public LongLaMP abstract-generation benchmark, cross-user transfer improves open-ended judge scores by 0.7 points and ROUGE-L by 3 at 5% graph sparsity.

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

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Aryan Jain, Abhishek Jha, Anish Nediyanchath, Promod Yenigalla
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
