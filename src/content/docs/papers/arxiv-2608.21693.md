---
title: "Benchmarking Composable Compression Techniques in Mixture-of-Experts LLMs"
description: "Mixture-of-Experts (MoE) LLMs scale model capacity efficiently through sparse activation, but their large expert parameter footprint, routing imbalance, and long-context KV-cache growth make deployment difficult on commodity hardware."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.21693) · [PDF](https://arxiv.org/pdf/2608.21693)

## 一句话摘要

Mixture-of-Experts (MoE) LLMs scale model capacity efficiently through sparse activation, but their large expert parameter footprint, routing imbalance, and long-context KV-cache growth make deployment difficult on commodity hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) LLMs scale model capacity efficiently through sparse activation, but their large expert parameter footprint, routing imbalance, and long-context KV-cache growth make deployment difficult on commodity hardware. Practical deployment often requires stacking multiple compression techniques: expert pruning removes redundant experts, weight quantization lowers model memory footprint, and KV-cache compression reduces long-context memory pressure. However, these techniques are typically evaluated in isolation, leaving open how they interact when applied together in realistic deployment pipelines. In this work, we present MoEXBench, a systematic benchmark for evaluating composable MoE compression as an end-to-end deployment workflow. MoEXBench studies 10 MoE models ranging from 30B to 235B total parameters across standard-attention, hybrid linear-attention, and sliding window attention architectures. It evaluates 20%-50% expert pruning rates, 1 to 16 bit weight-quantization schemes, and multiple KV-cache precision settings, applied both individually and in combination. MoEXBench introduces an eight-module evaluation suite that jointly measures composable-compression quality, workload and architecture robustness, pruning/quantization/KV cache sensitivity, and deployment efficiency on commodity hardware. Our results reveal non-trivial interactions among compression methods: composable compression cannot be predicted from standalone techniques, compression rate alone does not reliably predict quality loss or runtime gain, expert pruning is the dominant degradation source, and average quality can hide workload and architecture-specific failures. By releasing normalized module scores, compressed artifacts, and reproducible scripts, MoEXBench enables practical accuracy-memory-latency comparison across MoE families and hardware backends.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 4 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Afsara Benazir, Chen Chen, Rongxiao Qu, Jiabo Huang, Jingtao Li, Lingjuan Lyu
- 发布：2026-08-22；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
