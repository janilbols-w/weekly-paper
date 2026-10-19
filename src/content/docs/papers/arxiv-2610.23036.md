---
title: "Towards Looped Models Done Right, Part I: Topology, Input Injection, Recurrent-State Design"
description: "Looped language models reuse physical Transformer blocks across logical depth, but established architectures entangle recurrence placement, input injection, and recurrent state organization."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2610.23036) · [PDF](https://arxiv.org/pdf/2610.23036)

## 一句话摘要

Looped language models reuse physical Transformer blocks across logical depth, but established architectures entangle recurrence placement, input injection, and recurrent state organization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped language models reuse physical Transformer blocks across logical depth, but established architectures entangle recurrence placement, input injection, and recurrent state organization. We isolate these axes in models trained from scratch at matched parameter scale, logical depth, and token budgets, and then test whether the resulting design principles transfer to resident- and active-parameter-matched Mixture-of-Experts (MoE) models. The prelude-recurrent block-coda sandwich architecture consistently improves performance on context extraction and reasoning-intensive tasks. Input injection primarily enhances knowledge retrieval and context utilization, whereas random initialization and separate H/L recurrent states provide mixed or negative returns. Taken together, these results favor the Huginn-style design: at the 730M-parameter and 336B-token scale, the complete Huginn architecture outperforms Ouro across all ten benchmarks. The advantages of Huginn over Ouro transfer to MoE models. At the 8BA0.8B (32BA3B when unrolled) scale trained on 500B tokens, Huginn outperforms Ouro on nearly all benchmarks spanning knowledge, reasoning, and coding, while also exhibiting more balanced expert routing. Under matched training and inference FLOPs, the Huginn-style model uses 75% fewer resident parameters than a 112-layer feedforward MoE baseline. Despite its smaller physical parameters, it outperforms the feedforward baseline on DROP and GSM8K, matches it on MATH500, and remains competitive on the other benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Benhao Huang, Chufan Shi, Junlin Chen, Shicheng Wen, Zhengzhong Liu, Eric Xing, Xuezhe Ma
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
