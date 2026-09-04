---
title: "Para-Pipe: Exploiting Hierarchical Operator Parallelism of ML Computational Graphs on SoCs"
description: "As edge-based deep learning applications become more complex, optimizing performance on heterogeneous System-on-Chips (SoCs) presents unique challenges."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.04168) · [PDF](https://arxiv.org/pdf/2609.04168)

## 一句话摘要

As edge-based deep learning applications become more complex, optimizing performance on heterogeneous System-on-Chips (SoCs) presents unique challenges.

## 为什么值得关注

待编辑增强。

## 摘要原文

As edge-based deep learning applications become more complex, optimizing performance on heterogeneous System-on-Chips (SoCs) presents unique challenges. Traditional pipelining techniques distributing the computation across different on-chip processing units, while effective for throughput, do not address the latency demands posed by modern neural networks with complex interdependencies and extensive operator parallelism. There is a potential in leveraging operator parallelism to enable concurrent execution across multiple processing units, thereby reducing inference latency. However, prioritizing pipelining or parallel execution often necessitates a compromise, where optimizing one performance metric adversely impacts the other. This paper introduces Para-Pipe, a hierarchical mapping framework that integrates intra- and inter-stage operator parallelism within a pipelined architecture. Para-Pipe navigates the trade-off between throughput and latency by selectively fine-tuning parallelism levels within and across pipeline stages. This strategy can significantly reduce inter-processor communication overhead, significantly improving energy efficiency. Our evaluation demonstrates that Para-Pipe generates multiple Pareto-optimal configurations, achieving a balance between throughput and latency on an Amlogic SoC equipped with ARM big.LITTLE CPUs and GPU, as well as the Black Sesame Technology SoC featuring a deep learning accelerator and two DSPs. More importantly, throughput-optimized configurations under Para-Pipe on Amlogic SoC show an average energy efficiency improvement of 11.0% over purely pipelined strategies and 23.3% relative to non-pipelined parallel execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 6 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yujie Zhang, Huiying Lan, Ehsan Aghapour, Zhiyuan Ning, Peng Zan, Weidong Shao, Anuj Pathania, Tulika Mitra
- 发布：2026-09-03；更新：2026-09-04
- 来源：arXiv RSS；Venue：IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 44, no. 12, pp. 4472-4485, Dec. 2025
- 代码：未发现
- 阅读深度：metadata
