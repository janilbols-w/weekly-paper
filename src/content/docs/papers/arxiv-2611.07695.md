---
title: "Equivariant Deep Learning in Direct-Product Space for Electronic-Structure Hamiltonian Prediction"
description: "Most existing equivariant architectures for Hamiltonian prediction propagate features in direct-sum spaces of irreducible spherical tensors, whereas the target Hamiltonian is naturally an operator block in a direct-product representation over local orbital and spin bases."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.07695) · [PDF](https://arxiv.org/pdf/2611.07695)

## 一句话摘要

Most existing equivariant architectures for Hamiltonian prediction propagate features in direct-sum spaces of irreducible spherical tensors, whereas the target Hamiltonian is naturally an operator block in a direct-product representation over local orbital and spin bases.

## 为什么值得关注

待编辑增强。

## 摘要原文

Most existing equivariant architectures for Hamiltonian prediction propagate features in direct-sum spaces of irreducible spherical tensors, whereas the target Hamiltonian is naturally an operator block in a direct-product representation over local orbital and spin bases. This representation mismatch fragments contiguous Hamiltonian blocks, obscures direct manipulation of orbital couplings, and organizes features into irregular angular-momentum components that require numerous transformations and are poorly aligned with efficient hardware execution and memory management. To address both the representation mismatch and computational bottleneck, we propose DP-Learner, an equivariant learning framework that performs message passing directly on Hamiltonian-like operator blocks in the direct-product space. Theoretically, we propose Lie-generator-based directional embedding and invariantly weighted left--right products and contractions that preserve equivariance to SO(3), SU(2), and spatial inversions, without explicit Clebsch--Gordan decomposition or inverse reconstruction. Methodologically, we instantiate this principle as a Transformer architecture, in which Hamiltonian-like feature matrices or tensors evolve through equivariant operators in the direct-product space, while non-linear invariant scalar routing controls structured gating over matrix units, directional propagation, attention, and environment-embedded context interactions. We further construct MP-HAM-110K, a large-scale Hamiltonian dataset comprising more than 110,000 material structures covering 68 elements with both Hamiltonian and wavefunction data. Experiments on MP-HAM-110K and Materials-HAM-SOC demonstrate that DP-Learner dramatically improves Hamiltonian prediction accuracy and inference efficiency over the state-of-the-art method.

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

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shi Yin, Zujian Dai, Xinyang Pan, Lixin He
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
