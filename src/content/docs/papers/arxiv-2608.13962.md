---
title: "MoE Expert Execution in Disaggregated LLM Serving with a High-Bandwidth ReRAM Near-Memory Architecture"
description: "Attention-FFN disaggregation maps LLM modules to specialized pools, creating an opening to keep Mixture-of-Experts (MoE) weights resident in a high-bandwidth FFN pool."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.13962) · [PDF](https://arxiv.org/pdf/2608.13962)

## 一句话摘要

Attention-FFN disaggregation maps LLM modules to specialized pools, creating an opening to keep Mixture-of-Experts (MoE) weights resident in a high-bandwidth FFN pool.

## 为什么值得关注

待编辑增强。

## 摘要原文

Attention-FFN disaggregation maps LLM modules to specialized pools, creating an opening to keep Mixture-of-Experts (MoE) weights resident in a high-bandwidth FFN pool. Decode SLOs, however, cap the run-batch while sparse routing expands the activated-expert union, so weight traffic amortizes poorly and routing skew idles cold-expert resources. The FFN pool must therefore deliver weight-read bandwidth density under sparse unions and recover occupancy under skew without a global sharing fabric. We present a ReRAM near-memory architecture that keeps expert weights resident behind high-bandwidth local reads. The design factors actual MFU into ideal MFU and occupancy, recovers occupancy with bounded core-local multicast pooling, coactivation-aware placement, and load-aware fetch, and sizes each communication level from induced demand. A measured + modeled study on Qwen3.5-35B-A3B, Qwen3.5-397B-A17B, and GLM-5.2 shows that side-4 pooling raises occupancy from 0.328 to 0.519 and, at iso-peak compute, lowers per-token FFN-pool latency by 9.5x versus H20 with 20x lower weight-movement energy; an H20-attention + ReRAM-FFN system reduces decode TPOT by 1.25-4.0x, 2.4-10.3x, and 2.5-10.4x versus a homogeneous H20 pool.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kunming Shao, Ming Zeng, Xin Yuan, Binbin Liao, Yangming Zhang, Wei Wang, Tim Kwang-Ting Cheng, Chi-Ying Tsui
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
