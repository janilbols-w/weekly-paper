---
title: "CascadeLUT: Information-Ordered Streaming Inference for Bandwidth-Constrained FPGAs"
description: "Mapping neural networks to FPGAs enables low-latency, energy-efficient inference, particularly for lookup table (LUT)-based models that eliminate multipliers and map directly to reconfigurable fabric."
---

**评分：47/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.00720) · [PDF](https://arxiv.org/pdf/2608.00720)

## 一句话摘要

Mapping neural networks to FPGAs enables low-latency, energy-efficient inference, particularly for lookup table (LUT)-based models that eliminate multipliers and map directly to reconfigurable fabric.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mapping neural networks to FPGAs enables low-latency, energy-efficient inference, particularly for lookup table (LUT)-based models that eliminate multipliers and map directly to reconfigurable fabric. While prior work achieves high compute efficiency, it typically assumes full-sample availability, causing pipeline stalls in bandwidth-limited streaming scenarios. Here, the bottleneck shifts from computation to data movement, as large input transfers limit throughput and energy efficiency. We present CascadeLUT, an information-structured inference framework organized around bandwidth constraints. Instead of buffering the full input, features are partitioned into ordered subsets and predictions are progressively refined as subsets arrive. The cascade statically controls which layers consume incoming features, enabling deterministic streaming inference without runtime branching. By co-designing feature scheduling with hardware dataflow, CascadeLUT reduces data movement while maintaining accuracy. Across datasets, it achieves 4.0 to 12.5 times lower latency, 3.0 to 5.0 times higher throughput and up to 13.8 times lower energy/sample than prior LUT baselines, using 1.2 to 4.4 times the LUTs of the smallest DWN baseline per task. We also demonstrate on-device input quantization integrated with LUT-based inference and present end-to-end FPGA results on real-world workloads, with 5 times reductions in quantization overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Oliver Cassidy, Marta Andronic, George A. Constantinides
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
