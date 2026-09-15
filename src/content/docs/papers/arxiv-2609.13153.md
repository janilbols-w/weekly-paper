---
title: "DVFS for Small Language Model Inference on Mobile Edge Devices"
description: "This paper presents DVFSLM, a new dynamic voltage and frequency scaling (DVFS) design for energy-efficient inference of small language models (SLMs) on mobile edge devices."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.13153) · [PDF](https://arxiv.org/pdf/2609.13153)

## 一句话摘要

This paper presents DVFSLM, a new dynamic voltage and frequency scaling (DVFS) design for energy-efficient inference of small language models (SLMs) on mobile edge devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper presents DVFSLM, a new dynamic voltage and frequency scaling (DVFS) design for energy-efficient inference of small language models (SLMs) on mobile edge devices. The growing demand for local execution of language models has driven the adoption of SLMs, which balance computational feasibility with good inference performance. However, energy efficiency remains a critical challenge, since even miniaturized SLMs impose significant energy consumption, impacting application quality, device reliability, and environmental sustainability. Existing DVFS solutions, designed for cloud-based large models or generic mobile workloads, fail to address the unique workload characteristics of SLMs, resulting in wasted energy or excessive latency. Unlike prior work, DVFSLM explicitly addresses two key challenges: 1) the complex interdependencies of processor frequencies, power and latency across autoregressive token generations, and 2) hardware opacity, where the individual power and latency contributions from different processors (GPU, CPU and EMC) are obscured during collaborative execution. To address these, DVFSLM introduces workload-aware power and latency estimators that analyze core matrix operations and correlate them with hardware metadata, enabling precise estimations of how frequency adjustments impact power and latency. These estimations drive a runtime DVFS governor that coordinates the GPU and EMC frequencies with a profiled CPU-frequency threshold, minimizing the energy per token while satisfying configurable token-generation deadlines. Extensive experiments on a rich set of SLMs show that DVFSLM reduces the energy per token by up to 12.4% over the latest built-in governors and up to 8.4% over the state-of-the-art GearDVFS, while improving the latency quality of service (QoS) by up to 93.12% and 69.14%, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiesong Chen, Lixiang Han, Jiani Cao, Zhaoxi Yue, Zhenjiang Li
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
