---
title: "A-MADiff: Attention-Guided Multi-Agent DRL with Diffusion Policies for Memory-Aware Task Orchestration in Mobile AIGC Networks"
description: "Artificial Intelligence-Generated Content (AIGC) services employ Generative AI (GenAI) models to automatically generate diverse content."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.29255) · [PDF](https://arxiv.org/pdf/2608.29255)

## 一句话摘要

Artificial Intelligence-Generated Content (AIGC) services employ Generative AI (GenAI) models to automatically generate diverse content.

## 为什么值得关注

待编辑增强。

## 摘要原文

Artificial Intelligence-Generated Content (AIGC) services employ Generative AI (GenAI) models to automatically generate diverse content. Mobile AIGC networks host GenAI models on edge-located AIGC Service Providers (ASPs) to deliver low-latency and personalized AIGC services for mobile users. However, AIGC inference tasks typically occupy GPU memory until task completion, causing GPU memory exhaustion at serving ASPs and triggering out-of-memory failures rather than merely increasing service latency. Existing studies on AIGC task orchestration have largely overlooked GPU memory feasibility constraints. To address this issue, we develop a cooperative multi-agent orchestration framework, in which each edge node is equipped with a scheduling agent to route tasks to local ASPs or neighboring edge nodes. Since scheduling agents make decisions based only on local observations, while peer offloading couples their resource states and long-term utilities, we formulate the orchestration process as a cooperative Decentralized Partially Observable Markov Decision Process (Dec-POMDP). To solve the Dec-POMDP, we propose an \underline{A}ttention-guided \underline{M}ulti-\underline{A}gent deep reinforcement learning algorithm with \underline{Diff}usion policies (A-MADiff) under the centralized training with a decentralized execution paradigm. A-MADiff employs diffusion-based decentralized actors to generate multi-modal preferences over feasible orchestration actions, and an attention-guided centralized critic to estimate per-agent values from cross-agent states under GPU memory heterogeneity. Numerical results demonstrate that A-MADiff significantly improves the cumulative reward over the state-of-the-art baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chongzhi Wu, Zhengtao Li, Jiawen Kang, Jinbo Wen, Xiaohuan Li, Maomao Zhang, Ekram Hossain
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
