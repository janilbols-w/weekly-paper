---
title: "Optimizing AI Inference Across the Deployment Stack"
description: "AI deployment performance is shaped not by model architecture alone, but by interactions among compression, compiler transformations, and serving policies."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.10550) · [PDF](https://arxiv.org/pdf/2609.10550)

## 一句话摘要

AI deployment performance is shaped not by model architecture alone, but by interactions among compression, compiler transformations, and serving policies.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI deployment performance is shaped not by model architecture alone, but by interactions among compression, compiler transformations, and serving policies. Published benchmarks often report latency and throughput under incomparable conditions, limiting their use for deployment decisions. This paper presents a unified analytical treatment of inference optimization across the deployment stack. We introduce a three-layer taxonomy covering model-level techniques such as quantization, pruning, and distillation; compiler transformations such as graph fusion, layout optimization, and kernel autotuning; and system policies such as dynamic batching, admission control, and memory tiering. We formulate deployment as a constrained multi-objective optimization problem over accuracy, latency, throughput, memory footprint, and energy, and analyze a deployment-ranking functional with Pareto monotonicity and scale invariance. Roofline models show how memory-bandwidth hierarchies bound performance across precision regimes, while queuing models explain how service-time changes amplify response time under load. To improve comparability, we propose an evidence protocol that separates measured, derived, and analytical claims; limits numerical comparison to within-paper results; and requires reporting of hardware, software versions, batch semantics, and thermal state. We synthesize evidence from edge platforms, including Jetson AGX Orin and five inference frameworks; data center GPUs, including A100 and H100 with three LLM serving engines; and quantization studies across the Llama-3.1 family. The synthesis shows that deployment outcomes are governed by cross-layer interactions that no single-layer analysis can predict. We conclude with a constraint-aware selection procedure and open problems in compiler-serving co-optimization, cross-hardware performance prediction, and standardized energy reporting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tejinder Singh, John Pflueger, Jeebak Mitra, Robert Lincourt, Mitchell Markow, Bhavesh A. Patel
- 发布：2026-09-11；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
