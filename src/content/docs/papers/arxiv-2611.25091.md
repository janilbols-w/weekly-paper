---
title: "Berth: SLO-Preserving GPU Sharing Without New Preemption"
description: "Inference services keep GPUs reserved for their worst-case load, and most of that capacity sits idle."
---

**评分：49/100** · AI 基础设施 > 集群与资源系统 > GPU 调度与虚拟化

[论文原文](http://arxiv.org/abs/2611.25091v1) · [PDF](https://arxiv.org/pdf/2611.25091v1)

## 一句话摘要

Inference services keep GPUs reserved for their worst-case load, and most of that capacity sits idle.

## 为什么值得关注

待编辑增强。

## 摘要原文

Inference services keep GPUs reserved for their worst-case load, and most of that capacity sits idle. Filling it with best-effort work such as training is the obvious remedy, and latency is why it rarely happens: on a shared GPU, a request that must finish within milliseconds finds the best-effort job's kernels running or queued ahead of it. Spatial sharing cannot evict them, temporal sharing gives the request only its turn, and hardware partitioning protects it by idling what it does not use. Systems that keep both the SLO and the utilization have reached inside the stack (rewriting kernels, patching the driver, instrumenting the framework), which the operator of a closed GPU stack cannot do. This paper argues that reaching inside is unnecessary. The time-slicer built into commodity GPUs already preempts a running kernel within a fraction of a millisecond and switches the moment a context runs out of work; what it lacks is priority, and priority can be created from outside by controlling what the best-effort context has to run. Berth is a user-space system built on this observation: a preloaded shim feeds the best-effort job to the GPU only when no request needs it (feed control), a declared deadline reference extends the rule to continuous-batching LLM engines, and a shortened best-effort time slice, set without privileges, bounds what a long kernel can cost. Berth changes no application, framework, kernel or driver. Across 31 scenario points with MLPerf SLOs and 13 baselines, Berth meets SLOs within a few percentage points of running alone, above every baseline, with 2.7-3.5x the best-effort throughput of the strongest ones; beside LLM serving, it meets per-token targets for nearly every request while training keeps running. Sharing a closed GPU under SLOs needs no new preemption mechanism, only control over what the existing one sees.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu sharing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mohammadali Khodabandehlou, Mahdi Alizadeh, Lei Gao, Murali Annavaram, Bhaskar Krishnamachari
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
