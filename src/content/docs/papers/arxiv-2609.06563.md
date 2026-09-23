---
title: "MARBO: Relational Belief Grounding for LLM Agents in Social Deduction Games"
description: "Social deduction games (SDGs) require agents to reason under partial observability by maintaining relational beliefs about hidden roles and team alignments."
---

**评分：42/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2609.06563) · [PDF](https://arxiv.org/pdf/2609.06563)

## 一句话摘要

Social deduction games (SDGs) require agents to reason under partial observability by maintaining relational beliefs about hidden roles and team alignments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Social deduction games (SDGs) require agents to reason under partial observability by maintaining relational beliefs about hidden roles and team alignments. While recent LLM-agent approaches improve gameplay through prompting and preference optimization, they often optimize actions and in-game speech without explicitly grounding them in such beliefs. This frequently leads to strategically inconsistent behavior, especially for compact LLM agents. We introduce Multi-Agent Relational Belief Optimization (MARBO), a belief-grounded preference optimization framework that leverages relational beliefs to guide strategic decisions and in-game speech. MARBO provides preference feedback only when behaviors are supported by reliable relational beliefs and lead to strategically favorable social outcomes, encouraging more consistent learning under uncertainty. Experiments on representative SDGs show that MARBO enables compact LLM agents to consistently outperform existing baselines. The Code is available on https://github.com/PleaseTakemeAway/MARBO.

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

- taxonomy keywords: observability
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hwang Yechan, Bae Sangjun, Kim Jeongmo, Bang Sangwoo, Han Seungyul
- 发布：2026-09-09；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/PleaseTakemeAway/MARBO](https://github.com/PleaseTakemeAway/MARBO)
- 阅读深度：metadata
