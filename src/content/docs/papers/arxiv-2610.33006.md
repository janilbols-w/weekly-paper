---
title: "Linear-Time Context Compression with State-Space Encoding"
description: "Transformer-based large language models (LLMs) impose substantial computation and memory costs as context sizes increase, motivating methods that compress a context into a shorter representation before inference."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.33006) · [PDF](https://arxiv.org/pdf/2610.33006)

## 一句话摘要

Transformer-based large language models (LLMs) impose substantial computation and memory costs as context sizes increase, motivating methods that compress a context into a shorter representation before inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer-based large language models (LLMs) impose substantial computation and memory costs as context sizes increase, motivating methods that compress a context into a shorter representation before inference. Existing soft-prompt compression methods typically use the same Transformer backbone as used in the target model, where producing the compressed representation leads to significant latency overheads. This restricts them to the offline setting where context is compressed once and then reused across many queries. We propose the Boa Compressor, a plug-and-play online context compressor built on a Mamba state-space model (SSM) that encodes arbitrary-length context in a single linear-time pass, producing a representation on which we condition a frozen target LLM. The SSM is trained by distillation, matching the next-token logit distribution from the LLM ingesting the full context (as teacher) to the same LLM ingesting the compressed representation (as the student). At equal compression ratios, Boa matches or surpasses the performance of existing state-of-the-art offline compression baselines, while being an order of magnitude faster than Transformer-based implementations, thereby reducing end-to-end latency rather than adding compression time overhead. We demonstrate that Boa also scales well to longer contexts and to compression ratios as aggressive as 16x. By enabling effective compression that is cheap enough to run on every query at inference time, Boa becomes a practical and general tool for efficient long-context inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Marc Serra Ortega, Andrey Barsky, Carlos Boned Riera, Tom\'as Ockier, Dimosthenis Karatzas
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
