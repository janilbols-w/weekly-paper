---
title: "Toward Open ISA Supercomputing: A Comparative Study of RISC-V, Arm, and x86 Architectures on HPC Workloads"
description: "RISC-V is emerging as a candidate architecture for high-performance computing (HPC), but its competitiveness against established x86 and Arm processors remains difficult to assess because existing studies use different platforms, workloads, and methodologies, and rarely consider energy efficiency."
---

**评分：49/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.32632) · [PDF](https://arxiv.org/pdf/2610.32632)

## 一句话摘要

RISC-V is emerging as a candidate architecture for high-performance computing (HPC), but its competitiveness against established x86 and Arm processors remains difficult to assess because existing studies use different platforms, workloads, and methodologies, and rarely consider energy efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

RISC-V is emerging as a candidate architecture for high-performance computing (HPC), but its competitiveness against established x86 and Arm processors remains difficult to assess because existing studies use different platforms, workloads, and methodologies, and rarely consider energy efficiency. Our work provides an evaluation of contemporary HPC RISC-V, Arm, and x86 processors using a common software stack and methodology. We characterize the Sophgo SG2044 and compare it with the NVIDIA Grace CPU Superchip and Intel Xeon Platinum 8480+ across four HPC benchmarks (STREAM, HPL, HPL-MxP, and HPCG) and four representative applications (iPIC3D, PLUTO, OpenFOAM, and llama.cpp). The version of HPL-MxP linked to OpenBLAS built and used for this work is made available as open-source software. The SG2044 reaches 8.02 GFLOP/s of FP64 performance and 7.8 GB/s of memory bandwidth per core, increasing to 294 GFLOP/s and 107 GB/s at 64 cores. L2-cache-aware process placement enables near-linear scaling up to 16 cores, beyond which memory-bandwidth saturation limits further gains. Across generations of RISC-V hardware, in the context of the Monte Cimone (MC) project, the SG2044-based MCv3 doubles both single-core performance and peak memory bandwidth relative to MCv2, while improving memory bandwidth, node-level FP64 performance, and energy efficiency by approximately 100x, 158x, and 10x, over MCv1. Against the Arm and x86 systems, the SG2044 shows 8-15x less absolute performance, reflecting its narrower vector resources and less advanced technology node, but delivers competitive scaling and energy efficiency on several workloads. Its most notable result is LLM decode, where 64-core execution provides the highest relative scaling and energy efficiency among the evaluated platforms while exceeding Intel in throughput. Our results show that RISC-V processors are closing the gap with the competition.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Emanuele Venieri, Giacomo Madella, Gabriele Ceccolini, Simone Manoni, Federico Ficarelli, Filippo Barbari, Jenny Lynn Almerol, Elisabetta Boella, Nitin Shukla, Simone Bn\`a, Luca Benini, Andrea bartolini
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
