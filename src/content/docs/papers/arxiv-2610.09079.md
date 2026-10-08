---
title: "Large-scale Repository Engineering via Agent-Native Reusable Code Primitives"
description: "Large language models equipped with development environments have moved code generation toward repository-scale construction, yet building complete repositories remains difficult because interacting modules, interfaces, configurations, tests, and dependencies must work together."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.09079) · [PDF](https://arxiv.org/pdf/2610.09079)

## 一句话摘要

Large language models equipped with development environments have moved code generation toward repository-scale construction, yet building complete repositories remains difficult because interacting modules, interfaces, configurations, tests, and dependencies must work together.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models equipped with development environments have moved code generation toward repository-scale construction, yet building complete repositories remains difficult because interacting modules, interfaces, configurations, tests, and dependencies must work together. We introduce Code Primitives, agent-native reusable executable components with interface contracts, dependency closures, validation tests, and provenance. Each primitive uses a resident LLM to assess relevance and adapt its implementation, interfaces, and dependencies to the target repository, and we organize 1,424 validated primitives in CodeFace, a searchable library for repository construction. We introduce LEGO (Large-scale repository Engineering via aGent-native reusable cOde primitives), which activates task-relevant primitives, integrates their adapted implementations with task-specific code while resolving cross-component constraints, and revises the result against executed tests. To measure construction end to end, we build LEGO-REPO, a benchmark of 522 executable reconstruction tasks spanning seven software domains, 22 capability tracks, and five difficulty levels, scored against native test suites between an empty-package floor and original-source ceiling. The strongest of 13 evaluated backbones reaches a delivery score of 0.318 and scores zero on 41.0% of tasks; LEGO improves all 13 by 0.1474 on average and raises GPT-5.6-terra from 0.3180 to 0.5134 (+61.4%). In controlled comparisons, adapted primitives outperform retrieved code supplied as context or vendored unchanged. The effect persists against independent repository agents, across three external benchmarks, and with a disjointly re-mined CodeFace; GPT-OSS-20B for adaptation and diagnosis retains 95.1% of the homogeneous score at 24.0% lower cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haibo Jin, Peng Kuang, Xucheng Yu, Jerry Wang, Dehao Wu, Haohan Wang
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
