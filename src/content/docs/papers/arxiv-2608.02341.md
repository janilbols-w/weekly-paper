---
title: "Broadcast Rate Limits in Wi-Fi: A Forgotten Bottleneck for Collaborative Edge LLM Inference"
description: "LLM deployment is migrating from data centers to edge devices, where Mixture-of-Experts (MoE) models offer a promising path: sparse expert activation allows the model to be spread across multiple low-cost edge nodes."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2608.02341) · [PDF](https://arxiv.org/pdf/2608.02341)

## 一句话摘要

LLM deployment is migrating from data centers to edge devices, where Mixture-of-Experts (MoE) models offer a promising path: sparse expert activation allows the model to be spread across multiple low-cost edge nodes.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM deployment is migrating from data centers to edge devices, where Mixture-of-Experts (MoE) models offer a promising path: sparse expert activation allows the model to be spread across multiple low-cost edge nodes. Distributed MoE inference repeatedly dispatches embeddings from one main node to many workers - a one-to-many pattern poorly served by the sequential unicasts of mainstream stacks (NCCL, TCP), yet naturally matched by UDP broadcast. We propose a UDP broadcast method for collaborative edge MoE inference, augmented with timeout-driven retransmission exploiting near deterministic latency in distributed MoE for reliability and unordered result gathering for robustness to expert mispredictions, yielding a consistent 1.4x speedup over NCCL and TCP on a wired 8-node cluster. In wireless settings, however, we uncover a deeper, long-forgotten bottleneck: IEEE 802.11 caps broadcast rates at 54 Mbps regardless of physical-layer capacity - a legacy policy built for sparse control traffic, not edge AI. NS-3 simulations at distances 1m, 2m and 5m show that the optimal rates are much higher (64x, 43x, and 32x, respectively) than the 54 Mbps cap applied in standard. Thus, we argue that broadcast is no longer a control-plane relic: it is time for Wi-Fi standards to treat it as a high-throughput data-plane citizen.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: moe inference
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Liujianfu Wang, Yuyang Du, Shiqi Xu, Soung Chang Liew
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
