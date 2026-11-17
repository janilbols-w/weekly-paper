---
title: "Coordinated Cooling and Compute Management for AI Datacenters"
description: "The AI datacenters are currently being deployed on a large scale to support the training and deployment of power-intensive large-language models (LLMs)."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2601.08113) · [PDF](https://arxiv.org/pdf/2601.08113)

## 一句话摘要

The AI datacenters are currently being deployed on a large scale to support the training and deployment of power-intensive large-language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

The AI datacenters are currently being deployed on a large scale to support the training and deployment of power-intensive large-language models (LLMs). Extensive amount of computation and cooling required in datacenters increase concerns about the energy use and carbon emissions of AI datacenters. Although current state-of-the-art has examined the energy efficiency of LLM inference, most prior research focused on optimizing compute-side scheduling without considering thermal objectives or constraints. Since GPU-intensive inference generates substantial heat that can degrade datacenter performance, ignoring thermal effects can increase total energy consumption and reduce the efficiency of LLM serving. To fill this gap, we profile the characteristics of GPU servers under varying cooling and AI jobs, and develop a joint cooling and computing modeling approach for AI datacenters. Built upon such workload and thermal dynamics models, a novel hierarchical control framework is proposed to co-optimize computing and thermal management by identifying the optimal GPU parallelism, frequency (DVFS), and cooling control knobs. Using real Azure inference traces and detailed GPU profiling, our model balances serving latency and thermal constraints in AI datacenters while significantly improving AI datacenters' energy efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency, thermal management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nardos Belay Abera, Yize Chen
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
