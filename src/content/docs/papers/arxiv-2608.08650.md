---
title: "The Evolution of Mixture-of-Experts Architectures in Large Language Models: Routing, Topology, Load Balancing, and Expert Parallelism"
description: "Mixture-of-Experts models increase parameter capacity while keeping the computation activated by each token bounded, but their architectural evolution cannot be explained by a chronological list of model releases alone."
---

**评分：38/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2608.08650) · [PDF](https://arxiv.org/pdf/2608.08650)

## 一句话摘要

Mixture-of-Experts models increase parameter capacity while keeping the computation activated by each token bounded, but their architectural evolution cannot be explained by a chronological list of model releases alone.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts models increase parameter capacity while keeping the computation activated by each token bounded, but their architectural evolution cannot be explained by a chronological list of model releases alone. This technical survey synthesizes primary papers, official technical reports, and prior surveys to organize modern Mixture-of-Experts systems along five coupled dimensions: expert granularity, expert topology, routing freedom, the scope of load balancing, and execution structure. We describe eight architectural milestones as a dependency graph with six mainline developments and two orthogonal branches, rather than as eight successive generations. We then analyze individual systems through four control planes: Expert Topology, Routing, Balance, and Expert Parallelism. These planes specify which experts exist, which experts process each token, how aggregate load is controlled, and how selected computation is mapped onto physical devices. The framework connects algorithmic choices such as Top-k routing, shared experts, fine-grained experts, and dynamic expert composition with systems concerns including token dispatch, device placement, all-to-all communication, and communication-computation overlap. We conclude with equal-budget pretraining experiments, quality and systems metrics, and open research questions. The main trend is a shift from merely activating more sparse parameters toward decoupling semantic routing, computational budgets, and physical execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiguo Li
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
