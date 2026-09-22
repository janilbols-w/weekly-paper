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

LLM agents execute long-horizon workflows where each model response determines the progress of subsequent tool interactions and environment transitions. Unlike chatbot serving, where TTFT and TPOT SLO constraints are critical, agentic workloads are completion-oriented and increasingly governed by job completion time (JCT). This shift challenges existing LLM serving designs optimized around token SLOs. Through a systematic exploration of scheduling and parallelism, we uncover a previously overlooked principle for agent serving: JCT is governed by the balance between prefill and decode efficiency. A prefill-prioritized scheduling policy achieves the best TTFT and the highest decode throughput, yet fails to attain the lowest JCT. This principle further reshapes the parallelism landscape: we show that pipeline parallelism (PP), long overlooked because it offers little decode-latency advantage, can reduce JCT by providing a more favorable balance between prefill and decode efficiency. Based on these insights, we build PipeSwift, an optimized open-source pipeline-parallel runtime integrated with a tailored micro-batch partitioning strategy co-designed with schedule considering the above trade-off, and pipeline-integrated multi-token prediction. Evaluated on real coding and web-search agent trajectories with two 360B+ MoE models on 64 H800 GPUs, PipeSwift reduces overall JCT by up to 1.45$\times$ over SGLang wide-EP, 2.33$\times$ over vLLM PP2, and 1.54$\times$ over today's state-of-the-art open-source PD-disaggregated deployment.

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
- 发布：2026-09-16；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
