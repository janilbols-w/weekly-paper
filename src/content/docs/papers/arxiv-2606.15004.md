---
title: "Measure the Deployment, Not Just the Model: Rethinking Hardware-Aware Model Selection for Microcontrollers"
description: "Selecting an energy-efficient model for periodic sensing requires accounting for time between inferences."
---

**评分：49/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2606.15004) · [PDF](https://arxiv.org/pdf/2606.15004)

## 一句话摘要

Selecting an energy-efficient model for periodic sensing requires accounting for time between inferences.

## 为什么值得关注

待编辑增强。

## 摘要原文

Selecting an energy-efficient model for periodic sensing requires accounting for time between inferences. Hardware-aware model search typically measures inference alone, even when the application cares about energy per release. We present CREST (Cross-platform Runtime Evaluation and Search Tool), an open-source hardware-in-the-loop experimentation system that evaluates model and hardware configurations under a specified release schedule. Researchers can vary the objective, schedule, target and candidate proposer while reusing evaluation and replay. Records preserve comparison conditions and separate valid measurements from deployable candidates. Three case studies demonstrate the system. First, searches and controlled replay on STM32 N657 show how waiting changes model and clock selection. For one architecture, continuous inference favors 800 MHz over 300 MHz at 8.0 versus 17.1 mJ per inference, but additional waiting offsets 97% of this saving in a fitted decomposition. With STOP between releases, 300 MHz uses about 0.3-0.4% less board energy per release at 100 and 500 ms. At a fixed clock, the preferred architecture changes between release periods, which a model with shared waiting parameters cannot produce. Latency predicts continuous energy within a median 1.7% on held-out observations, yet most release-energy error remains in scheduled terms. In paired replay, one of six randomly selected near-latency pairs reverses its continuous-energy order by 5.8 mJ per release. Second, replay on three Arduino targets shows proxy-selected inertial-odometry candidates can fail to fit or use more energy than measured selections, with only 9 of 16 FLOPs-selected candidates fitting the most memory-constrained board. Third, an audio classification study reuses the evaluator with LLM-based candidate proposers, and cross-target replay moves a selected configuration from third to last in energy rank.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Joseph Q. Zales, Pragya Sharma, Mani Srivastava
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
