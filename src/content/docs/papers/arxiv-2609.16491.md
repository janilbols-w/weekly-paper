---
title: "PipeSwift: Revisiting Pipeline Parallelism for Large-Scale Completion-Oriented Agentic LLM Serving"
description: "LLM agents execute long-horizon workflows where each model response determines the progress of subsequent tool interactions and environment transitions."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.16491) · [PDF](https://arxiv.org/pdf/2609.16491)

## 一句话摘要

LLM agents execute long-horizon workflows where each model response determines the progress of subsequent tool interactions and environment transitions.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents execute long-horizon workflows where each model response determines the progress of subsequent tool interactions and environment transitions. Unlike chatbot serving, where TTFT and TPOT SLO constraints are critical, agentic workloads are increasingly governed by completion time. This shift challenges existing LLM serving designs, which are optimized around token-level SLOs. We revisit scheduling and parallelism under this completion-oriented objective. Through systematic exploration, we show that job completion time (JCT) is governed by the balance between prefill and decode efficiency. Prefill-prioritized scheduling, while achieving the best TTFT and decode throughput, renders suboptimal JCT; across the scheduling-policy space, completion time varies by up to 1.40$\times$, with the optimum at neither extreme. We further show that pipeline parallelism (PP), previously overlooked due to its limited decode latency advantage, benefits JCT by providing a favorable balance of prefill--decode trade-off. Based on these insights, we build \name{}, an optimized open-source pipeline-parallel runtime that co-designs scheduling and parallelism through a JCT-aware scheduling layer and pipeline-integrated multi-token prediction. Evaluated on deterministic replays of real coding and web-search agent trajectories with two 360B+ MoE models on 64 H800 GPUs, \name{} reduces overall JCT by up to 1.45$\times$ over SGLang wide-EP, 2.33$\times$ over vLLM PP2, and 1.54$\times$ over today's state-of-the-art open-source PD-disaggregated deployment.

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

- 作者：Shiju Wang, Fei Ren, Fangcheng Fu, Zhanhong Tan, Kairui Li, Jingwei Cai, Kaisheng Ma
- 发布：2026-09-16；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
