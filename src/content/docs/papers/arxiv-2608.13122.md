---
title: "Validation-Centric AI-Assisted GPU Porting of a 250,000+ Line Legacy Weather Simulation Code"
description: "Recent advances in large language models have made CLI-based AI agents a practical tool for accelerating GPU porting of large legacy scientific applications."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.13122) · [PDF](https://arxiv.org/pdf/2608.13122)

## 一句话摘要

Recent advances in large language models have made CLI-based AI agents a practical tool for accelerating GPU porting of large legacy scientific applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in large language models have made CLI-based AI agents a practical tool for accelerating GPU porting of large legacy scientific applications. Such applications, however, are not merely old code bases; they are scientific assets whose credibility has been accumulated through long-term development, comparison with observations, and use in domain studies. GPU porting must therefore preserve this scientific validity while adapting the implementation to GPU-centric HPC systems. This paper presents a validation-centric AI-assisted GPU porting workflow through a case study of CReSS, a legacy Fortran weather simulation code with more than 250,000 lines. The workflow uses an AI agent to extract OpenMP regions, generate dump-based kernel benchmarks from physically meaningful simulation states, apply OpenACC transformations, and validate results through element-wise comparison with dumped reference data and application-level validation. Using a real typhoon simulation, the workflow produced numerically validated GPU implementations for 162 target kernels and achieved a 5.1x application-level speedup within practical wall-clock development cost. In particular, it detected numerical discrepancies in five kernels caused by floating-point and intrinsic-function differences, including threshold-sensitive branch divergence and cancellation effects, enabling feedback to the application developers. The case study suggests that, for large legacy scientific applications requiring dump-based validation, practical AI-assisted GPU porting must manage session-spanning context, runtime-state reconstruction, and costly recovery from small static-analysis omissions. These findings demonstrate that AI-assisted GPU porting requires not only code generation, but validation-centric workflow design.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tetsuya Hoshino, Masaya Kato, Kazuhisa Tsuboki, Daichi Mukunoki, Takahiro Katagiri, Toshihiro Hanawa
- 发布：2026-08-13；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
