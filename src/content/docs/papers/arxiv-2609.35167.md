---
title: "EdgeCraft: Automated Model Crafting for Edge IoT"
description: "Machine learning (ML) increasingly powers Internet of Things (IoT) applications at the edge."
---

**评分：43/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.35167) · [PDF](https://arxiv.org/pdf/2609.35167)

## 一句话摘要

Machine learning (ML) increasingly powers Internet of Things (IoT) applications at the edge.

## 为什么值得关注

待编辑增强。

## 摘要原文

Machine learning (ML) increasingly powers Internet of Things (IoT) applications at the edge. Yet producing a deployable edge ML artifact for a specific scenario requires navigating a huge search space spanning data representation, model design, training on domain-specific data, and runtime customization. This workflow is fragmented and difficult to scale across diverse edge applications. We present EdgeCraft, an LLM-driven system that turns high-level intent into deployable edge ML artifacts. Building such a system raises two challenges: (1) How can an LLM be guided to find high-quality solutions that meet dynamic SLOs for task quality, latency, and energy? (2) How can trustworthy target-device verification be obtained at low cost? EdgeCraft addresses these challenges with two designs. (1) A constraint-aware synthesis tree explores alternative candidates and uses measured SLO gaps to guide each improvement. (2) A multi-fidelity verifier progressively combines low-cost checks with full target-device verification to reduce verification cost while preserving reliable verification results. It also records verified failures for reuse, avoiding repeated device work. To support concurrency, EdgeCraft provides a multi-tenant runtime that runs cloud training and target-device verification in parallel while isolating requests. Across 50 public tasks, EdgeCraft exceeds the task-specific Reference in best-observed quality on 40 tasks and finds an SLO-feasible artifact on 45, with the two outcomes overlapping on 38 tasks. Moreover, EdgeCraft achieves competitive performance on our self-collected SEN dataset, suggesting its generalizability to real-world IoT sensing tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant, slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Genglin Wang, Kaiwei Liu, Liekang Zeng, Wangsong Yin, Shangcheng Jin, Guoliang Xing, Zhenyu Yan
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
