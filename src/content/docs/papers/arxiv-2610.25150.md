---
title: "Learning without Overwriting: Structural Knowledge Fusion for Continual Learning"
description: "Catastrophic forgetting in sequential deep learning arises from a fixed-capacity architectural constraint: parameter updates encoding new tasks perturb weight subspaces supporting prior representations."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.25150) · [PDF](https://arxiv.org/pdf/2610.25150)

## 一句话摘要

Catastrophic forgetting in sequential deep learning arises from a fixed-capacity architectural constraint: parameter updates encoding new tasks perturb weight subspaces supporting prior representations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Catastrophic forgetting in sequential deep learning arises from a fixed-capacity architectural constraint: parameter updates encoding new tasks perturb weight subspaces supporting prior representations. We introduce the Knowledge Fusion Network (KFN), which mitigates the stability-plasticity trade-off in class-incremental learning through novelty-gated structural expansion rather than parameter negotiation within a shared capacity budget. KFN decouples task acquisition from knowledge consolidation: each incoming task is learned in an isolated lightweight specialist network (2.8M parameters) and integrated into the global model via a Structural Fusion Module that allocates dedicated channel capacity conditioned on a quantitative novelty score. Dual structural isolation--channel-space separation with temporally phased gradient unfreezing--protects consolidated knowledge. On ten-task Split CIFAR-100, KFN achieves 11.94% minimum task accuracy and 71.16% task-10 accuracy, whereas shared-parameter baselines degrade severely: LwF to 9.07% average accuracy (0.00% min), Replay++ to 8.91% (85.08% forgetting), and Replay to 16.21% (73.44% forgetting); KFN's forgetting (57.92%) is 15.5 pp lower than Replay. Furthermore, KFN prevents logit-scale drift, maintaining near-symmetric task performance. Across CIFAR-100 and EuroSAT satellite imagery, KFN's class-incremental retention (72.7% and 42.5%) substantially exceeds the best baselines (29.6% and 0.94%). Crucially, KFN achieves parameter-efficient linear scaling, adding 25% of the base parameter count per step and requiring 25.1% of naive backbone duplication over ten tasks (28.1M vs 112.0M). With a 37.1% peak GPU memory reduction over full retraining, KFN establishes novelty-gated expansion as a practical path beyond fixed-capacity architectures.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kanishk Bakshi, Amitansu Pattanaik, Kathiravan Srinivasan
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
