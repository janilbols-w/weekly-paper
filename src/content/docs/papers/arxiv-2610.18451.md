---
title: "FastEEP: Fast Intra-Instance Elastic Scaling for Expert-Parallel MoE Serving"
description: "Large-scale expert parallelism (EP) has become the standard deployment configuration for Mixture-of-Experts (MoE) models in production."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](http://arxiv.org/abs/2610.18451v1) · [PDF](https://arxiv.org/pdf/2610.18451v1)

## 一句话摘要

Large-scale expert parallelism (EP) has become the standard deployment configuration for Mixture-of-Experts (MoE) models in production.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large-scale expert parallelism (EP) has become the standard deployment configuration for Mixture-of-Experts (MoE) models in production. Meanwhile, the highly dynamic nature of LLM workloads requires providers to continuously adjust serving capacity to match fluctuating demand. Scaling MoE serving cannot be efficiently achieved by simply adding or removing serving instances; instead, it often requires resizing the EP group within an existing instance, which we refer to as intra-instance scaling.Existing inference engines primarily rely on instance-level scaling, which destroys and reconstructs entire serving instances, incurring substantial scaling overhead. We present FastEEP (Fast Elastic Expert Parallel), a fast intra-instance scaling system for MoE serving based on the principle of Partial Reuse. FastEEP reuses existing runtime state across worker execution, GPU memory, and communication by separating reusable execution structures from the resources activated by the current EP configuration. This separation enables coordinated resource reclamation and reconfiguration while preserving costly-to-reconstruct state, allowing fast EP scaling without full instance teardown and reconstruction. Our evaluation shows that FastEEP achieves 4.5x--11.7x faster scaling than the existing vLLM-based approach across different models, enabling efficient, fine-grained scaling of MoE serving.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yunfei Feng, Jingkai He, Shiqi Liu, Cheng Zhang, Dong Du, Erhu Feng
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
