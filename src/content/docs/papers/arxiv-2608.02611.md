---
title: "KernelBrain: Coarse-to-Fine, Budget-Aware Search for Agentic GPU Kernel Optimization"
description: "Automating GPU kernel optimization remains difficult in practice: generated variants can violate correctness constraints, runtime measurements are noisy, and search often stalls early."
---

**评分：54/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2608.02611) · [PDF](https://arxiv.org/pdf/2608.02611)

## 一句话摘要

Automating GPU kernel optimization remains difficult in practice: generated variants can violate correctness constraints, runtime measurements are noisy, and search often stalls early.

## 为什么值得关注

待编辑增强。

## 摘要原文

Automating GPU kernel optimization remains difficult in practice: generated variants can violate correctness constraints, runtime measurements are noisy, and search often stalls early. We present a practical optimization agent that combines LLM-guided mutation, adaptive resource allocation, policy-gated evaluation, and profiler-informed diagnosis. The system screens many candidates with low-cost evaluation and allocates higher-fidelity budget only to promising survivors to optimize and evolve GPU kernels. On important Triton kernel generation tasks, this design improves both kernel quality and search efficiency, reaching 0.88x-6.72x speedup over PyTorch and up to 1.4x speedup over the state-of-the-art kernel agent, with up to 48% lower optimization time.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 25 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel generation, kernel optimization, triton kernel
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Shuai Che, Gang Peng
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
