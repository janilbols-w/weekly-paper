---
title: "DynBranch: Speculative Subgraph Reuse for Dynamic Agentic LLM Serving"
description: "Agentic LLM workflows decide their execution paths at runtime."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.31047) · [PDF](https://arxiv.org/pdf/2609.31047)

## 一句话摘要

Agentic LLM workflows decide their execution paths at runtime.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic LLM workflows decide their execution paths at runtime. Downstream computation may be predictable, or may have run before, yet it cannot begin until the model or the user resolves the branch. We call this serialization the branch-resolution barrier. Caching alone does not hide it: the key that identifies a reusable result is not known until then. In this paper, we propose DynBranch, which makes an unresolved branch addressable before it resolves. Its stable coordinate lets candidate subgraphs run during resolution and completed subgraph results be reused across later requests. A two-level controller admits this work when its expected benefit exceeds the load price. DynBranch sits at the model-API boundary and requires no changes to agent harnesses or model execution engines. Across four agentic workloads with Qwen3-32B on 4x H200 GPUs, DynBranch reduces mean latency by up to 32% over each workload's strongest prior system and by 46-66% against a no-reuse floor, while preserving workflow results. The benefit persists across backbone families and on a commodity Qwen3-8B/RTX 4090 deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Junyi Shen, Noppanat Wadlom, Zhengyuan Su, Yao Lu
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
