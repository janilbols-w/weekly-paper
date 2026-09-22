---
title: "Towards Training-free Automatic Proxy Discovery via Large Language Models for Mixed Precision Quantization"
description: "Mixed-Precision Quantization (MPQ) liberates Deep Neural Networks (DNNs) from the Out-Of-Memory (OOM) bottleneck and has garnered increasing research attention."
---

**评分：54/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2512.07419) · [PDF](https://arxiv.org/pdf/2512.07419)

## 一句话摘要

Mixed-Precision Quantization (MPQ) liberates Deep Neural Networks (DNNs) from the Out-Of-Memory (OOM) bottleneck and has garnered increasing research attention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixed-Precision Quantization (MPQ) liberates Deep Neural Networks (DNNs) from the Out-Of-Memory (OOM) bottleneck and has garnered increasing research attention. However, conventional methods either rely on costly differentiable optimization search, which is neither efficient nor flexible, or learn a quantized DNN from a proxy (e.g., HAWQ) manually designed by human experts, which is labor-intensive and requires extensive expert knowledge. Can we design a proxy without involving any human experts or training? In this paper, we provide an affirmative answer by proposing a novel Large Language Model (LLM)-driven Training-free Automatic Proxy (dubbed TAP) discovery framework. It reforms the design paradigm of MPQ by utilizing LLMs and evolutionary search strategies to automatically find superior TAP tailored for MPQ. In addition, to bridge the gap between black-box LLMs and the challenging MPQ task, we introduce a lightweight Direct Preference Optimization (DPO)-based strategy controller that dynamically reweights the selection probabilities of the three prompt templates for evolutionary search strategies according to fitness signals, without fine-tuning the LLM. This forms a task-aware feedback loop that improves proxy generation across evolutions. Extensive experiments on mainstream benchmarks demonstrate that TAP achieves state-of-the-art performance. Finally, we believe that our TAP will significantly contribute to the MPQ community by providing a new perspective on LLM-driven design algorithms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixed precision, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haidong Kang, Jun Du, Guo Yu
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
