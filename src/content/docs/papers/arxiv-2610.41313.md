---
title: "Migrating a Legacy Scientific Application with an AI Coding Agent: NICAM from Fortran to Kokkos"
description: "Migrating from Fortran to C++/Kokkos broadens access to hardware accelerators through backends such as CUDA and HIP while offering greater flexibility in software design."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.41313) · [PDF](https://arxiv.org/pdf/2610.41313)

## 一句话摘要

Migrating from Fortran to C++/Kokkos broadens access to hardware accelerators through backends such as CUDA and HIP while offering greater flexibility in software design.

## 为什么值得关注

待编辑增强。

## 摘要原文

Migrating from Fortran to C++/Kokkos broadens access to hardware accelerators through backends such as CUDA and HIP while offering greater flexibility in software design. However, legacy Fortran applications often have large codebases, making manual porting time-consuming and costly. Recent advances in large language models (LLMs) and AI coding agents have made large-scale code migration increasingly feasible. In this study, we ported NICAM (Nonhydrostatic ICosahedral Atmospheric Model), a legacy Fortran climate model accelerated with OpenACC, to C++/Kokkos with the assistance of Claude Code. The agent translated the code directly from Fortran to C++/Kokkos under human review. Approximately 140,000 lines of Fortran were analyzed and ported into 35,000 lines of C++/Kokkos, covering the dynamical core and seven physics packages. A 100-member ensemble comparison with the original Fortran model showed that the port is statistically consistent with the original. Performance was evaluated on Miyabi-G, an NVIDIA GH200 cluster, and Sirius, an AMD MI300A cluster. Compared with the Fortran/OpenACC baseline on GH200, the port achieved application speedups of $1.71\times$ on GH200 and $1.54\times$ on MI300A. The CUDA build achieved a GPU kernel-time speedup of $1.38\times$ on GH200. After normalization by peak memory bandwidth, the HIP build on MI300A achieved $0.96\times$ the kernel performance of the Fortran/OpenACC baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xuanzhengbo Ren, Takashi Shimokawabe, Hisashi Yashiro
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
