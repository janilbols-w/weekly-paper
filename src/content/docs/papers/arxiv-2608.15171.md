---
title: "P-PAS: Prefill-Pressure Adaptive Scheduling for Long-Context LLM Serving"
description: "Long-context LLM applications such as retrieval-augmented generation (RAG) and agentic systems often process tens of thousands of input tokens to produce short outputs, making end-to-end request latency an important serving objective."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.15171) · [PDF](https://arxiv.org/pdf/2608.15171)

## 一句话摘要

Long-context LLM applications such as retrieval-augmented generation (RAG) and agentic systems often process tens of thousands of input tokens to produce short outputs, making end-to-end request latency an important serving objective.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM applications such as retrieval-augmented generation (RAG) and agentic systems often process tens of thousands of input tokens to produce short outputs, making end-to-end request latency an important serving objective. We show that the maximum number of batched tokens (MBT), which controls the token scheduling budget in vLLM, has a scheduling-pressure-dependent effect on latency. Larger token budgets can reduce latency under low scheduling pressure, while smaller budgets become preferable under higher pressure. Consequently, no single static MBT performs best across load regimes. We introduce Prefill-Pressure Adaptive Scheduling (P-PAS), a lightweight policy that dynamically adapts the scheduling budget based on concurrent prefill and decode state. P-PAS retains a large token budget under low pressure and constrains prefill work as pressure increases. Across models, workloads, and GPUs, P-PAS maintains low end-to-end latency across changing load regimes, avoiding the limitations of a fixed MBT. Kernel-level profiling shows that large prefill chunks can improve execution efficiency under low scheduling pressure, but that this advantage varies across model--hardware configurations. As scheduling pressure increases, smaller chunks can instead reduce interference with active decoding, explaining the observed load-dependent MBT sensitivity. Code and artifacts for reproducing our results are available at https://github.com/TimoSaemann/ppas-vllm .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Timo Sämann
- 发布：2026-08-15；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/TimoSaemann/ppas-vllm](https://github.com/TimoSaemann/ppas-vllm)
- 阅读深度：metadata
