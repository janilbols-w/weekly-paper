---
title: "The Collaboration Gap: Exploration and Benchmarking of Open-World Agentic Cooperation"
description: "The trajectory of AI development suggests that we will increasingly rely on agent-based systems powered by language models, composed of independently developed agents with different information, privileges, and tools."
---

**评分：39/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2511.02687) · [PDF](https://arxiv.org/pdf/2511.02687)

## 一句话摘要

The trajectory of AI development suggests that we will increasingly rely on agent-based systems powered by language models, composed of independently developed agents with different information, privileges, and tools.

## 为什么值得关注

待编辑增强。

## 摘要原文

The trajectory of AI development suggests that we will increasingly rely on agent-based systems powered by language models, composed of independently developed agents with different information, privileges, and tools. The success of these systems will depend critically on effective collaboration among these heterogeneous agents, even under partial observability. Despite intense interest, the literature lacks empirical studies evaluating agentic collaboration without relying on fixed communication protocols, limiting insights for open-world deployments. We propose an illustrative collaborative maze-solving benchmark that (i) isolates collaborative capabilities, (ii) modulates problem complexity, (iii) enables scalable automated grading, and (iv) imposes no output-format constraints, benchmarking unguided, natural communication. Using this benchmark, we evaluate 32 leading open- and closed-source models in solo, homogeneous, and heterogeneous pairings. Our results reveal a surprising collaboration gap: models that perform well solo often degrade substantially when required to collaborate. We identify mitigations that show remarkable influence. For example, a small nudge via a relay inference approach, where a stronger agent leads before handing off to a weaker one, closes much of the gap. Our findings argue for (1) collaboration-aware evaluation, (2) training strategies to enhance collaborative capabilities, and (3) deliberate interaction design to elicit agents' collaboration skills, principles relevant to AI-AI and human-AI settings where agents must establish common ground.

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

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tim R. Davidson, Adam Fourney, Saleema Amershi, Robert West, Eric Horvitz, Ece Kamar
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
