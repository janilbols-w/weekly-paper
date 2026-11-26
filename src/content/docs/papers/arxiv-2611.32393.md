---
title: "Fractal Neural Synthesis: Constant-Storage Procedural Weight Derivation via Complex Quadratic Boundary Dynamics"
description: "Conventional neural networks store synaptic parameters as explicit tensors whose persistent Flash footprint scales linearly (O(W)) with parameter count, constraining resource-limited edge microcontrollers."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.32393) · [PDF](https://arxiv.org/pdf/2611.32393)

## 一句话摘要

Conventional neural networks store synaptic parameters as explicit tensors whose persistent Flash footprint scales linearly (O(W)) with parameter count, constraining resource-limited edge microcontrollers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Conventional neural networks store synaptic parameters as explicit tensors whose persistent Flash footprint scales linearly (O(W)) with parameter count, constraining resource-limited edge microcontrollers. We formulate and systematically evaluate Fractal Neural Synthesis (FNS), a procedural weight derivation architecture that replaces hidden-layer matrices with a constant 24-byte coordinate seed Theta = (c_x, c_y, ell) in F_64^3 anchored near the complex quadratic bifurcation boundary dM of f_c(z) = z^2 + c. We introduce a large-bailout (R = 256) smooth escape kernel, four zero-overhead geometric sampling apertures--Cartesian Grid, coprime 3x3 Rule-of-Thirds (Z/9Z), phi-Vogel spiral, and multi-scale Harmonic Tripod--and prove conditional Kolmogorov (K_Kolm <= 192 + c_0 bits) and Shannon entropy bounds. Across magnifications zeta in [10^0, 10^8], C^1 Fourier and lattice-noise bases collapse to post-standardization rank ~2.25 and SHA-256 PRNG exhibits avalanche discontinuity (rho ~ 0.019, 50.6% micro-step retention), whereas dM uniquely sustains both rank (~10.0) and local continuity (rho in [0.81, 0.97], 89.2% retention). Under leak-free 10-fold CV across four zero-scaler-byte non-linear benchmarks, FNS with an INT8 readout surpasses 0-hidden Linear-INT8 by +3.6 to +10.8 pp while delivering 10.7x-129x total Flash reduction (725x-2,773x hidden reduction) relative to converged Float32 MLPs (90.30% Ionosphere in 285 B; 97.22% Optical Digits in 2,598 B; 97.90% PenDigits in 2,598 B; 87.00% Satimage in 1,570 B).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Volkan Dagli, Zerrin Dagli, Daghan Dagli
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
