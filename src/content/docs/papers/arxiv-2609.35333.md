---
title: "Scalable In-Context Reinforcement Learning with Recurrent Algorithm Distillation"
description: "Algorithm Distillation (AD) has demonstrated the remarkable ability of Transformers to perform in-context reinforcement learning without explicit weight updates."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.35333) · [PDF](https://arxiv.org/pdf/2609.35333)

## 一句话摘要

Algorithm Distillation (AD) has demonstrated the remarkable ability of Transformers to perform in-context reinforcement learning without explicit weight updates.

## 为什么值得关注

待编辑增强。

## 摘要原文

Algorithm Distillation (AD) has demonstrated the remarkable ability of Transformers to perform in-context reinforcement learning without explicit weight updates. However, capturing long-term learning progress necessitates expansive context windows, which incur prohibitive memory costs and limit scalability in complex, long-horizon tasks. To address this bottleneck, we propose Recurrent Algorithm Distillation (RAD). RAD employs a dual-component architecture: a Compression Transformer that distills extended interaction histories into compact latent tokens, and an AD Transformer that auto-regressively generates actions using a hybrid context of these compressed memories and recent transitions. By maintaining a fixed-size latent buffer, RAD decouples the effective history length from computational complexity, functionally providing the model with a long-horizon memory. Empirical evaluations across diverse environments demonstrate that RAD matches the asymptotic performance of standard AD with significantly reduced context window sizes, offering a scalable solution for efficient in-context decision-making.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuanqing Ma, Zhenrui Zheng, Chenjun Xiao
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
