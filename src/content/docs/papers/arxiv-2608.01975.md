---
title: "TELLER: Non-intrusive Cross-Layer Root-Cause Analysis for LLM Inference"
description: "Large language model (LLM) inference has evolved from an offline workload into a continuously operated software service, yet root-cause analysis remains difficult because a single request spans the inference engine, Python/C++ backend, host CUDA APIs, GPU kernels, and distributed communication."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.01975) · [PDF](https://arxiv.org/pdf/2608.01975)

## 一句话摘要

Large language model (LLM) inference has evolved from an offline workload into a continuously operated software service, yet root-cause analysis remains difficult because a single request spans the inference engine, Python/C++ backend, host CUDA APIs, GPU kernels, and distributed communication.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference has evolved from an offline workload into a continuously operated software service, yet root-cause analysis remains difficult because a single request spans the inference engine, Python/C++ backend, host CUDA APIs, GPU kernels, and distributed communication. Existing profilers expose raw timelines, while log-based diagnosis often misses cross-layer execution semantics and request-level structure. We present TELLER, a non-intrusive Trace- and Log-aware LLM inference Root-cause analysis framework. TELLER first collects NVTX/CUPTI traces and service logs without modifying model binaries, then reconstructs per-request call-chain trees and aligns log lines with the corresponding execution steps. We introduce a dependency-aware causal-context slice that preserves parent-child structure, temporal order, and communication relations, and a Trace Pair Encoding (TPE) tokenizer that compresses such slices into compact structural token sequences with parent, depth, and duration attributes. On top of these representations, TELLER combines numeric candidate localization with a multimodal root-cause model that jointly predicts abnormal steps, localizes suspicious operators, and generates natural-language explanations. Experiments on multi-node GPU inference workloads show a clear compression-accuracy trade-off: a moderate TPE vocabulary reduces per-step trace length by more than 80% while achieving the best overall performance on both horizontal (cross-node communication) and vertical (within-node execution stack) views, whereas more aggressive compression substantially degrades diagnosis quality. Further analyses under low-fault priors, strengthened baselines, modality ablations, explanation-quality checks, and tracing overhead show that TELLER provides a practical triage and evidence-localization substrate for LLM inference RCA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruilin Xu, Junyi Li, Pengfei Chen, Zongxuan Xie
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
