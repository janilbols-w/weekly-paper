---
title: "Expert-Choice Routing Enables Adaptive Computation in Diffusion Language Models"
description: "Diffusion language models (DLMs) enable parallel, non-autoregressive text generation, yet existing DLM mixture-of-experts (MoE) models inherit token-choice (TC) routing from autoregressive systems, leading to load imbalance and rigid computation allocation."
---

**评分：40/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2604.01622) · [PDF](https://arxiv.org/pdf/2604.01622)

## 一句话摘要

Diffusion language models (DLMs) enable parallel, non-autoregressive text generation, yet existing DLM mixture-of-experts (MoE) models inherit token-choice (TC) routing from autoregressive systems, leading to load imbalance and rigid computation allocation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (DLMs) enable parallel, non-autoregressive text generation, yet existing DLM mixture-of-experts (MoE) models inherit token-choice (TC) routing from autoregressive systems, leading to load imbalance and rigid computation allocation. We show that expert-choice (EC) routing is a better fit for DLMs: it provides deterministic load balancing by design, yielding higher throughput and faster convergence than TC. Building on the property that EC capacity is externally controllable, we introduce timestep-dependent expert capacity, which varies expert allocation according to the denoising step. We find that allocating more capacity to low-mask-ratio steps consistently achieves the best performance under matched FLOPs, and provide a mechanistic explanation: tokens in low-mask-ratio contexts exhibit an order-of-magnitude higher learning efficiency, so concentrating compute on these steps yields the largest marginal return. Finally, we show that existing pretrained TC DLMs can be retrofitted to EC by replacing only the router, achieving faster convergence and improved accuracy across diverse downstream tasks. Together, these results establish EC routing as a superior paradigm for DLM MoE models and demonstrate that computation in DLMs can be treated as an adaptive policy rather than a fixed architectural constant. Code is available at https://github.com/zhangshuibai/EC-DLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shuibai Zhang, Caspian Zhuang, Chihan Cui, Zhihan Yang, Fred Zhangzhi Peng, Yanxin Zhang, Haoyue Bai, Zack Jia, Yang Zhou, Guanhua Chen, Ming Liu
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/zhangshuibai/EC-DLM](https://github.com/zhangshuibai/EC-DLM)
- 阅读深度：metadata
