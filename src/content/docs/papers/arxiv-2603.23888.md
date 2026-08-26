---
title: "SiftMoE: Similarity-Aware Energy-Efficient Expert Selection for Wireless Distributed MoE Inference"
description: "Mixture-of-Experts (MoE) architectures leverage sparse activation to enhance the scalability of large language models (LLMs), making them suitable for deployment in resource-constrained edge networks."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2603.23888) · [PDF](https://arxiv.org/pdf/2603.23888)

## 一句话摘要

Mixture-of-Experts (MoE) architectures leverage sparse activation to enhance the scalability of large language models (LLMs), making them suitable for deployment in resource-constrained edge networks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) architectures leverage sparse activation to enhance the scalability of large language models (LLMs), making them suitable for deployment in resource-constrained edge networks. However, the sheer number of experts often exceeds the memory capacity of individual edge nodes, necessitating wireless distributed MoE (WIDE) inference where experts are spread across multiple edge nodes. In this context, expert selection directly affects communication costs. Motivated by the similarity of experts, we propose SiftMoE, which judiciously selects or skips experts to strike a tradeoff between communication costs and inference accuracy. Specifically, we first establish theoretical bounds on the accuracy degradation resulting from expert replacement or skipping. Based on the bounds, we formulate an energy minimization problem for expert selection in WIDE inference subject to latency and accuracy constraints. In particular, for slow-fading channels, we derive optimal expert selection policies for both single-token decoding and multi-token prefilling. For fast-fading channels, we further extend our scheme to cope with rapidly varying channel conditions. Simulation results demonstrate that SiftMoE significantly reduces energy consumption while maintaining inference accuracy compared with conventional Top-K routing in WIDE systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: moe inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qian Chen, Xianhao Chen, Kaibin Huang
- 发布：2026-08-26；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
