---
title: "Denser $\\neq$ Better: Limits of On-Policy Self-Distillation for Continual Post-Training"
description: "Continual post-training enables foundation models to acquire new knowledge while preserving existing capabilities."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.01763) · [PDF](https://arxiv.org/pdf/2607.01763)

## 一句话摘要

Continual post-training enables foundation models to acquire new knowledge while preserving existing capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Continual post-training enables foundation models to acquire new knowledge while preserving existing capabilities. Recent work suggests that on-policy learning can mitigate forgetting, with self-distillation as a particularly attractive approach. We revisit this optimistic claim through self-distillation policy optimization (SDPO). Our experiments show that SDPO accelerates in-domain specialization when teacher signals are stable and well aligned, but struggles to generalize out of distribution. In continual post-training, SDPO exhibits greater forgetting and can even collapse, whereas GRPO, the more established on-policy reinforcement learning method, adapts more conservatively and better preserves prior capabilities. Further analyses link these failures to increased drift in parameter and response space, and to amplification of high-frequency artifacts through a self-reinforcing teacher-student loop. Thus, on-policy data alone is insufficient for continual learning. Self-distillation is effective when teacher targets are stable and token-level supervision is reliable, but should not be treated as a default stabilizer for continual post-training. Our code is available at https://github.com/Moenupa/SDPO-CL.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Meng Wang, Haohan Zhao, Wenzhuo Liu, Lu Yang, Geng Liu, Haiyang Guo, Guo-Sen Xie, Gaofeng Meng, Hongbin Liu, Fei Zhu
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Moenupa/SDPO-CL](https://github.com/Moenupa/SDPO-CL)
- 阅读深度：metadata
