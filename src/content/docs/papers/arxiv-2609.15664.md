---
title: "CIDERS: Cloud-Edge LLM Collaborative Learning via Accelerating Personalized Bilevel Optimization"
description: "Amid the rapid advancement of physical-world intelligence, cloud-edge collaborative large language models (LLMs) have emerged as a promising roadmap for practical LLM deployment."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.15664) · [PDF](https://arxiv.org/pdf/2609.15664)

## 一句话摘要

Amid the rapid advancement of physical-world intelligence, cloud-edge collaborative large language models (LLMs) have emerged as a promising roadmap for practical LLM deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Amid the rapid advancement of physical-world intelligence, cloud-edge collaborative large language models (LLMs) have emerged as a promising roadmap for practical LLM deployment. However, existing cloud-edge paradigms struggle to balance global consensus with local personalization, which fails to satisfy the need for a unified knowledge foundation on the cloud and domain-specific adaptation at the edge. To address this, we introduce, for the first time, a personalized bilevel optimization framework that formalizes cloud-edge LLM collaboration as a dual structure: the upper level optimizes edge-side personalization, while the lower level governs cloud-side knowledge transfer, reaching cloud-edge evolving in coordination. We then propose CIDERS, an efficient solver that decomposes the model into a learnable backbone and a messenger. While the cloud performs knowledge transfer to the learnable backbone, the key lies in embedding global trajectories into each local personalization step via consensus-variate correction to reconcile personalization with consensus. We provide a comprehensive theoretical analysis, including a geometric characterization of the local trajectory and a full convergence guarantee, revealing an explicit trade-off structure between personalization and global convergence. Extensive experiments demonstrate that CIDERS consistently outperforms competitive baselines on the compressed edge path, with 3.1x and 1.7x gains on mathematical reasoning and code generation, respectively, and a 10\% relative gain on instruction metrics. Mechanism experiments attribute these gains to early consensus-corrected coordination and task-aware distillation. Overall, CIDERS offers a viable path toward consensus-guided continuous personalization in cloud-edge LLM systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Victor H. Chen, Hairui Yu, Stella K. Chung, Hong Yan
- 发布：2026-09-14；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
