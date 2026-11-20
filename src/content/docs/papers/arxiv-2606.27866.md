---
title: "FlexMoE: Learning One-for-All Multi-Budget Expert Pruning for Flexible MoE Deployment"
description: "Mixture-of-Experts (MoE) language models scale model capacity through sparse expert activation, yet deployment still requires storing and serving all experts."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.27866) · [PDF](https://arxiv.org/pdf/2606.27866)

## 一句话摘要

Mixture-of-Experts (MoE) language models scale model capacity through sparse expert activation, yet deployment still requires storing and serving all experts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) language models scale model capacity through sparse expert activation, yet deployment still requires storing and serving all experts. Moreover, deployment budgets can vary substantially across devices, users, and workloads. Existing MoE compression methods typically optimize a separate compressed model for each target budget. We introduce FlexMoE, a post-training one-for-all framework that converts a large pretrained MoE model into a multi-budget family of smaller deployable subnetworks. FlexMoE first ranks expert FFN channels by importance to construct a sliceable weight space shared across budgets, and then learns expert-wise discrete retention actions under gradually increasing cost pressure, allowing a single action-training run to produce reliable pruning masks across budgets. Moreover, only a single mid-budget fine-tune can further recover degraded performance and yields a shared recovered model that transfers to other unseen budgets, avoiding repeated per-budget recovery and separated checkpoint storage. Across tested MoE LLMs with diverse architectures and scales, FlexMoE consistently outperforms strong MoE compression baselines. In particular, on Qwen2-57B-A14B, it retains ~99.8% of base performance while pruning 50% of routed-expert parameters even without recovery fine-tuning. For deployment, pruned subnetworks deliver real memory reduction and end-to-end throughput gains, while our kernel co-design enables runtime budget switching without checkpoint reloading and delivers substantial inference acceleration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fan Mo, Yuxuan Han, Geng Zhang, Wangbo Zhao, Yang You
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
