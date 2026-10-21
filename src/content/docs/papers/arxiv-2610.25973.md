---
title: "Correctness-Dependent Asymmetric Target Distributions for Self-Distillation Policy Optimization"
description: "Self-distillation policy optimization provides dense token-level supervision for LLM post-training through feedback-conditioned self-teachers."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.25973) · [PDF](https://arxiv.org/pdf/2610.25973)

## 一句话摘要

Self-distillation policy optimization provides dense token-level supervision for LLM post-training through feedback-conditioned self-teachers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-distillation policy optimization provides dense token-level supervision for LLM post-training through feedback-conditioned self-teachers. However, directly matching the self-teacher can disrupt successful behaviors on correct rollouts while providing insufficient correction on incorrect ones. We propose Asymmetric Policy Optimization via Self-Distillation (APSD), which constructs correctness-dependent targets by mixing student and self-teacher distributions: interpolation preserves successful behaviors on correct rollouts, while extrapolation beyond the self-teacher strengthens correction on incorrect ones. We analyze APSD through divergence decomposition, reverse-KL barycentric geometry, and gradient analysis, highlighting the importance of gradient flow through student-dependent targets. Experiments under reinforcement learning with verifiable rewards and rich feedback show that APSD achieves strong overall performance against reinforcement-learning and self-distillation baselines and matches SDPO performance with 2.6x fewer training steps on average across Qwen3 model scales.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Suwan Yoon, Seongryong Jung, Changhee Lee
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
