---
title: "ServeTwin: A Benchmark-Validated Simulator for Distributed LLM Architecture Exploration"
description: "Evaluating distributed LLM serving designs on physical clusters is costly."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.02732) · [PDF](https://arxiv.org/pdf/2610.02732)

## 一句话摘要

Evaluating distributed LLM serving designs on physical clusters is costly.

## 为什么值得关注

待编辑增强。

## 摘要原文

Evaluating distributed LLM serving designs on physical clusters is costly. Yet existing simulators provide only subsets of the capabilities needed for realistic design exploration: stateful closed-loop execution, timing prediction without profiling target hardware, and direct execution of unmodified serving benchmarks. We present ServeTwin, a closed-loop simulator that couples specification-driven analytical timing with a stateful serving loop. This coupling captures feedback among request completion, scheduling, queue state, and KV-cache evolution, including prefill-decode disaggregation and multi-turn agent workloads. ServeTwin avoids target-hardware operator profiling through iSTAGE, an analytical trace generator that derives per-iteration traces from model and engine specifications while representing ragged batches and discrete engine mechanisms such as CUDA-graph batch padding. It further decomposes execution time into component-owned throughput, scheduler, and runtime costs. This ownership lets unaffected parameters transfer across platforms and confines recalibration to changed hardware or software components. ServeTwin implements a vLLM-compatible interface and runs unmodified serving benchmarks. Against real deployments, it reproduces InferenceX's steady-state throughput-interactivity frontier with a 3.6% mean error and predicts LMBenchmark's multi-turn performance with a 9.9% error while tracking KV-cache evolution. Pre-silicon sweeps reveal that the preferred HBM bandwidth-capacity tradeoff reverses across workload states and that increasing concurrency shifts the bottleneck from memory bandwidth to scheduler and runtime overheads. Together, these capabilities enable practical exploration of distributed LLM serving systems before target hardware is available.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sungjoon Park, Changue Jung, Kyungno Joo, Mincheol Kang, Jaehyung Ahn, Sehwan Lee, Sangjoon Kim
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
