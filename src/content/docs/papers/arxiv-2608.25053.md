---
title: "Hydra: Phase-Aware Workload Characterization of LLM Inference across Edge SoC Generations, Backends, and Quantization Levels"
description: "Edge LLM deployment is shaped by more than model size and precision: inference backend, hardware platform, memory traffic, and power management all affect latency and efficiency."
---

**评分：55/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2608.25053) · [PDF](https://arxiv.org/pdf/2608.25053)

## 一句话摘要

Edge LLM deployment is shaped by more than model size and precision: inference backend, hardware platform, memory traffic, and power management all affect latency and efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge LLM deployment is shaped by more than model size and precision: inference backend, hardware platform, memory traffic, and power management all affect latency and efficiency. We present Hydra, a common-schema, phase-aware workload characterization framework for LLM inference on edge SoCs. Hydra instruments HuggingFace Transformers and llama.cpp with a shared per-prompt timing schema and fuses those records with hardware telemetry, enabling a multi-dimensional characterization of performance, system-resource utilization, and efficiency across prefill and decode phases. Using Hydra, we evaluate three consecutive edge System-on-Chip (SoC) generations (AGX Xavier, AGX Orin, and AGX Thor), 13 instruction-tuned LLMs from seven families, five execution formats, and consider input/output-length sensitivity. The resulting artifact contains roughly 107K per-prompt records and is publicly released with Hydra. Our analysis shows that aggregate latency alone hides key deployment effects: backend structure changes where latency is introduced, quantization reduces memory traffic and energy but does not predict power monotonically, and SoC generation changes how utilization and efficiency should be interpreted. By connecting phase-level timing with system-resource utilization and efficiency metrics, Hydra enables reproducible, phase-aware characterization of edge LLM inference. Hydra's source code and the collected per-prompt trace corpus are available open-source at: https://github.com/amirtaherin/hydra

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 9 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: workload characterization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Amir Taherin, Sana Taghipour Anvari, Charles Amante, Yixiao Chen, Ruben Noroian, Zlatan Feric, Nicolas Bohm Agostini, Pu Zhao, Jos\'e Cano, Bin Ren, Yanzhi Wang, David Kaeli
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/amirtaherin/hydra](https://github.com/amirtaherin/hydra)
- 阅读深度：metadata
