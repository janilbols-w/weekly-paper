---
title: "Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows"
description: "Running large language model (LLM) agents in production gets expensive fast."
---

**评分：53/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2609.32917) · [PDF](https://arxiv.org/pdf/2609.32917)

## 一句话摘要

Running large language model (LLM) agents in production gets expensive fast.

## 为什么值得关注

待编辑增强。

## 摘要原文

Running large language model (LLM) agents in production gets expensive fast. A frontier model (the largest, most capable tier) is accurate but can cost 25 times what a small model costs per token, and the gap compounds once a workflow chains several calls together. Planner-as-Router (PaR) attacks this from a different angle. Instead of leaving model-tier selection to some component downstream, it folds the choice into planning itself. As the planner breaks a query into subtasks, it also assigns each one a model size tier (small, mid, or frontier, ordered by capability and price), so the dependencies between subtasks are visible before any specialist runs. Unlike per-call routers such as cascade routing, which look at one node at a time, PaR sees the whole workflow up front and needs no separate router model or training data. We evaluate PaR with EntBench, a benchmark of 54 enterprise agentic tasks across seven classes, graded by actually running the generated Structured Query Language (SQL) and MongoDB queries against live databases. Over 1,157 evaluations spanning eight routers and three seeds, PaR stays on the observed cost-accuracy frontier. It matches a sink-frontier heuristic (frontier model on terminal nodes only) in accuracy at comparable cost and a faithful FrugalGPT cascade at lower cost, and cuts cost 44% against all-frontier routing while giving up 2.9 points of accuracy. Several accuracy gaps fall inside the plus-or-minus six-point confidence interval of a 54-task study, so we frame PaR's advantage as frontier position rather than a clean accuracy win. We also report a preliminary observation, not a validated result: a small pilot hints that cheap routing may carry a hidden compounding penalty on compositional workflows, which we frame as a hypothesis for future measurement. PaR, EntBench, and all evaluation code are open source.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Vivek Kumar Singh, Preeti Priyam, Gautam Bhowmick
- 发布：2026-09-26；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/vsingh45/par-entbench](https://github.com/vsingh45/par-entbench)
- 阅读深度：metadata
