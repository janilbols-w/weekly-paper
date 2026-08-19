---
title: "Automatically Generating ML Compiler Backends from Tensor Accelerator ISA Descriptions"
description: "Machine learning (ML) compilers play a key role in enabling high-performance implementations of ML workloads."
---

**评分：50/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2510.09932) · [PDF](https://arxiv.org/pdf/2510.09932)

## 一句话摘要

Machine learning (ML) compilers play a key role in enabling high-performance implementations of ML workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Machine learning (ML) compilers play a key role in enabling high-performance implementations of ML workloads. These compilers use existing CPU and GPU backends to generate device-specific code. In recent years, many tensor accelerators (or AI accelerators) have been designed to further accelerate these workloads, with commercial products like AWS Trainium publicly available. However, compared to commodity hardware, a majority of tensor accelerators do not have mature ML compiler backends with robust code generation support. Moreover, tensor accelerator designs are subject to fast iteration cycles, making it difficult to manually develop and maintain ML compiler backends. Therefore, to enable faster integration of novel tensor accelerator designs in ML infrastructure, we need to make the compiler backend construction process more agile. We introduce ACT, a compiler backend generator that automatically generates compiler backends for tensor accelerators, given just the instruction set architecture (ISA) descriptions. These backends are integrated with XLA, a production ML compiler. ACT uses a novel ISA-parameterized compilation algorithm to generate a compiler backend with an equality-saturation-based instruction selection phase and a constraint-programming-based memory allocation phase. We generated compiler backends for 6 accelerator platforms from industry (e.g., AWS Trainium, Intel AMX) and academia (e.g., Gemmini). We showed that these generated backends match or outperform commercial compiler backends and expert-written kernel libraries, while maintaining low compilation overheads. Notably, ACT-generated backend for AWS NKI ISA improved the code generation coverage for AWS Trainium by 2.3x compared with AWS's production compiler, neuronx-cc. ACT is part of a larger open-source ecosystem (https://github.com/act-compiler/act) built around our ISA description language, TAIDL.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Devansh Jain, Akash Pardeshi, Marco Frigo, Kaustubh Khulbe, Krut Patel, Saatvik Lochan, Jai Arora, Charith Mendis
- 发布：2026-08-19；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/act-compiler/act](https://github.com/act-compiler/act)
- 阅读深度：metadata
