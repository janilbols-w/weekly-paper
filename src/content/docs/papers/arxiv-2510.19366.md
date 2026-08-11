---
title: "MoE-Prism: Disentangling Monolithic Experts for Elastic MoE Services via Model-System Co-Designs"
description: "Mixture-of-Experts (MoE) scales model capacity through sparse activation, and is becoming an important architecture for large language models (LLMs)."
---

**评分：40/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2510.19366) · [PDF](https://arxiv.org/pdf/2510.19366)

## 一句话摘要

Mixture-of-Experts (MoE) scales model capacity through sparse activation, and is becoming an important architecture for large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) scales model capacity through sparse activation, and is becoming an important architecture for large language models (LLMs). However, existing MoE serving systems typically execute all requests under a fixed routing configuration, limiting their ability to exploit heterogeneous computation requirements across requests. Routing top-$k$, which determines the number of routed experts activated per token, directly controls routed-expert computation and provides a natural mechanism for request-level compute elasticity. Realizing this capability, however, requires finer-grained routing units and efficient runtime execution for heterogeneous routing budgets. We present \textsc{MoE-Prism}, a model and system support framework for request-level compute elasticity in MoE serving. \textsc{MoE-Prism}decomposes monolithic experts into fine-grained sub-experts to expose denser routing operating points and provides a $k$-aware serving runtime that effectively serves heterogeneous routing budgets under both throughput-oriented and latency-sensitive workloads. We implement \textsc{MoE-Prism} on top of vLLM and evaluate it on three representative MoE models. \textsc{MoE-Prism} expands the number of available routing operating points by $4\times$, improves offline inference throughput by up to 33.9\%, and reduces online serving TTFT under heterogeneous workloads. These results demonstrate practical elastic MoE serving with request-level routing targets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: serving runtime
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xinfeng Xia, Xiaofeng Hou, Jiacheng Liu, Wenfeng Wang, Mingxuan Zhang, Peng Tang, Chao Li, Minyi Guo
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
