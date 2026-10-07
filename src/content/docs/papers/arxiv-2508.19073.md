---
title: "AEGIS: Runtime-Guided GPU Collocation for Multi-Tenant Deep Learning Training"
description: "Deep learning training commonly runs on shared multi-tenant GPU servers, where exclusive allocation provides isolation but can leave resources underutilized and increase queueing time."
---

**评分：44/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2508.19073) · [PDF](https://arxiv.org/pdf/2508.19073)

## 一句话摘要

Deep learning training commonly runs on shared multi-tenant GPU servers, where exclusive allocation provides isolation but can leave resources underutilized and increase queueing time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep learning training commonly runs on shared multi-tenant GPU servers, where exclusive allocation provides isolation but can leave resources underutilized and increase queueing time. Collocation can improve efficiency, but interference-agnostic placement may cause severe slowdowns, while inaccurate memory information can lead to out-of-memory (OOM) failures. We present AEGIS, a server-scale runtime scheduling system for controlled collocation of deep learning training workloads on shared multi-GPU servers. AEGIS integrates memory feasibility, post-placement observation, runtime-pressure filtering, placement, and OOM-aware recovery in a single scheduling loop. After placement, AEGIS observes workload activity before permitting further collocation, then uses low-overhead telemetry to determine whether a GPU can safely accept additional work. OOM failures trigger retries under progressively safer memory conditions, eventually falling back to exclusive execution. This online approach avoids costly offline pairwise compatibility profiling. We evaluate AEGIS using vision, Transformer, recommendation, and LLM-style workloads across three production-derived traces. AEGIS reduces geometric-mean makespan by 16% relative to Lucid, 21% relative to Horus, and 27% relative to exclusive allocation. Sensitivity studies show that activity-anchored observation and runtime-pressure filtering balance conservative isolation against interference-agnostic collocation, improving makespan while limiting sharing-induced per-task slowdown.

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

- taxonomy keywords: multi-tenant
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ehsan Yousefzadeh-Asl-Miandoab, B\"u\c{s}ra Karatay Demiray, Florina M. Ciorba, Pamela Delgado, P{\i}nar T\"oz\"un
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
