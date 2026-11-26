---
title: "LoopPrune: Recurrent Pruning for Looped Diffusion Transformers"
description: "Looped diffusion Transformers reuse shared blocks to deepen computation and match larger models with fewer parameters, reducing storage and deployment burdens."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.22757) · [PDF](https://arxiv.org/pdf/2611.22757)

## 一句话摘要

Looped diffusion Transformers reuse shared blocks to deepen computation and match larger models with fewer parameters, reducing storage and deployment burdens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped diffusion Transformers reuse shared blocks to deepen computation and match larger models with fewer parameters, reducing storage and deployment burdens. Yet repeated attention and MLP computations remain costly. Pruning reduces storage and computation by removing redundant parameters or units. Training-free methods struggle to resolve recurrent contributions, while training-based methods lack explicit constraints on position-specific errors affecting later inputs and final outputs. We propose LoopPrune, a pruning and recovery framework addressing these requirements. Recurrent importance estimation combines shared-removal effects and position variation to select a shared structure; shared reconstruction pools recurrent input statistics to compensate weights. Loop-position recovery compares complete denoising predictions at identical student states and matches text guidance, updating all student parameters against a fixed dense teacher. Extensive experiments across four open-source models, six benchmarks, and three pruning paradigms demonstrate effectiveness. At 30% structured parameter pruning, Looped-DiT B/16 retains 93.14% of dense six-benchmark average accuracy, exceeding the best baseline by 9.49%. Across PyTorch, vLLM-Omni, and SGLang Diffusion, pruned SDXSv3 reduces peak allocated GPU memory by 34.36-44.64% and accelerates denoising 1.46-1.74x over dense models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Weizhong Huang, Huaijia Kou, Yan Zhang, Fei Chao, Xiawu Zheng, Liujuan Cao
- 发布：2026-11-17；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
