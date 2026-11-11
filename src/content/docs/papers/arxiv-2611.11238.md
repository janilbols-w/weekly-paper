---
title: "FRESCO: A Novel Consistency Control for Asynchronous Pipeline Parallel Training"
description: "Asynchronous pipeline parallelism can accelerate distributed model training, but suffers from instability caused by inconsistent gradient computations."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2611.11238) · [PDF](https://arxiv.org/pdf/2611.11238)

## 一句话摘要

Asynchronous pipeline parallelism can accelerate distributed model training, but suffers from instability caused by inconsistent gradient computations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Asynchronous pipeline parallelism can accelerate distributed model training, but suffers from instability caused by inconsistent gradient computations. We identify a fundamental source of this inconsistency: error signals are coupled to forward-time features, not just parameter states. This means that parameters may evolve as long as they preserve forward-equivalence. Leveraging this insight, we introduce FRESCO, which frames asynchronous updates as a constrained optimization problem: it finds the minimal update modification that acts trivially on the activation subspace. We demonstrate that FRESCO consistently outperforms representative asynchronous baselines in LLM pre-training, with the gains most pronounced under deep pipelines and high inconsistency levels: at pipeline depth 32, it reaches the same loss as the strongest baseline with 43% fewer iterations and 30% less wall-clock time, while requiring 8~921$\times$ less memory overhead. Moving beyond the current limitations, FRESCO establishes a new foundation for high-utilization pipeline parallel training, providing a scalable path for large-model development on diverse, resource-constrained systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pipeline parallel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dongyeop Lee, Namhoon Lee
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
