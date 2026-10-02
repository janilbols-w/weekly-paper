---
title: "Latency and accuracy tradeoffs in Spiking Neural Networks"
description: "Spiking neural networks are attractive for low-power speech command recognition, yet their latency has received far less attention than their energy efficiency, and their multi-timestep execution is widely assumed to make them slower than quantized neural networks."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.35260) · [PDF](https://arxiv.org/pdf/2609.35260)

## 一句话摘要

Spiking neural networks are attractive for low-power speech command recognition, yet their latency has received far less attention than their energy efficiency, and their multi-timestep execution is widely assumed to make them slower than quantized neural networks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking neural networks are attractive for low-power speech command recognition, yet their latency has received far less attention than their energy efficiency, and their multi-timestep execution is widely assumed to make them slower than quantized neural networks. This paper challenges the assumption that more local timesteps necessarily imply higher network latency. By overlapping computation across adjacent layers at the timestep level, SNNs may complete execution in less time than comparable bit-serial QNNs. However, this overlap relies on spikes firing on incomplete inputs, and a spike once generated cannot be withdrawn, so its error persists and reduces accuracy. Waiting for more input before firing would seem to improve accuracy at the cost of reduced overlap. Yet we find and prove that this intuition fails at some layers, where even a small increase in waiting can change spike timing and downstream computation, making the network both slower and less accurate. We therefore propose a Pipeline Delay Search method which selects each layer's delay by balancing task-level accuracy gains against added network latency. We then adapt the selected configurations through spike-based quantization-aware training and bounded tuning of firing thresholds and initial membrane potentials. Together, these steps form Falcon, a framework for Fine-grained Analysis of Latency and Controlled firing which systematically analyzes and optimizes SNN latency under a spatial analog compute-in-memory mapping with shared digital engines. We evaluate Falcon on GSCV2 and SSC, achieving competitive accuracies of 96.31 and 83.02 at modeled network-core latencies of 119.64 and 124.00us, respectively. Together, our analysis and results show that SNNs can compute more yet finish faster, and wait longer yet predict worse, highlighting why Falcon matters for both latency and accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhanglu Yan, Zixuan Zhu, Kaiwen Tang, Yuyang Cai, Qianhui Liu, Weng-Fai Wong
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
