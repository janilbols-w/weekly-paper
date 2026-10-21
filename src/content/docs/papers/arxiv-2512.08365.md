---
title: "Magneton: Optimizing Energy Efficiency of ML Systems via Differential Energy Debugging"
description: "The training and deployment of machine learning (ML) models have become extremely energy-intensive."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2512.08365) · [PDF](https://arxiv.org/pdf/2512.08365)

## 一句话摘要

The training and deployment of machine learning (ML) models have become extremely energy-intensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

The training and deployment of machine learning (ML) models have become extremely energy-intensive. While existing optimization efforts focus primarily on hardware energy efficiency, a significant but overlooked source of inefficiency is software energy waste caused by poor software design. This often includes redundant or poorly designed operations that consume more energy without improving performance. These inefficiencies arise in widely used ML frameworks and applications, yet developers often lack the visibility and tools to detect and diagnose them. We propose differential energy debugging, a novel approach that leverages the observation that competing ML systems often implement similar functionality with vastly different energy consumption. Building on this insight, we design and implement Magneton, an energy profiler that compares energy consumption between similar ML systems at the operator level and automatically pinpoints code regions and configuration choices responsible for excessive energy use. Applied to 9 popular ML systems spanning LLM inference, general ML frameworks, and image generation, Magneton detects and diagnoses 16 known cases of software energy inefficiency and further discovers 8 previously unknown cases, 7 of which have been confirmed by developers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yi Pan, Wenbo Qian, Dedong Xie, Ruiyan Hu, Yigong Hu, Baris Kasikci
- 发布：2026-10-21；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
