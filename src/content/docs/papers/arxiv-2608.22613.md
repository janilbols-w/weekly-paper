---
title: "NOVA: Technology-Architecture Co-Design of Near-Memory Processing for Attention-SSM-MoE Hybrid LLM Inference"
description: "The rapid evolution of hybrid large language models (LLMs), which interleave grouped-query-attention (GQA), state-space model (SSM), and Mixture-of-Experts (MoE) layers, introduces two fundamental challenges for near-memory processing (NMP) architectures."
---

**评分：49/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.22613) · [PDF](https://arxiv.org/pdf/2608.22613)

## 一句话摘要

The rapid evolution of hybrid large language models (LLMs), which interleave grouped-query-attention (GQA), state-space model (SSM), and Mixture-of-Experts (MoE) layers, introduces two fundamental challenges for near-memory processing (NMP) architectures.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid evolution of hybrid large language models (LLMs), which interleave grouped-query-attention (GQA), state-space model (SSM), and Mixture-of-Experts (MoE) layers, introduces two fundamental challenges for near-memory processing (NMP) architectures. First, the Technology Wall: the conventional 6F^2 DRAM cell is approaching its physical scaling limits at 10nm-class nodes, making it difficult to meet the memory capacity demands of MoE models with hundreds of experts. Second, the Architecture Wall: existing NMP designs target narrow arithmetic intensity (Op/B) ranges and cannot efficiently support the heterogeneous compute characteristics of hybrid LLMs, spanning memory-bound SSM layers, compute-intensive GQA layers, and large Op/B variations across experts. We propose NOVA, a technology-architecture co-designed NMP system that overcomes both walls. On the technology side, NOVA combines a 4F^2 vertical channel transistor (VCT) DRAM cell with a peri-over-cell (POC) structure to achieve approximately 2x memory density at iso-area over conventional 6F^2-based DRAM, enabling continued scaling into sub-10nm nodes. On the architecture side, NOVA repurposes the POC peripheral-die (peri-die) to host processing units, forming a 2-tier NMP architecture: Tier-1 (peri-die NMP) for low-to-mid Op/B operations, and Tier-2 (base-die NMP) for mid-to-high Op/B operations. Parallel execution across tiers supports diverse compute patterns for hybrid LLMs, maximizing inference performance. Evaluated on state-of-the-art hybrid and MoE LLMs including Nemotron3-Nano, Nemotron3-Super, Falcon-H1R, and Qwen3, NOVA achieves on average 4.5x higher throughput, 69.8% lower end-to-end latency, and 5x better energy efficiency over a GPU baseline, with only 3.9% area overhead and no loss in memory capacity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：In-Jun Jung, Jaeha Min, Joo-Young Kim
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
