---
title: "FOREST: Coordinating Tree-based HBF, RRAM, and HBM for Efficient Speculative LLM Inference"
description: "Speculative decoding (SD) accelerates large language model (LLM) inference by combining lightweight drafting with parallel target-model verification."
---

**评分：56/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2611.27701) · [PDF](https://arxiv.org/pdf/2611.27701)

## 一句话摘要

Speculative decoding (SD) accelerates large language model (LLM) inference by combining lightweight drafting with parallel target-model verification.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding (SD) accelerates large language model (LLM) inference by combining lightweight drafting with parallel target-model verification. However, its stages impose distinct resource demands: target verification requires high-throughput access to large weight sets, sequential drafting executes a compact model under tight latency constraints, and long-context attention processes growing key-value (KV) caches. Conventional GPU-centric SD systems serve these workloads through shared HBM-centric memory and general-purpose compute, creating mismatches in capacity, bandwidth, and computation. These mismatches constrain deployable model-context configurations and limit the efficiency of bandwidth-bound and latency-sensitive operations. We propose FOREST, a heterogeneous memory-centric architecture coordinating HBF, 3D-stacked RRAM, and HBM memory-compute trees for efficient SD. It features: (1) compute-aligned 3D RRAM, combining ultra-wide, low-frequency reads with clock-decoupled interfaces and overlapped SRAM-DCIM weight refills for latency-sensitive drafting; (2) cross-tree numerical co-design, moving block-scaled Q/K/V preprocessing to HBF and RRAM root plates and enabling block-floating-point (BFP) attention with pipelined softmax reduction in the HBM tree; and (3) HBF-aware SD design-space exploration, revealing how bandwidth-compute provisioning and model scale determine performance, energy, and cost trade-offs. Evaluated across six SD configurations spanning 32B-405B target models, FOREST achieves up to 5.5x end-to-end speedup, 11.46x higher decode throughput, and 16.5x higher decode energy efficiency over NVIDIA A800 GPU-based SD baselines. Under a modeled total cost of ownership, FOREST delivers up to 6.73x higher token-generation cost efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 20 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency, total cost of ownership
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hao Ding, Zheng Shi, Dongxue Zhao, Huiying Bian, Meng Li, Xu Zheng, Kun Wang, Nanjian Wu, Jie Chen, Yimao Cai
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
