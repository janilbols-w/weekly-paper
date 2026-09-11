---
title: "HDA-MoE: Hybrid Parallelism and Dynamic, Adaptive Scheduling for Mixture-of-Experts with 3D Near-Memory Processing"
description: "Mixture-of-Experts (MoE) architectures have become a key technique for scaling Large Language Models (LLMs), enabling high model capacity with reduced computational cost."
---

**评分：56/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.08682) · [PDF](https://arxiv.org/pdf/2609.08682)

## 一句话摘要

Mixture-of-Experts (MoE) architectures have become a key technique for scaling Large Language Models (LLMs), enabling high model capacity with reduced computational cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) architectures have become a key technique for scaling Large Language Models (LLMs), enabling high model capacity with reduced computational cost. However, this efficiency comes at the expense of increased memory capacity and bandwidth demands. Recent 3D Near-Memory Processing (NMP) architectures, which vertically integrate memory and compute through hybrid bonding, provide high internal bandwidth and energy efficiency, making them attractive for accelerating MoE inference. Nevertheless, the distributed memory and compute organization of NMP systems introduces new challenges for mapping MoE workloads. Existing parallelization strategies, such as Tensor Parallelism (TP) and Expert Parallelism (EP), suffer from either high communication costs or unbalanced computation utilization, leading to inferior efficiency. In addition, the dynamic routing behavior of MoE models further complicates efficient deployment. To address these challenges, we present HDA-MoE, a framework that optimizes MoE execution on NMP architectures through hybrid parallel deployment and runtime scheduling. HDA-MoE integrates an offline hybrid parallel mapping algorithm with an online dynamic and adaptive scheduling mechanism to reduce communication overhead while improving computation utilization. Experimental results show that HDA-MoE achieves a speedup of 1.1x--3.4x over TP, 1.1x--1.5x over EP, 1.1x--3.7x over the Hybrid TP-EP compute-balanced baseline, and 1.1x--1.3x over HD-MoE. Source code is available at https://github.com/PKU-SEC-Lab/HDA-MoE-TCAD26.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 18 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Haochen Huang, Shuzhang Zhong, Shengxuan Qiu, Zhe Zhang, Shuangchen Li, Cong Li, Dimin Niu, Hongzhong Zheng, Guangyu Sun, Runsheng Wang, Meng Li
- 发布：2026-09-08；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/PKU-SEC-Lab/HDA-MoE-TCAD26](https://github.com/PKU-SEC-Lab/HDA-MoE-TCAD26)
- 阅读深度：metadata
