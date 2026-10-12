---
title: "CopRoute: Dependence-Aware Conformal Routing for Language Models"
description: "Set-based language model routing aims to increase the coverage of the event where at least one model answers a query correctly while controlling the number of inference calls made."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2610.13276) · [PDF](https://arxiv.org/pdf/2610.13276)

## 一句话摘要

Set-based language model routing aims to increase the coverage of the event where at least one model answers a query correctly while controlling the number of inference calls made.

## 为什么值得关注

待编辑增强。

## 摘要原文

Set-based language model routing aims to increase the coverage of the event where at least one model answers a query correctly while controlling the number of inference calls made. Existing risk-controlled routing policies bound the all-miss risk (the probability that every model in the selected set fails) by calibrating a single conformal threshold and applying it to a nested family of model sets. Because each model is scored in isolation, these policies ignore the dependence structure of model failures. Models that share training data or architecture tend to fail on the same queries, so two individually strong models can be jointly redundant while a weaker but complementary model covers the queries that the others miss. To account for this dependence, which existing risk-controlled policies ignore, we propose CopRoute, which orders models by how many new queries each one answers correctly beyond those already selected, decides per query how far down that order to go, and then picks the smallest cutoff that still meets the target risk. We show that CopRoute's ordering attains, on the design data, the best guarantee any efficient fixed-ordering algorithm can give for the average number of calls to the first correct model, and that a separate calibration step certifies the all-miss risk of the deployed sets. On RouterBench and RouterEval, CopRoute attains the fewest certified calls on nine of ten datasets at a target risk of 0.05 and on eight of ten at 0.10, making up to 79 percent fewer calls (median 24 percent) than the state-of-the-art risk-controlled policy at the same certified all-miss risk.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Siva Rajesh Kasa, Santhosh Kumar Kasa, Karan Gupta
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
