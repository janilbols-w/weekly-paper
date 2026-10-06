---
title: "How Should Teachers Be Prepared? RL on Student-Induced States for On-Policy Distillation"
description: "On-policy distillation (OPD) improves the reasoning capabilities of small language models through token-level teacher supervision on student-generated trajectories."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.04950) · [PDF](https://arxiv.org/pdf/2610.04950)

## 一句话摘要

On-policy distillation (OPD) improves the reasoning capabilities of small language models through token-level teacher supervision on student-generated trajectories.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) improves the reasoning capabilities of small language models through token-level teacher supervision on student-generated trajectories. Yet can teachers that excel at solving problems independently also guide student reasoning effectively? Prior work shows that when student prefixes follow reasoning paths that differ from the teacher's own or contain errors, teachers can be less accurate when continuing from these prefixes than when solving problems independently. To this end, we propose Prep-OPD, which uses reinforcement learning (RL) before distillation to train the teacher to adapt to the student's existing reasoning state and correct course when errors arise. Training optimizes teacher continuations from fixed student prefixes using final-answer correctness as the reward. The prepared teacher then trains the student through trajectory guidance and token-level supervision. We evaluate Prep-OPD on eight mathematical reasoning benchmarks, using Qwen3-4B-Instruct-2507 as the teacher and Qwen3-0.6B and Qwen3-1.7B as students. With the 4B teacher and 1.7B student, Prep-OPD improves average accuracy over standard OPD and the strongest baseline, Relay-OPD, by 8.28 and 2.30 percentage points, respectively. Controlled experiments further show that teacher RL conditioned on student-generated prefixes yields higher student accuracy than problem-start teacher RL with and without handoff on Qwen3-1.7B. Reusing the same prepared teacher also improves Qwen3-0.6B.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaoyu Ma, Haoyue Liu, Zhichao Wang, Jionghao Zhu, Xiaoying Tang
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
