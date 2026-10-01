---
title: "dattri-LLM: A Unified and Efficient Library for Training Data Attribution at LLM Scale"
description: "Training data attribution (TDA) estimates the contribution of individual training examples to model outputs."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.38767) · [PDF](https://arxiv.org/pdf/2609.38767)

## 一句话摘要

Training data attribution (TDA) estimates the contribution of individual training examples to model outputs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training data attribution (TDA) estimates the contribution of individual training examples to model outputs. Most scalable TDA methods rely on per-example gradients, whose computation and use at LLM scale pose challenges in efficiency, compatibility, and extensibility. We introduce dattri-LLM, a TDA library that makes gradient-based attribution more practical at scale. For efficiency, dattri-LLM uses compact gradient representations and dynamically routes gradient operations based on a cost model. For compatibility, its capture mechanism collects per-example gradients from existing training loops that call backward(), without requiring changes to the loop or its configuration. This includes distributed training with DDP and FSDP and pipelines built with HuggingFace Transformers, TRL, and OLMo. For extensibility, dattri-LLM exposes reusable gradient operations and training-time callbacks for implementing attribution methods and applications. These interfaces support a variety of attribution methods, including gradient similarity, curvature-based influence, and trajectory-based methods, as well as applications that act on gradients during training, such as online data selection. On the same hardware and workload, dattri-LLM achieves 3.2x the throughput of the fastest competing library on average, scales multiple attribution methods to 110B-parameter models across four H200 GPUs, and offers superior attribution fidelity-cost trade-offs across a range of models with different model families and scales.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Shixuan Liu, Tongli Zhou, Junwei Deng, Pingbang Hu, Jiaqi W. Ma
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
