---
title: "X-GS: An Extensible Framework for Perceiving and Thinking with 3D Gaussian Splatting"
description: "3D Gaussian Splatting (3DGS) has emerged as a powerful technique for novel view synthesis, subsequently extending into numerous spatial AI applications."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.09632) · [PDF](https://arxiv.org/pdf/2603.09632)

## 一句话摘要

3D Gaussian Splatting (3DGS) has emerged as a powerful technique for novel view synthesis, subsequently extending into numerous spatial AI applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

3D Gaussian Splatting (3DGS) has emerged as a powerful technique for novel view synthesis, subsequently extending into numerous spatial AI applications. However, most existing 3DGS methods operate in isolation, focusing on specific domains. In this paper, we introduce X-GS, an extensible framework that integrates previously isolated 3DGS methods into the perception module of a VLM for spatial tasks, with two major components: the $\textit{Perceiver}$ and the $\textit{Thinker}$. The $\textit{Perceiver}$ performs online 3DGS-based SLAM with semantic distillation and outputs semantic Gaussians from unposed video streams. It leverages recent vision foundation models for stronger geometric priors, and we introduce three novel optimizations to improve semantic distillation efficiency. The $\textit{Thinker}$ interfaces diverse VLMs with these semantic Gaussians, unlocking spatial multimodal capabilities such as 3D visual grounding and scene captioning. Experimental results on diverse benchmarks demonstrate the efficiency and newly unlocked multimodal capabilities of the X-GS framework.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yueen Ma, Zenglin Xu, Irwin King
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
