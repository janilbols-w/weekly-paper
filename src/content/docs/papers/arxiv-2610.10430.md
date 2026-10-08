---
title: "Conditional Flow Matching for Generation of 3D Multi-variable Instantaneous Urban Microclimate Fields"
description: "Rapid and accurate prediction of urban wind and temperature fields is important for urban microclimate design and climate adaptation."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.10430) · [PDF](https://arxiv.org/pdf/2610.10430)

## 一句话摘要

Rapid and accurate prediction of urban wind and temperature fields is important for urban microclimate design and climate adaptation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Rapid and accurate prediction of urban wind and temperature fields is important for urban microclimate design and climate adaptation. Large-eddy simulation (LES) effectively resolves these instantaneous fields, but its application is limited in iterative design of urban microclimate applications due to high computational cost. Existing regressive data-driven models offers quick outputs, but they produce only deterministic point predictions that inherently fail to represent turbulent stochasticity. This paper adopts a novel generative framework of Conditional Flow Matching (CFM) that uses building geometry and mean flow as guidance to generate plausible three-dimensional instantaneous velocity and temperature fields for urban microclimate in seconds. To overcome the GPU memory bottleneck of pixel space 3D generation, the model operates in parallel on overlapping pixel space through a shared-noise initialization that preserves high spatial continuity of flow structure across the entire domain. Against reference LES data, the CFM surrogate can rapidly and accurately restore the first-order statistics with Normalized Root Mean Square Error (NRMSE) of 2.99% for wind and 1.77% for temperature, second-order turbulence metrics with NRMSE of 7.17% for wind and 8.84% for temperature, turbulent kinetic energy with NRMSE of 7%, probability density function and vertical profiles in representative locations. Wind engineering application of local gust prediction demonstrate that the speed and accuracy of CFM, supporting the use of generative AI for making turbulence-aware resilient urban design and climate adaptation more computationally feasible.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Peng Liu, Shaoxiang Qin, Theodore Potsis, Lili Ji, Dingyang Geng, Liangzhu Leon Wang
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
