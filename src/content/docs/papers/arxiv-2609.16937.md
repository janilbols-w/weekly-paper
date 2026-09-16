---
title: "Beyond Token-Local Imitation: Reward-Compatible Temporal Credit Assignment for On-Policy Distillation"
description: "On-policy distillation (OPD) has emerged as an effective approach for large language model post-training, yet existing objectives face a trade-off between objective fidelity and optimization stability."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.16937) · [PDF](https://arxiv.org/pdf/2609.16937)

## 一句话摘要

On-policy distillation (OPD) has emerged as an effective approach for large language model post-training, yet existing objectives face a trade-off between objective fidelity and optimization stability.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) has emerged as an effective approach for large language model post-training, yet existing objectives face a trade-off between objective fidelity and optimization stability. Token-level OPD provides stable but local supervision, whereas sequence-level OPD captures future credit at the cost of horizon-dependent variance. We establish a unified temporal-credit view of these formulations, showing that practical token-level OPD can be interpreted as a temporal approximation to the sequence-level reverse-KL gradient. Building on this connection, we propose $\gamma$OPD, which uses discounted temporal credit assignment to balance long-horizon supervision and optimization stability, while admitting a horizon-independent variance bound. We further develop a reward-compatible bounded mixing (RBM) mechanism for $\gamma\mathrm{OPD}$ that balances verifiable outcome feedback with the discounted OPD advantage to move beyond purely teacher-dependent optimization. Experiments on mathematical and code reasoning demonstrate consistent improvements over existing OPD methods across vanilla, size-mismatched, and multi-teacher distillation settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shiqi Liu, Zeyu He, Letian Tao, Guojian Zhan, Jiaxin Gao, Feihong Zhang, Jingliang Duan, Wei Xiong, Kehua Sheng, Bo Zhang, Yang Guan, Shengbo Eben Li
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
