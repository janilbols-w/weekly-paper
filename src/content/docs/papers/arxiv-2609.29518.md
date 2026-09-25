---
title: "CataOPD: Catalytic On-Policy Distillation for Large Language Model Reasoning"
description: "Reinforcement learning (RL) and on-policy distillation (OPD) are two representative paradigms for improving large language model reasoning."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.29518) · [PDF](https://arxiv.org/pdf/2609.29518)

## 一句话摘要

Reinforcement learning (RL) and on-policy distillation (OPD) are two representative paradigms for improving large language model reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) and on-policy distillation (OPD) are two representative paradigms for improving large language model reasoning. However, when no correct trajectory is sampled, RL lacks a positive correctness signal, while OPD remains constrained by the reasoning trajectories reachable under the student's on-policy distribution. Therefore, we propose CataOPD, where the teacher acts as a catalyst rather than a target, expanding reachability while internalizing verified student-produced trajectories into a catalyst-free policy. Self-Rescue Routing uses empirically all-failed groups as routing signals rather than teacher-intervention triggers, first seeking correct trajectories through additional on-policy self-sampling. For problems unresolved after self-rescue, Catalytic-Guided Self-Resolution uses catalytic guidance to elicit a verified student-produced trajectory in the guided student distribution. Barrier-Weighted Internalization weights tokens by guided-to-unguided log-probability gaps, focusing updates on decisive tokens difficult without guidance. Experimental results show that CataOPD outperforms current baselines, extends independent student reasoning to still-unrecovered problems, and improves out-of-distribution generalization under catalyst-free inference. Our project is available at https://github.com/QwenQKing/CataOPD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Wenjin Liu, Chenxi Wang, Jiapu Wang, Zhe Cui, Anh Tuan Luu, Haoran Luo
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/QwenQKing/CataOPD](https://github.com/QwenQKing/CataOPD)
- 阅读深度：metadata
