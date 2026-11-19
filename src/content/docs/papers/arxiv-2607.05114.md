---
title: "Localized LoRA-MoE: Mixture of Low-Rank Experts With Adaptive Routing"
description: "Parameter-efficient fine-tuning (PEFT) methods such as LoRA adapt large models through a single low-rank update."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2607.05114) · [PDF](https://arxiv.org/pdf/2607.05114)

## 一句话摘要

Parameter-efficient fine-tuning (PEFT) methods such as LoRA adapt large models through a single low-rank update.

## 为什么值得关注

待编辑增强。

## 摘要原文

Parameter-efficient fine-tuning (PEFT) methods such as LoRA adapt large models through a single low-rank update. Such updates are susceptible to gradient interference: when a training stream interleaves multiple operational contexts, conflicting updates to shared adapter weights collapse the adapter into an unspecialized average. While recent methods introduce block-wise isolation to remedy this issue, their topologies are static and cannot adapt to context switching or localized sensor degradation. In this work, we introduce Localized LoRA-MoE, a framework that combines localized spatial blocking with context-conditioned expert routing. We propose and evaluate two architectural variants: Block-Wise LoRA-MoE (centralized routing), which modulates the entire structural grid through a single context-conditioned gate, and Cell-Wise LoRA-MoE (decentralized routing), which assigns an independent gate to every coordinate cell of the matrix grid. Across three structured transformation benchmarks--a high-dimensional SVD matrix simulation, context-switched transformations over real tabular data, and spatial reconstruction under simulated sensor occlusion--both variants outperform static baselines under comparable adapter budgets. Both variants perform similarly when context shifts the grid uniformly, while cell-wise routing is strictly better when contexts are spatially heterogeneous. When fine-tuning a language model on six interleaved GLUE tasks, task-conditioned routing at a fixed adapter budget outperforms LoRA and static localized adapters, matching per-task adapters with 6x budgets. At decoder scale on Qwen2.5-1.5B, both routed variants outperform static baselines across eight commonsense benchmarks, with cell-wise routing achieving +3.9 points over LoRA at matched active capacity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Babak Barazandeh, Subhabrata Majumdar, Vinay Prithyani, George Michailidis
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
