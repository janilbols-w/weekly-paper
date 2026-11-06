---
title: "UMLoad: Fast On-Demand Model Loading on Unified Memory Architecture"
description: "On-demand model loading dominates response latency for interactive on-device AI, yet unified memory architectures (UMAs), now common on edge devices, should make it cheap by placing weights in memory the GPU already sees."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.04253) · [PDF](https://arxiv.org/pdf/2611.04253)

## 一句话摘要

On-demand model loading dominates response latency for interactive on-device AI, yet unified memory architectures (UMAs), now common on edge devices, should make it cheap by placing weights in memory the GPU already sees.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-demand model loading dominates response latency for interactive on-device AI, yet unified memory architectures (UMAs), now common on edge devices, should make it cheap by placing weights in memory the GPU already sees. However, frameworks still use the loading flow built for discrete GPUs, leaving significant inefficiencies. This paper presents UMLoad, a system-level model-loading accelerator that decouples a framework's logical allocations from their physical page backing. UMLoad uses on-demand reconstruction to eliminate the weight copy while preserving copy independence, and GPU-assisted page zeroing to accelerate runtime allocation while preserving its security guarantee. Implemented on Intel, AMD, and NVIDIA UMA platforms and evaluated with llama$.$cpp, PyTorch, and vLLM across six models, UMLoad reduces average loading time by 36.6%-71.9% over vanilla and 19.9%-62.7% over pipelined loaders, and cuts mean LLM-routing time to first token (TTFT) by 51.3%-59.3% and model-backed tool completion latency by 10.2%-31.6%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: unified memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zimeng Wang, Jinrong Yang, Rong Chen
- 发布：2026-11-04；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
