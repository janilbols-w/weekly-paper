---
title: "Locking Pretrained Weights via Deep Low-Rank Residual Distillation"
description: "The quality of open-weight language models has dramatically improved in recent years."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.10777) · [PDF](https://arxiv.org/pdf/2605.10777)

## 一句话摘要

The quality of open-weight language models has dramatically improved in recent years.

## 为什么值得关注

待编辑增强。

## 摘要原文

The quality of open-weight language models has dramatically improved in recent years. Sharing weights greatly facilitates model adoption by enabling their use across diverse hardware and software platforms. They also allow for more open research and testing, to the extent that users can use them as checkpoints, fine-tune them according to their needs, and potentially redistribute them. In some cases, however, concerns on modifying these weights towards unauthorized uses may outweigh the pros of giving users such freedom. Defending against such adaptation is non-trivial: since an adaptive attacker can observe all weights and architectures by definition, they can reverse simple structural defenses, and use optimization to defeat the simplest locking mechanisms. In this work, we exploit the inference-training asymmetry of automatic differentiation as a novel defense axis. We propose DLR-Lock, a method where the purveyor of the model purposely replaces each pretrained MLP in their model with a deep low-rank residual network (DLR-Net) of comparable parameter count, forcing activation memory that grows linearly with depth during backpropagation. DLR-Nets are efficiently trained via module-wise regression. We show that, beyond this memory overhead, DLR-Lock results in architectural mismatches that complicate the optimization landscape of standard fine-tuning, and a backward pass that incurs disproportionately more overhead than the forward pass. Our defense succeeds in withstanding adaptive attackers with full knowledge of the defense strategy while preserving the original model's capabilities. Experiments on LLMs validate these claims.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Keitaro Sakamoto, Pierre Ablin, Federico Danieli, Marco Cuturi
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
