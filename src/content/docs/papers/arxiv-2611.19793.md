---
title: "IANN: A Unified Framework for Equivariant InterAtomic Neural Networks with User-Friendly Implementation"
description: "Machine-learning interatomic potentials (MLIPs) now approach density functional theory (DFT) accuracy at a fraction of its cost, but the practical benefit is limited by software fragmentation: each state-of-the-art architecture is released as a separate codebase, with its own data format, configuration system, training loop and molecular-dynamics interface."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.19793) · [PDF](https://arxiv.org/pdf/2611.19793)

## 一句话摘要

Machine-learning interatomic potentials (MLIPs) now approach density functional theory (DFT) accuracy at a fraction of its cost, but the practical benefit is limited by software fragmentation: each state-of-the-art architecture is released as a separate codebase, with its own data format, configuration system, training loop and molecular-dynamics interface.

## 为什么值得关注

待编辑增强。

## 摘要原文

Machine-learning interatomic potentials (MLIPs) now approach density functional theory (DFT) accuracy at a fraction of its cost, but the practical benefit is limited by software fragmentation: each state-of-the-art architecture is released as a separate codebase, with its own data format, configuration system, training loop and molecular-dynamics interface. Comparing two architectures on the same dataset, or moving a trained model into a production simulation, therefore requires substantial re-engineering. We introduce IANN (InterAtomic Neural Network), an open-source PyTorch framework that reimplements equivariant graph neural networks - PaiNN, NequIP, MACE, Allegro, EquiformerV2, EquiformerV3 and UMA - behind a unified data object, a unified trainer and a single deployment route, so that the architecture is a one-word change in a configuration dictionary. Forces, stresses and virials are obtained for every architecture from one analytic differentiation of the energy with respect to the edge vectors of the atomic graph, exact under periodic boundary conditions. Distributed training is configured automatically from the SLURM, PBS or MPI environment, so the same script runs unchanged from a workstation to a multi-node GPU allocation. Self-describing checkpoints serve directly as ASE calculators, as ensembles reporting uncertainties, or as TorchScript models run inside LAMMPS through bundled C++ pair styles with single- and multi-GPU inference. Trained on a common dataset of millions of structures, the architectures can be compared under identical conditions. We further release PaiNN foundation models trained on 41.9 million curated DFT structures from MPtrj, Alexandria, OMat24, MatPES, OC20, OC22, OC25, MPr2SCAN and MatPESr2SCAN, spanning the PBE, RPBE and r2SCAN functionals. Additionally, IANN provides an agent interface to facilitate integration with autonomous agents.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Changzhi Ai, Xueping Qin, Dimosthenis Sokaras, Frank Abild-Pedersen, Johannes Voss
- 发布：2026-11-15；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/changzhiai/IANN](https://github.com/changzhiai/IANN)
- 阅读深度：metadata
