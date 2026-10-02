---
title: "One Readout, Many Repairs: Diffusion-Guided Hierarchical Search for Tool-Agent Repair"
description: "Tool agents use large language models to act through external tools, yet successfully executed calls can still leave user requests unfulfilled."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2609.34879) · [PDF](https://arxiv.org/pdf/2609.34879)

## 一句话摘要

Tool agents use large language models to act through external tools, yet successfully executed calls can still leave user requests unfulfilled.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tool agents use large language models to act through external tools, yet successfully executed calls can still leave user requests unfulfilled. Tool-agent repair seeks alternative call sequences that execute successfully and fulfill the original requests. However, repair requires exploring both operation choices and their concrete realizations, making complete-sequence regeneration costly. Moreover, regeneration repeats operation selection even when failure arises from how those operations are realized. The resulting challenge is to reduce this repetition while preserving exploration of alternative operations and realizations. Therefore, we formulate repair as hierarchical search over operation supports, which we introduce as sets of permitted operation types that define reusable search regions for concrete tool-call sequences. We propose ReCommit, a training-free, diffusion-guided framework for improving tool-agent failure recovery while reducing repair computation. ReCommit amortizes operation-level proposal computation across repair trials by reusing operation-type scores from a single parallel readout of a masked diffusion language model. These scores guide search across supports, while realization search explores alternative entity bindings, arguments, and action composition within each support. Experiments on real failures across four enterprise services in the Agent-Diff benchmark show 75.9\% and 63.2\% relative recovery gains with 61.3\% and 51.3\% reductions in mean full-budget repair time at repair budgets $B=3$ and $B=13$, respectively, over the strongest evaluated 8B comparison method. ReCommit achieves a favorable recovery--cost trade-off, including in comparisons with the evaluated 32B models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: failure recovery
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiang Xia, Cheng Yan, Wuyang Zhang, Fan Xu, Zhijun Fan, Shuyuan Zhang, Yanyong Zhang
- 发布：2026-09-28；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
