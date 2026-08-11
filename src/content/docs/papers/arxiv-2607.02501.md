---
title: "Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots"
description: "Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.02501) · [PDF](https://arxiv.org/pdf/2607.02501)

## 一句话摘要

Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied$.$cpp on three VLA and two WAM models, using normalized comparisons across Python and C++ quantization configurations. Overall, Embodied$.$cpp achieves 1.05x-2.70x inference speedups and 7\%-77\% lower VRAM relative to Python baselines, while maintaining near-baseline success for most configurations. These results show that Embodied$.$cpp improves deployment efficiency while preserving high control quality across diverse embodied model architectures. Project Link: https://github.com/SEU-PAISys/Embodied.cpp

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Ling Xu, Borui Li, Hao Wu, Chuyu Han, Xiangyu Li, Mohan Hua, Shiqi Jiang, Ting Cao, Chuanyou Li, Sheng Zhong, Shuai Wang
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/SEU-PAISys/Embodied.cpp](https://github.com/SEU-PAISys/Embodied.cpp)
- 阅读深度：metadata
