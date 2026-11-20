---
title: "FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash"
description: "Embodied agents are emerging as a promising paradigm for complex robotic tasks, leveraging Vision-Language-Action (VLA) and World Action Models (WAMs) to generate actions through Diffusion Transformer (DiT)-based iterative denoising."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](http://arxiv.org/abs/2611.25580v1) · [PDF](https://arxiv.org/pdf/2611.25580v1)

## 一句话摘要

Embodied agents are emerging as a promising paradigm for complex robotic tasks, leveraging Vision-Language-Action (VLA) and World Action Models (WAMs) to generate actions through Diffusion Transformer (DiT)-based iterative denoising.

## 为什么值得关注

待编辑增强。

## 摘要原文

Embodied agents are emerging as a promising paradigm for complex robotic tasks, leveraging Vision-Language-Action (VLA) and World Action Models (WAMs) to generate actions through Diffusion Transformer (DiT)-based iterative denoising. However, existing models often struggle to generalize to out-of-distribution (OOD) environments. We observe that retrieving successful experiences and using them to warm-start denoising enables agents to better adapt to unfamiliar situations while reducing computational overhead. This creates a new opportunity to improve task accuracy and inference efficiency simultaneously, in contrast to conventional acceleration techniques that trade accuracy for computation. However, realizing this opportunity requires scaling experience banks, introducing substantial storage and search overhead that challenges the capacity, bandwidth, and power constraints of edge systems. We propose FlashX, a CMOS Directly Bonded to Array (CBA)-based NAND flash architecture for scalable experience reuse in embodied agents. FlashX exploits CBA's high internal bandwidth for parallel pSLC key search, employing interleaved Compute-in-Flash (CIF) engines to sustain sensing throughput while retaining dense TLC latent storage. Proprioception-aware clustering further reduces search overhead and enables incremental experience acquisition without global reclustering. Evaluations across VLA and WAM workloads demonstrate up to 12.24\%p and 7.43\%p improvements in task success under dense and compute-efficient configurations, respectively. FlashX achieves 2.57$\times$ higher search throughput than the strongest prior NAND search architecture under pSLC sensing, with a further 9.7$\times$ search reduction through clustering. This delivers 1.29--3.95$\times$ end-to-end speedup and 1.12--2.34$\times$ energy efficiency improvement over SSD-based retrieval.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuseon Choi, Sanghyeon Park, Eunjong Lee, Hanseo Lee, Sangjin Kim
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
