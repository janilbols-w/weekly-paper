---
title: "Atlas: Optimizing Deployment of Compound AI Workflows on Heterogeneous Clusters"
description: "Compound AI workflows are increasingly used to serve complex AI tasks by coordinating multiple AI models and software components."
---

**评分：38/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.04513) · [PDF](https://arxiv.org/pdf/2609.04513)

## 一句话摘要

Compound AI workflows are increasingly used to serve complex AI tasks by coordinating multiple AI models and software components.

## 为什么值得关注

待编辑增强。

## 摘要原文

Compound AI workflows are increasingly used to serve complex AI tasks by coordinating multiple AI models and software components. This approach enables deployment flexibility, as each workflow stage can expose different model variants and resource requirements, but it also expands the deployment choices. A deployment must choose an execution plan that selects AI models for each compound AI workflow stage and places them on a heterogeneous cluster in order to satisfy SLOs. Deployment optimizers therefore need estimates to compare many candidate plans and identify feasible ones. System metrics can often be profiled per stage and composed according to workflow topology, but accuracy cannot, as errors and information loss at upstream stages affect the accuracy of downstream stages. Existing approaches either profile complete configurations end to end, which scales poorly, or use product-based accuracy surrogates that treat stages as independent and can misrank candidate plans. We introduce Atlas, a framework for optimizing compound AI deployments under SLO constraints. Atlas uses MAP, a Markovian Accuracy Predictor, to estimate configuration accuracy from local conditional accuracy transitions between adjacent workflow stages. MAP discretizes intermediate outputs into accuracy buckets and composes transition profiles according to workflow topology, giving the optimizer an accuracy estimate without exhaustive end-to-end profiling. Atlas formulates execution-plan selection as a mixed-integer linear program that maximizes predicted accuracy subject to SLOs. Across four compound AI workflows, MAP achieves Spearman correlation up to 0.947 while reducing profiling cost by up to 2.6x relative to exhaustive end-to-end profiling. Guided by MAP, the Atlas optimizer selects execution plans within 0.03 of oracle accuracy while reducing deployment cost by up to 42% through heterogeneous placement.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Milos Gravara, Andrija Stanisic, Stefan Nastic
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
