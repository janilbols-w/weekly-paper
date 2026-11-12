---
title: "Understanding Mixture-of-Experts Language Models Beyond Expert Boundaries"
description: "In Mixture-of-Experts (MoE) models, the nature of expert specialization remains controversial."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.13975) · [PDF](https://arxiv.org/pdf/2611.13975)

## 一句话摘要

In Mixture-of-Experts (MoE) models, the nature of expert specialization remains controversial.

## 为什么值得关注

待编辑增强。

## 摘要原文

In Mixture-of-Experts (MoE) models, the nature of expert specialization remains controversial. Reports of domain-associated expert preferences contrast with analyses attributing routing primarily to token identity or syntactic patterns. To clarify these differing accounts, we look beyond expert-level routing to investigate the neuron-level organization of domain-specialized computation using Routing-Aware Magnitude Profiling (RAMP), a measure developed for this analysis. Using mixed-domain calibration data, we identify domain-specialized neuron sets with 58-74% overlap across multi-source samples of the same domain, compared with 15-24% across domains. To understand how this organization evolves during training, we trace neuron importance throughout pre-training and post-training across three fully open MoE families. Neuron importance continues to reorganize between pre-training checkpoints despite comparatively stable expert-level importance rankings, while post-training largely preserves neuron rankings. Building on these neuron-level perspectives, we further introduce RAMP-based Pruning (RAMPr) to select neurons across experts for balanced multi-domain capability preservation. At 75% neuron retention, RAMPr preserves average 91-98% of original full performance across six models. At 50% retention, our pruning method can reduce resident GPU memory by 36-43% and improves batched prefill throughput by 17-39% effectively. Our code is available at https://github.com/ydyjya/Neuron-Level-Specialization-in-MoE

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhenhong Zhou, Mao Zheng, Mingyang Song, Qiankun Li, Kun Wang, Junfeng Fang
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ydyjya/Neuron-Level-Specialization-in-MoE](https://github.com/ydyjya/Neuron-Level-Specialization-in-MoE)
- 阅读深度：metadata
