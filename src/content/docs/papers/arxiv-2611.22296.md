---
title: "SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding"
description: "Speculative decoding (SD) accelerates large language model (LLM) inference, but its optimal configuration depends jointly on workload characteristics, GPU hardware, and available memory."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.22296) · [PDF](https://arxiv.org/pdf/2611.22296)

## 一句话摘要

Speculative decoding (SD) accelerates large language model (LLM) inference, but its optimal configuration depends jointly on workload characteristics, GPU hardware, and available memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding (SD) accelerates large language model (LLM) inference, but its optimal configuration depends jointly on workload characteristics, GPU hardware, and available memory. For example, on the RTX~5090, the state-of-the-art speculative drafter DFlash achieves $3.50\times$ the throughput of autoregressive (AR) decoding at low concurrency, but only $0.76\times$ at high concurrency with short outputs. We present SpecSearch, a hardware-aware search engine that jointly optimizes decoding strategy, draft length, and precision across workload--GPU pairs. Its analytical cost model captures memory and compute constraints to identify feasible configurations and narrow the search space for throughput optimization. Guided by this model, calibration measurements are collected from multiple GPUs. Using the measurements, a Jev-based predictor learns to select high-throughput decoding configurations on held-out GPUs without requiring deployment-GPU calibration. The predictor is parameter-efficiently trained on calibration data, while adapting a frozen Qwen3-4B using LoRA adapters and a linear correction layer. Across NVIDIA RTX~5090, H100, L40 and AMD MI300X GPUs, SpecSearch with full calibration achieves an average of $2.01\times$ the throughput of AR and $1.36\times$ the throughput of SD, both served by vLLM. The proposed Jev-based predictor closely matches this search performance with $1.30\times$ throughput improvement over SD with vLLM, while eliminating the need for held-out GPU calibration. Additionally, it retains $97.36\%$ of the throughput achieved by SpecSearch that utilizes full calibration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Selin Yildirim, Ali Zeyrek, Deming Chen
- 发布：2026-11-17；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
