---
title: "OpWeave: Flexible Operator Disaggregation for Heterogeneous LLM Serving"
description: "LLM serving systems increasingly disaggregate inference into finer-grained stages, with recent approaches separating attention from FFN or MoE execution during decode."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.14237) · [PDF](https://arxiv.org/pdf/2609.14237)

## 一句话摘要

LLM serving systems increasingly disaggregate inference into finer-grained stages, with recent approaches separating attention from FFN or MoE execution during decode.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM serving systems increasingly disaggregate inference into finer-grained stages, with recent approaches separating attention from FFN or MoE execution during decode. This operator-level disaggregated serving (ODS) can improve hardware matching and enable independent scaling, particularly across heterogeneous devices. However, existing systems fix operator boundaries and lack a unified characterization of when disaggregation reduces serving cost. We present OpWeave, an end-to-end framework for heterogeneous ODS. OpWeave provides an analytical cost model that bounds the gains of homogeneous and heterogeneous ODS over colocated serving. It jointly optimizes operator partitioning and deployment configuration through a regularity-aware planner that keeps the search tractable even for hybrid-attention models. A vLLM-based runtime executes the synthesized plans with flexible operator stages across heterogeneous device groups. In our evaluation, OpWeave reduces serving cost by up to $1.78\times$ on homogeneous and $1.89\times$ on heterogeneous GPU clusters relative to the best feasible baseline, while meeting latency SLOs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zikun Li, Yixuan Mei, Shiqi Pan, Zixuan Chen, Xiaowen Zhang, Mengdi Wu, Shuhuai Lin, Yutong Yang, Zhihao Zhang, Xupeng Miao, Rashmi Vinayak, Zhihao Jia
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
