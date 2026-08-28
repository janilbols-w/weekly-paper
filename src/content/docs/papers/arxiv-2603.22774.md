---
title: "Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference"
description: "Large-scale machine learning workloads increasingly rely on multi-GPU systems, yet their performance is often limited by an overlooked component: the CPU."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2603.22774) · [PDF](https://arxiv.org/pdf/2603.22774)

## 一句话摘要

Large-scale machine learning workloads increasingly rely on multi-GPU systems, yet their performance is often limited by an overlooked component: the CPU.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large-scale machine learning workloads increasingly rely on multi-GPU systems, yet their performance is often limited by an overlooked component: the CPU. Through a detailed study of modern large language model (LLM) serving workloads, we find that multi-GPU performance often degrades not because GPUs are saturated, but because CPUs fail to keep them busy. Under limited CPU allocations, systems exhibit symptoms such as delayed kernel launch, stalled communication, and increased tokenization latency, leading to severe GPU underutilization even when ample GPU resources are available. The problem becomes more severe in agentic LLM serving, where long accumulated contexts increase CPU-side tokenization work while high prefix-cache reuse across multi-turn interactions reduces GPU-side prefill work. These bottlenecks persist even in serving stacks that employ process-level separation and modern GPU-side optimizations such as CUDA Graphs. Since CPU cores cost orders of magnitude less than GPUs, provisioning additional cores is a highly cost-effective mitigation. Under moderate serving load, we observe that CPU-starved configurations frequently time out, while providing adequate CPU resources restores responsiveness and reduces time-to-first-token (TTFT) latency by 1.47-7.11x across configurations, all without requiring additional GPUs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Euijun Chung, Yuxiao Jia, Aaron Jezghani, Hyesoon Kim
- 发布：2026-08-28；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
