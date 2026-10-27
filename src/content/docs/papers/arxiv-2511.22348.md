---
title: "FADiff: Fusion-Aware Differentiable Optimization for DNN Scheduling on Tensor Accelerators"
description: "Efficiently deploying Deep Neural Networks (DNNs) - particularly Large Language Models (LLMs) - on tensor accelerators is essential for achieving high throughput and energy efficiency at the edge."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2511.22348) · [PDF](https://arxiv.org/pdf/2511.22348)

## 一句话摘要

Efficiently deploying Deep Neural Networks (DNNs) - particularly Large Language Models (LLMs) - on tensor accelerators is essential for achieving high throughput and energy efficiency at the edge.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficiently deploying Deep Neural Networks (DNNs) - particularly Large Language Models (LLMs) - on tensor accelerators is essential for achieving high throughput and energy efficiency at the edge. However, the combinatorial explosion of the joint design space spanning intra-layer mapping and inter-layer fusion renders existing approaches inadequate. In this work, we present FADiff, a gradient-based optimization framework that automatically discovers optimal mapping and fusion strategies to accelerate DNN inference. We first formulate a unified, differentiable analytical cost model that accurately estimates the energy and latency of individual layer mappings as well as diverse fusion configurations. We then combine CP-SAT-based pre-enumeration of feasible discrete candidates with augmented-Lagrangian penalties over continuous relaxations, enabling a constrained gradient-based search that efficiently navigates the vast design space to identify optimal joint strategies. Experimental results show that FADiff consistently outperforms prior methods, delivering superior optimization quality with significantly faster convergence in both energy and latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shuao Jia, Zichao Ling, Chen Bai, Bei Yu, Kang Zhao, Jianwang Zhai
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
