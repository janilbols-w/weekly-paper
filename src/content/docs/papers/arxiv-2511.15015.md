---
title: "Dynamic Expert Quantization for Scalable Mixture-of-Experts Inference"
description: "Mixture-of-Experts (MoE) has become a practical architecture for scaling LLM capacity while keeping per-token compute modest, but deploying MoE models on a single, memory-limited GPU remains difficult because expert weights dominate the HBM footprint."
---

**评分：55/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2511.15015) · [PDF](https://arxiv.org/pdf/2511.15015)

## 一句话摘要

Mixture-of-Experts (MoE) has become a practical architecture for scaling LLM capacity while keeping per-token compute modest, but deploying MoE models on a single, memory-limited GPU remains difficult because expert weights dominate the HBM footprint.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) has become a practical architecture for scaling LLM capacity while keeping per-token compute modest, but deploying MoE models on a single, memory-limited GPU remains difficult because expert weights dominate the HBM footprint. Existing expert offloading and prefetching systems reduce the resident set, yet they often pay expert-loading costs on the critical path when activation becomes dense. Post-training quantization (PTQ) lowers the footprint without transfers, but prevailing pipelines fix expert bit-widths offline and assume routing remains stable, even though MoE expert utilization is heavy-tailed and the hot set can shift across workloads. We present DynaExq, a runtime-aware mixed-precision serving system that treats single-GPU MoE inference under a hard HBM envelope as an online, budget-constrained precision allocation problem. The key insight is to keep the experts that dominate runtime traffic resident at higher precision, while maintaining a low-precision fallback for the remaining experts, so the system can reduce transfer volume and avoid the waiting latency that limits offloading and prefetching under dense activation. DynaExq estimates long-horizon expert hotness from router traces, selects a per-layer high-precision resident set via a budget-feasible top-$n$ rule, and applies promotions and demotions asynchronously through stable expert handles so the forward pass always executes on a fully materialized expert version. Across Qwen3-MoE-30B/80B and six benchmarks, DynaExq improves accuracy over static PTQ on Qwen3-80B (73.09% to 77.57%) under comparable device-memory budgets and achieves up to 2.73x higher throughput than offloading/prefetch baselines at batch size 32.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 18 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kexin Chu, Dawei Xiang, Zixu Shen, Yiwei Yang, Zecheng Liu, Wei Zhang
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
