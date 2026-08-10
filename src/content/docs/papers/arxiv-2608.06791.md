---
title: "HLSmith: An Expert-Guided Agentic Framework for C/C++-to-HLS Translation"
description: "Application-specific FPGA accelerators offer substantial performance and energy-efficiency gains across many application domains, but developing them is costly, often requiring months of specialized effort."
---

**评分：47/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.06791) · [PDF](https://arxiv.org/pdf/2608.06791)

## 一句话摘要

Application-specific FPGA accelerators offer substantial performance and energy-efficiency gains across many application domains, but developing them is costly, often requiring months of specialized effort.

## 为什么值得关注

待编辑增强。

## 摘要原文

Application-specific FPGA accelerators offer substantial performance and energy-efficiency gains across many application domains, but developing them is costly, often requiring months of specialized effort. Even with high-level synthesis (HLS), designers still need extensive hardware expertise to build high-performance accelerators. Although large language models (LLMs) have demonstrated strong software-generation capabilities, even frontier models lack the hardware intuition and procedural knowledge needed to reliably translate baseline C/C++ programs into high-performance HLS designs: they struggle to identify effective architectures, follow the optimization processes used by HLS experts, and apply hardware transformations consistently across diverse kernels. We present HLSmith, an expert-guided framework for translating C/C++ programs into optimized HLS accelerators. HLSmith combines three components: an HLS optimization expertise library that encodes guarded transformation recipes, their applicability and prerequisite conditions, and unsafe cases to avoid; a staged, feedback-driven orchestration flow modeled on expert HLS development practice that guides agents through synthesis, bottleneck analysis, and optimization; and a tool-grounded model-adaptation pipeline that converts optimization trajectories from commercial frontier models into training data for fine-tuning open-weight LLMs. We evaluate HLSmith on PolyBench against ChatHLS, a leading prior agent-orchestration framework for HLS accelerator development. HLSmith achieves a geometric mean speedup of 4.24x over ChatHLS while producing functionally correct designs, in both software and RTL simulation, for every benchmark, compared with ChatHLS's 57% valid-design rate. It further reaches speedups of up to 252x and 138x with commercial frontier models and open-weight models, respectively.

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

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yuebo Luo, Ahmad Sedigh Baroughi, Philip Stachura, Le Chen, Venkatram Vishwanath, Zhenman Fang, Caiwen Ding
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
