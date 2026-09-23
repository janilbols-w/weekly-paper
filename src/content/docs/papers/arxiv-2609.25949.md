---
title: "Flux: Optimal Scheduling of Optical Circuit Switches for LLM Training"
description: "Optical Circuit Switching (OCS) offers high bandwidth density and energy efficiency for LLM training, but incurs a non-negligible reconfiguration delay."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.25949) · [PDF](https://arxiv.org/pdf/2609.25949)

## 一句话摘要

Optical Circuit Switching (OCS) offers high bandwidth density and energy efficiency for LLM training, but incurs a non-negligible reconfiguration delay.

## 为什么值得关注

待编辑增强。

## 摘要原文

Optical Circuit Switching (OCS) offers high bandwidth density and energy efficiency for LLM training, but incurs a non-negligible reconfiguration delay. Prior work typically schedules optical circuit switches independently of compute, using aggregate traffic demand to determine which circuits to provision and when. We argue that this separation creates a fundamental inefficiency: reconfigurations that ignore the compute timeline can stall communication, resulting in low circuit utilization and large buffer requirements. In this paper, we present Flux, a scheduler that optimally schedules optical circuit switches based on the structure of the entire workload. Flux remains effective across a wide range of switching speeds by reusing circuits and amortizing reconfiguration delay behind compute and communication. We show that Flux reduces training iteration time by up to $10\times$ and peak NIC buffer requirements by more than three orders of magnitude compared to traditional periodic schedulers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Arno Troch, Seyyidahmed Lahmer, Abubakr Nada, Jeroen Famaey, Michael Peeters
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
