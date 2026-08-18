---
title: "Anatomy of a Quantized Agent: VRAM Stability and Forecasting in Code-Synthesis Agentic Workloads"
description: "Analytical models of peak VRAM consumption for LLM inference decompose memory into weight-storage, KV-cache, and activation terms parameterized by step count, tool invocations, and context expansion."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.15117) · [PDF](https://arxiv.org/pdf/2608.15117)

## 一句话摘要

Analytical models of peak VRAM consumption for LLM inference decompose memory into weight-storage, KV-cache, and activation terms parameterized by step count, tool invocations, and context expansion.

## 为什么值得关注

待编辑增强。

## 摘要原文

Analytical models of peak VRAM consumption for LLM inference decompose memory into weight-storage, KV-cache, and activation terms parameterized by step count, tool invocations, and context expansion. We evaluate this decomposition empirically within a strictly scoped measurement study: a LangGraph-based CUDA-kernel-synthesis agent (AgentK), a 4-bit quantization family (Q4 K M), a single NVIDIA H100 GPU, and four LLM backbones across 1,920 trajectories. Focusing on peak-memory forecasting behavior, we report two primary observations. First, closed-form analytical models achieve competitive accuracy when provided with two empirical constants: loaded-weight VRAM and a fixed activation-memory overhead. Supplied with live GPU readings and ground-truth trajectory parameters, the closed-form model matches or outperforms the best learned baseline on three of the four backbones (test MAPE 2.2-4.4% vs. 3.4-6.5%, p = 0.76). The exception is the smallest backbone (Phi-4-mini), where minimal VRAM variance (CV 0.3%) causes dynamic modeling to underperform simple regression. Second, compile success strictly bifurcates by backbone capacity (from 5.7% for Phi-4-mini to 62.0% for Qwen2.5-Coder-14B), demonstrating that functional code synthesis remains constrained by intrinsic LLM capabilities rather than available memory. Furthermore, because overall peak-memory variance is remarkably low across all backbones (CV 0.3-9.4%), learned prompt-feature regression offers statistically insignificant improvements over a constant-mean baseline. Consequently, we find no justification for deploying complex predictive VRAM models in highly quantized, weight-dominated regimes. We release the evaluated corpus and anonymized framework to support replication.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anubhab Banerjee
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
