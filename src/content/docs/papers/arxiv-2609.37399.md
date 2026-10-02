---
title: "MEDEM: Multi-Engine DL Accelerator Design Methodology"
description: "Multi-engine deep learning (DL) accelerators are becoming increasingly prevalent as they address the heterogeneity and growing complexity of modern DL workloads."
---

**评分：51/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.37399) · [PDF](https://arxiv.org/pdf/2609.37399)

## 一句话摘要

Multi-engine deep learning (DL) accelerators are becoming increasingly prevalent as they address the heterogeneity and growing complexity of modern DL workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-engine deep learning (DL) accelerators are becoming increasingly prevalent as they address the heterogeneity and growing complexity of modern DL workloads. To efficiently process diverse DL workloads, these accelerators must incorporate combinations of engines with complementary capabilities to match the distinct computational characteristics of these workloads' heterogeneous kernels. However, existing multi-engine DL accelerator design approaches lack a systematic methodology, leaving fundamental questions unresolved. These include how to co-design engines for workloads with diverse computational characteristics and which engine combinations minimize aggregate execution costs (such as time or energy) across such workloads. Addressing these questions requires efficient exploration of exponentially large design spaces. To address these questions systematically, this work proposes Multi-Engine DL Accelerator Design Methodology (MEDEM). MEDEM defines generic engine abstractions, co-designs candidate instances (engines), and selects a combination of co-designed engines to minimize aggregate execution cost given diverse DL workloads and a resource budget. MEDEM encompasses a set of design strategies that efficiently navigate the exponentially large design spaces of engine co-design and combination selection, identifying highly optimized multi-engine accelerators. A comprehensive evaluation demonstrates that MEDEM identifies accelerators that outperform state-of-the-art designs, delivering geometric-mean improvements of up to 4.84x in energy-delay product (EDP) and 1.59x in throughput. The improvements are achieved using different resource budgets, demonstrating MEDEM's scalability, and using 51 single- and multi-model DL workloads, demonstrating its generalizability.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Fareed Qararyah, Mohammad Ali Maleki, Pedro Trancoso
- 发布：2026-09-29；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
