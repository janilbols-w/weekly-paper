---
title: "Dissecting an Unexplored SASS Control-Code Field: Barrier Exemption and Programmable Warp Priority"
description: "Every instruction in NVIDIA's native GPU ISA (SASS) carries a control code that guides hardware scheduling, and prior work has decoded its known fields to optimize GPU kernels."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2611.24437) · [PDF](https://arxiv.org/pdf/2611.24437)

## 一句话摘要

Every instruction in NVIDIA's native GPU ISA (SASS) carries a control code that guides hardware scheduling, and prior work has decoded its known fields to optimize GPU kernels.

## 为什么值得关注

待编辑增强。

## 摘要原文

Every instruction in NVIDIA's native GPU ISA (SASS) carries a control code that guides hardware scheduling, and prior work has decoded its known fields to optimize GPU kernels. However, one control-code field remains unexplored: it appears over 500000 times in NVIDIA's closed-source libraries such as cuBLAS and cuDNN, yet nvcc never emits it when compiling user programs. This paper presents the first systematic study of this control-code field across GPU architectures from Volta to Blackwell. Using instruction-level microbenchmarks, we show that the field controls two independent hardware mechanisms: barrier exemption (EXEMPT), which allows instructions blocked by a pending barrier to issue early during the barrier wait, and programmable warp priority (START, TILE, and END), which moves warps across three priority levels in the hardware scheduler. We identify the conditions under which each mechanism improves GPU kernel performance and implement a post-compilation binary optimizer that places these marks directly in compiled binaries without modifying source code or the compiler. Evaluated across six GPUs spanning four architectures, our optimizations speed up representative kernels by up to 31.9%, and the optimizer accelerates production kernels in llama.cpp and vLLM by up to 5.4% and end-to-end LLM inference by up to 3.6%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ziwen Wang, Qi Luo, Kunlin Li, Changxi Liu, Dongsheng Wang, Yun Chen
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
