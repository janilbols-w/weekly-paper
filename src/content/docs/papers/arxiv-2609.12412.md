---
title: "HoliBench: A Cross-Platform Benchmarking and Deployment Toolkit for Foundation Models in CPS-IoT Applications"
description: "Foundation models, including large language models, vision-language models, and time-series foundation models, are increasingly deployed on embedded and edge platforms for CPS and IoT applications, where energy, latency, and memory are as critical as task accuracy."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.12412) · [PDF](https://arxiv.org/pdf/2609.12412)

## 一句话摘要

Foundation models, including large language models, vision-language models, and time-series foundation models, are increasingly deployed on embedded and edge platforms for CPS and IoT applications, where energy, latency, and memory are as critical as task accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Foundation models, including large language models, vision-language models, and time-series foundation models, are increasingly deployed on embedded and edge platforms for CPS and IoT applications, where energy, latency, and memory are as critical as task accuracy. Existing benchmarking tools evaluate model capability in isolation, reporting accuracy assuming sufficient compute, while hardware profiling tools remain platform-specific and mutually incompatible. As a result, users lack a unified workflow for making deployment decisions across heterogeneous devices. We present HoliBench, a modular benchmarking and deployment toolkit that jointly characterizes accuracy, latency, and energy across platforms from single-board computers to GPU servers. Its platform abstraction layer calibrates cross-device measurement, and the toolkit supports multiple model modalities, inference engines, concurrencies, and existing evaluation harnesses. An interactive interface exposes constraint-aware configuration selection over a design space that is profiled once and reused across studies. Using HoliBench, we characterize 20 models across 7 device types, 3 quantization levels, 8 inference backends, and over 30 tasks, surfacing tradeoffs that existing tools miss: quantization reduces latency only on hardware with low-precision support, accuracy gains show diminishing returns relative to energy, and for autoregressive workloads, average inference power is approximately constant across output lengths. We further find that single-model profiles compose under sequential co-resident execution. In a multi-model CPS deployment, standalone profiles predict combined-pipeline latency and power within 1.2% and 2.5%, enabling deployment exploration without exhaustively profiling every pipeline configuration. We release HoliBench as open-source infrastructure for deployment-aware evaluation of foundation models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Inesh Chakrabarti, Zejun Xiong, Pragya Sharma, Mani Srivastava
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
