---
title: "Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR"
description: "Reinforcement learning with verifiable rewards (RLVR) and on-policy distillation (OPD) have emerged as two dominant methods for post-training reasoning LLMs."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.04108) · [PDF](https://arxiv.org/pdf/2609.04108)

## 一句话摘要

Reinforcement learning with verifiable rewards (RLVR) and on-policy distillation (OPD) have emerged as two dominant methods for post-training reasoning LLMs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning with verifiable rewards (RLVR) and on-policy distillation (OPD) have emerged as two dominant methods for post-training reasoning LLMs. Prior work uses OPD's dense token-level supervision to complement the sparse RL reward, fusing the two signals within a single step: either as a \emph{weighted-additive combination} or a \emph{teacher-modulated rescaling} of the RL advantage. In this paper, we show that a simple two-stage scheme, OPD-then-RL, consistently outperforms pure OPD, pure RLVR, and all such joint baselines across logic and math reasoning benchmarks. Beyond the empirical results, we further provide a systematic understanding of this through pass@$k$ behavior, learning dynamics, and parameter updates, yielding a consistent explanation: OPD expands the student's coverage of teacher-supported solutions and RL sharpens within that support, while jointly optimizing the two signals causes them to interfere.To provide a practical recipe, we find that the OPD validation score is the key signal for when to switch to RL, and that OPD is a better cold start for RL than SFT. Together, our results establish OPD-then-RL as a simple yet strong way to combine the two methods, turning two entangled signals into complementary stages.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Boyan Li, Bingsen Chen, Chenghao Yang, Ping Nie, Chen Zhao, Xi Ye
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
