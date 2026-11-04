---
title: "STLT: A Novel System for Energy-Aware Distributed Inference in the Edge-Cloud-Space Continuum"
description: "Low Earth Orbit satellites are pivotal for Earth observation tasks such as wildfire detection, capturing imagery for analysis by Deep Neural Networks (DNNs)."
---

**评分：48/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2611.01233) · [PDF](https://arxiv.org/pdf/2611.01233)

## 一句话摘要

Low Earth Orbit satellites are pivotal for Earth observation tasks such as wildfire detection, capturing imagery for analysis by Deep Neural Networks (DNNs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Low Earth Orbit satellites are pivotal for Earth observation tasks such as wildfire detection, capturing imagery for analysis by Deep Neural Networks (DNNs). On-board analysis reduces downlink volume, but severe energy constraints force a trade-off between computation and data transmission. Splitting the DNN between satellite and ground turns this balance into a design choice, where the split point determines combined computation and downlink energy. Existing approaches typically rely on static split-point decisions that fail to account for dynamic space conditions, or on complex algorithms, historical data, or prediction models that introduce significant overhead. To address these shortcomings, we present STLT, a two-stage system for energy-aware distributed inference between LEO satellites and a ground station. First, an offline analyzer characterizes the DNN architecture to identify a set of favorable split points, consequently reducing the search space. Second, an on-board algorithm performs lightweight energy-aware split selection, dynamically choosing from this pre-computed set based on the current state of the environment. We evaluate STLT on a real-world satellite telemetry dataset, showing that it reduces the split-candidate search space by 30.7% on average, lowers decision latency by 25.1% and energy by 27.5% on average, and delivers up to 20.1% more inference tasks than a state-of-the-art satellite-ground co-inference baseline while consuming 8.8% less energy overall.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Andrija Stanisic, Milos Gravara, Juan Luis Herrera, Stefan Nastic
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
