---
title: "STAR: Counterfactual Dual-World Rollouts and Spatial Target Adaptive Reconstruction for Visual On-Policy Distillation"
description: "Vision-language models often rely on global context and language priors while overlooking answer-determining local details."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.32472) · [PDF](https://arxiv.org/pdf/2611.32472)

## 一句话摘要

Vision-language models often rely on global context and language priors while overlooking answer-determining local details.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models often rely on global context and language priors while overlooking answer-determining local details. Privileged visual on-policy self-distillation supervises full-image student rollouts using a frozen teacher that views high-resolution evidence crops. Yet our cross-scale diagnostics show that models retain over half of their full-image accuracy when local evidence is completely masked, indicating that single-image correctness does not guarantee reliance on local evidence, while the need for visual correction also varies across tokens with their spatial attention states. We propose STAR, a visual on-policy self-distillation framework combining independent counterfactual dual-world rollouts with spatial-attention-guided target reconstruction. Local image editing constructs paired worlds with identical questions and backgrounds but distinct answer-determining facts, where a shared student samples trajectories independently to expose contextual shortcuts under image-consistent prefixes. Within each world, the teacher contrasts real and mean-color crops to determine the visual correction direction, while the divergence between student image attention and a teacher-centroid spatial reference adaptively controls token-wise target log-probability reconstruction. Without auxiliary attention losses or test-time tool overhead, STAR improves Qwen3.5 across scales by up to 8.04 percentage points in average accuracy over initialization across six fine-grained benchmarks, reaches OPSD's final accuracy $4.7\times$ faster, and generalizes to out-of-domain reasoning tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yi Zou, Zhuang Yan, Yudong Zhang, Xu Wang, Yang Wang
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
