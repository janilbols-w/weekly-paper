---
title: "Self-Attention to Operator Learning-based 3D-IC Thermal Simulation"
description: "Thermal management in 3D ICs is increasingly challenging due to higher power densities."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2510.15968) · [PDF](https://arxiv.org/pdf/2510.15968)

## 一句话摘要

Thermal management in 3D ICs is increasingly challenging due to higher power densities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Thermal management in 3D ICs is increasingly challenging due to higher power densities. Traditional PDE-solving-based methods, while accurate, are too slow for iterative design. Machine learning approaches like FNO provide faster alternatives but suffer from high-frequency information loss and high-fidelity data dependency. We introduce Self-Attention U-Net Fourier Neural Operator (SAU-FNO), a novel framework combining self-attention and U-Net with FNO to capture long-range dependencies and model local high-frequency features effectively. Transfer learning is employed to fine-tune low-fidelity data, minimizing the need for extensive high-fidelity datasets and speeding up training. Experiments demonstrate that SAU-FNO achieves state-of-the-art thermal prediction accuracy and provides an 842x speedup over traditional FEM methods, making it an efficient tool for advanced 3D IC thermal simulations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: thermal management
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhen Huang, Hong Wang, Wenkai Yang, Muxi Tang, Depeng Xie, Ting-Jung Lin, Yu Zhang, Wei W. Xing, Lei He
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
