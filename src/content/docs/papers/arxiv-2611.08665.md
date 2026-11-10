---
title: "Dynamic GPU Voxel Grids and Voxel-sequential Processing in NanoVDB"
description: "We introduce two fundamental advances to the NanoVDB data structure: dynamic GPU-native topological updates, and a voxel-sequential access paradigm that dramatically accelerates point-wise and stencil-based operators on sparse grids."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.08665) · [PDF](https://arxiv.org/pdf/2611.08665)

## 一句话摘要

We introduce two fundamental advances to the NanoVDB data structure: dynamic GPU-native topological updates, and a voxel-sequential access paradigm that dramatically accelerates point-wise and stencil-based operators on sparse grids.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce two fundamental advances to the NanoVDB data structure: dynamic GPU-native topological updates, and a voxel-sequential access paradigm that dramatically accelerates point-wise and stencil-based operators on sparse grids. NanoVDB's linearized memory layout has delivered strong GPU performance, and the Index-Grid concept introduced in the fVDB framework [Williams et al 2024] provided topology/data separation and optimal compactness of storage in sparse machine learning workloads. However, all these prior iterations of NanoVDB assume a static topology that has precluded use of this data structure in simulation and dynamic geometric processes. We eliminate this limitation by introducing a suite of dynamic topology operators -- morphological dilation, grid merging, pruning, and cross-resolution coarsening and refinement. These operators use bit-parallel algorithms to reconstruct grids containing hundreds of millions of voxels in just a few milliseconds. We also introduce a voxel-sequential access paradigm and data structure for GPU kernels operating on sparse data. We stream active voxels as a flat linear sequence, minimizing or eliminating the need for tree traversal in the process. This achieves compute density and regularity that allow even complex stencil-based operators to approach peak memory bandwidth, with minimal storage overhead. Together, these contributions remove the read-only constraint from NanoVDB, establishing it as a high-performance primary representation for dynamic GPU simulation and geometry manipulation. We evaluate the efficacy of our newly introduced operators in benchmarks sourced from applications such as 3D reconstruction, fluid simulation, and large-scale mesh voxelization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Eftychios Sifakis, Francis Williams, Christopher Horvath, Rohan Sawhney, Mark Harris, Jonathan Swartz, Ken Museth
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
