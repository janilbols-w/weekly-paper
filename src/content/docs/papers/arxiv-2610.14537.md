---
title: "Learn the Dynamics, Enforce the Physics: Generative Latent Operators for High-Dimensional Beam Evolution"
description: "Particle-in-cell (PIC) simulation is indispensable for modeling beam dynamics in particle accelerators, but its computational cost limits many-query workflows, such as configuration exploration, virtual diagnostics, and controller design."
---

**评分：39/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](http://arxiv.org/abs/2610.14537v1) · [PDF](https://arxiv.org/pdf/2610.14537v1)

## 一句话摘要

Particle-in-cell (PIC) simulation is indispensable for modeling beam dynamics in particle accelerators, but its computational cost limits many-query workflows, such as configuration exploration, virtual diagnostics, and controller design.

## 为什么值得关注

待编辑增强。

## 摘要原文

Particle-in-cell (PIC) simulation is indispensable for modeling beam dynamics in particle accelerators, but its computational cost limits many-query workflows, such as configuration exploration, virtual diagnostics, and controller design. We introduce GLOBE, a physics-constrained Generative Latent Operator for Beam Evolution, modeling the nonlinear, control-dependent, multiscale evolution of 3D beam--field dynamics covering $10^7$ spatial cells. GLOBE compresses beam--field states into a compact latent space and factors their evolution into two components. A control-conditioned neural operator learns the dominant dynamics, while an amplitude-normalized generative model captures the residual distribution, recovering fine-scale structures and conditional variations. GLOBE enforces field constraints by regime-specific, parameter-free operators: a Poisson solve reconstructs the electric field in the electrostatic regime, and a spectral projection imposes Gauss's law and a divergence-free magnetic field in the electromagnetic regime. On two high-resolution 3D particle-accelerator benchmarks, bunched-beam transport and plasma-wakefield acceleration, GLOBE lowers relative-$L_2$ error by 9\% and 13\%, low-frequency spectral error by 69\% and 51\%, and mid-frequency spectral error by 54\% and 20\% relative to the strongest baseline (DPOT), satisfies field constraints, and reduces hours of PIC simulation to a minute per rollout.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haohan Zou, Alexander Scheinker, Yuanyuan Shi
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
