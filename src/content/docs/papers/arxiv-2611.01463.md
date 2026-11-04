---
title: "DIMWIT: Directly Invoking Models Without Intensive Tuning"
description: "Resource managers typically encode what to do in a task-specific policy---a heuristic, an optimization procedure, or a model trained for the task---that must be developed before use and may need revision as the workload or system changes."
---

**评分：41/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2611.01463) · [PDF](https://arxiv.org/pdf/2611.01463)

## 一句话摘要

Resource managers typically encode what to do in a task-specific policy---a heuristic, an optimization procedure, or a model trained for the task---that must be developed before use and may need revision as the workload or system changes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Resource managers typically encode what to do in a task-specific policy---a heuristic, an optimization procedure, or a model trained for the task---that must be developed before use and may need revision as the workload or system changes. We propose bypassing policy development and instead asking pretrained models to make resource-management decisions directly, given the current system state, desired outcome, and available choices. We evaluate this approach on microservice autoscaling, DRAM sizing, and video encoding, using a frontier LLM and two small decision models. On two microservice applications, a small decision model meets latency targets while using within 10% of the replicas allocated by policy-based autoscalers and within 13% of the frontier LLM. In DRAM sizing, a small decision model reduces DRAM usage by up to 27.5% relative to static provisioning while maintaining at least 95% of baseline performance. In video encoding, it completes encodes up to 4.3$\times$ faster than the frontier LLM, with an imperceptible 1.1-point decrease in Video Multi-Method Assessment Fusion (VMAF), a metric of perceptual video quality. Making individual resource-management decisions may be considerably simpler than developing a general strategy for making them.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: autoscaling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saarth Deshpande, Neeraja J. Yadwadkar, Venkat Arun
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
