---
title: "Ripple: Deadline-Aware CPU-GPU Sharing for Embodied Inference"
description: "Unified-memory edge devices increasingly run LLM/VLM inference alongside time-critical CPU tasks for perception and control."
---

**评分：42/100** · AI 基础设施 > 集群与资源系统 > GPU 调度与虚拟化

[论文原文](https://arxiv.org/abs/2611.01067) · [PDF](https://arxiv.org/pdf/2611.01067)

## 一句话摘要

Unified-memory edge devices increasingly run LLM/VLM inference alongside time-critical CPU tasks for perception and control.

## 为什么值得关注

待编辑增强。

## 摘要原文

Unified-memory edge devices increasingly run LLM/VLM inference alongside time-critical CPU tasks for perception and control. GPU memory traffic can overwhelm these tasks, yet platforms such as DGX Spark expose neither bandwidth counters nor direct bandwidth regulation. We present Ripple, a CPU-GPU co-scheduler that combines model-derived GPU memory volumes with CPU completion feedback to regulate interference. Ripple divides inference into pausable, layer-based units and translates each CPU job's deadline slack into a GPU-byte budget, admitting work within the budgets of all overlapping jobs. Online updates track changing interference, while deadline-aware pacing and judicious SM footprint narrowing preserve inference progress. Implemented with SGLang engine hooks and a central scheduler, we evaluate Ripple on DGX Spark with four robotic CPU task mixes and LLM/VLM inference. It is the only evaluated approach that consistently meets the 2% CPU deadline-miss target and VLM deadlines across the tested deadline settings while retaining best-effort LLM throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu sharing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiadong Zhang, Xiaosong Ma
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
