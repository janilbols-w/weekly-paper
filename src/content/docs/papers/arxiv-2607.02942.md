---
title: "Serving Agentic Workflows with a Physical-Plan Compiler and Adaptive Runtime"
description: "Efficient serving of agentic workflows requires selecting each LLM node's model, verification policy, and backend to balance output quality, latency, and throughput."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2607.02942) · [PDF](https://arxiv.org/pdf/2607.02942)

## 一句话摘要

Efficient serving of agentic workflows requires selecting each LLM node's model, verification policy, and backend to balance output quality, latency, and throughput.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficient serving of agentic workflows requires selecting each LLM node's model, verification policy, and backend to balance output quality, latency, and throughput. These assignments must also adapt to changes in serving load. Existing approaches address parts of this problem through model routing, verifier placement, and backend scheduling. However, independent optimization overlooks their dependencies: model and backend choices determine verification cost, while verification changes the quality-cost trade-off among models. Ignoring these interactions can waste serving resources and degrade workflow performance. To address this problem, we propose \textbf{Dyserve}, which provides the missing workflow physical-planning layer between orchestration and model serving through compiler-runtime co-design. Our design is guided by three observations: planning headroom is request-dependent; node vulnerability, the impact of local errors on final correctness, depends on position and task type; and serving load changes the cost of a plan during execution. For each request, its profile-guided compiler jointly selects node implementations and prepares pressure-specialized variants for the materialized workflow. The runtime selects variants using live backend pressure and updates only undispatched assignments, without invoking the optimizer on the load-change path. Across four agentic workloads, Dyserve improves accuracy by \textbf{3-9} percentage points with \textbf{1.1-6.8}$\times$ mean-latency speedups over the highest-accuracy evaluated baseline for each workload. On a burst trace, variant switching raises the fraction of correct, on-time completions from \textbf{18.1\%} to \textbf{67.2\%} relative to admission-only execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiayi Qian, Yichong Zhang, Hanchen Yang, Chun Tao, Souvik Kundu, Zishen Wan, Tushar Krishna
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
