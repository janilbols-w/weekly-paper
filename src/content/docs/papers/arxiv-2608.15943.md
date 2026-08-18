---
title: "KV-Pipe: On the Relation Between KV Sharing and Pipeline Parallel Efficiency in LLMs"
description: "Pipeline parallelism (PP) is widely used to scale large language model (LLM) training, but its efficiency is often limited by stage imbalance and pipeline bubbles."
---

**评分：45/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2608.15943) · [PDF](https://arxiv.org/pdf/2608.15943)

## 一句话摘要

Pipeline parallelism (PP) is widely used to scale large language model (LLM) training, but its efficiency is often limited by stage imbalance and pipeline bubbles.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pipeline parallelism (PP) is widely used to scale large language model (LLM) training, but its efficiency is often limited by stage imbalance and pipeline bubbles. Meanwhile, cross-layer KV sharing has primarily been studied as a mechanism for reducing KV-cache costs during inference, without examining how KV reuse reshapes pipeline workloads. We present \textbf{KV-Pipe}, a stage-aware KV-sharing mechanism that turns KV reuse into a pipeline-balancing control knob. KV-Pipe starts from the tail stage, converts selected attention layers to cross-layer KV sharing in a tail-first order, and iteratively retargets the current bottleneck to drive the FLOPs Imbalance Ratio (FIR) toward $1$. The procedure is performed offline and requires only a pipeline partition and per-layer FLOPs estimates, introducing negligible runtime overhead and requiring no online tuning. Across multiple pipeline-parallel configurations, KV-Pipe consistently improves utilization and throughput, achieving up to \textbf{9.2\%} higher training MFU and up to a \textbf{9.8\%} reduction in iteration time, with larger gains at higher pipeline-parallel degrees where stage imbalance is amplified. Furthermore, the same KV-sharing mechanism provides an inference-side benefit by reducing KV-cache growth and redundant KV projection work, resulting in higher decoding throughput for long-context workloads. These results identify KV layout as a system--architecture degree of freedom for jointly improving pipeline-parallel training efficiency and long-context inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pipeline parallel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Maryam Dialameh, Hossein Rajabzadeh, Harish Krishnamoorthy Murali, Walid Ahmed, Weiwei Zhang, Hyock Ju Kwon
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
