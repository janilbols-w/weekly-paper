---
title: "Enabling Spatially Fine-Grained DVFS in Neural Processing Units for Energy-Efficient LLM Serving"
description: "As neural processing units (NPUs) evolve rapidly to accommodate the ever-increasing compute demand of large language models (LLMs), their power consumption is becoming a limiting factor."
---

**评分：40/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2607.16473) · [PDF](https://arxiv.org/pdf/2607.16473)

## 一句话摘要

As neural processing units (NPUs) evolve rapidly to accommodate the ever-increasing compute demand of large language models (LLMs), their power consumption is becoming a limiting factor.

## 为什么值得关注

待编辑增强。

## 摘要原文

As neural processing units (NPUs) evolve rapidly to accommodate the ever-increasing compute demand of large language models (LLMs), their power consumption is becoming a limiting factor. Our study shows that using dynamic voltage and frequency scaling (DVFS) to exploit the service-level objective (SLO) slacks is a promising way to improve NPU energy efficiency for LLM services. And as tensor operators in LLMs exhibit diverse bottlenecks across NPU components, it is desirable to configure the frequency separately for each component to maximize their energy efficiency. In this paper, we develop eNPU that enables hardware and software support for spatially fine-grained, component-level DVFS on NPUs. eNPU refactors the NPU core pipeline to partition components into separate V/$f$ domains. It introduces lightweight cross-domain communication mechanisms to mitigate synchronization overheads across components, and extends the NPU ISA for sub-$\mu$s DVFS control. eNPU uses a compiler-driven two-level greedy search to co-optimize instruction scheduling and per-component V/$f$ selection under SLO constraints. We implement eNPU's pipeline design on an open-source NPU core to verify its functionality and evaluate the energy savings with a production-level NPU simulator with various LLMs using production traces. eNPU reduces energy consumption of LLM services by 25.8%--35.2% with 3.45% area overhead on a TPUv4 chip, while preserving strict SLO guarantees.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuqi Xue, Jerry Wu, Corey Yu, Jian Huang
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
