---
title: "Constrained Code Generation with Diffusion Language Models"
description: "Diffusion language models (DLMs) are a powerful, emerging paradigm for code generation."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2605.16829) · [PDF](https://arxiv.org/pdf/2605.16829)

## 一句话摘要

Diffusion language models (DLMs) are a powerful, emerging paradigm for code generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (DLMs) are a powerful, emerging paradigm for code generation. They construct programs through iterative refinement of partially corrupted token sequences and enable parallel token refinement. Importantly, this paradigm exposes a global program state at each denoising step, which provides a natural intervention point for enforcing program-level functionality and security constraints, guiding the generation before the final code is committed. Building on this observation, the paper introduces Constrained Diffusion for Code (CDC), an inference-time neurosymbolic framework that integrates constraint satisfaction directly into the reverse denoising process without retraining the base diffusion model. CDC augments the base diffusion sampler with constraint-aware denoising operators that combine mathematical optimization with program analysis to identify constraint-relevant regions of the intermediate program state and locally adjust the denoising trajectory, steering generation toward feasible programs while remaining close to the base model. Across code generation benchmarks, CDC consistently improves constraint satisfaction in functional correctness, security, and even syntax, outperforming diffusion and autoregressive baselines with less corrective computation and more localized edits.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lize Shao, Michael Cardei, Zichen Xie, Ferdinando Fioretto, Wenxi Wang
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
