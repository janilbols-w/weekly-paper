---
title: "A Physics-Guided Transformer Framework for Electromigration Analysis in Multi-Segment Interconnects"
description: "As technology scales to smaller nodes, increasing current densities make electromigration (EM) one of the dominant reliability challenges in on-chip interconnects."
---

**评分：38/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2610.06464) · [PDF](https://arxiv.org/pdf/2610.06464)

## 一句话摘要

As technology scales to smaller nodes, increasing current densities make electromigration (EM) one of the dominant reliability challenges in on-chip interconnects.

## 为什么值得关注

待编辑增强。

## 摘要原文

As technology scales to smaller nodes, increasing current densities make electromigration (EM) one of the dominant reliability challenges in on-chip interconnects. Accurate transient stress analysis is needed to identify wires susceptible to EM degradation, but applying physics-based solvers across many interconnects remains computationally expensive. This paper proposes a physics-guided transformer framework for fast EM stress prediction in multi-segment interconnect lines. The framework converts each line into geometry- and DC-aware segment tokens and uses transformer attention to capture line-level context. A lightweight query decoder then predicts stress at selected locations and time instants. The model is trained with an objective that combines normalized supervised regression, linewise relative-$L_2$ loss, and physics-guided continuity and terminal-flux terms. Experiments on IBM power grid benchmarks show that the proposed model achieves relative-$L_2$ error below 8\% and reaches up to 2459.68$\times$ speedup compared with the matrix exponential~solver.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Pavlos Stoikos, Anuj Pathania, George Floros
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
