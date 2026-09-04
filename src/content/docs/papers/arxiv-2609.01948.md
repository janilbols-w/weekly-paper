---
title: "An Emerging NVM-Based On-Chip Training Architecture with Non-Ideality Mitigation Through Bipolar Weight Distributions"
description: "The rapid advancement of deep learning has presented significant energy efficiency challenges to the conventional von Neumann architecture."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.01948) · [PDF](https://arxiv.org/pdf/2609.01948)

## 一句话摘要

The rapid advancement of deep learning has presented significant energy efficiency challenges to the conventional von Neumann architecture.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid advancement of deep learning has presented significant energy efficiency challenges to the conventional von Neumann architecture. In-memory computing (IMC) architectures based on emerging non-volatile memory (eNVM) are widely regarded as a promising solution for accelerating neural network training due to their high parallelism and low power consumption. However, the intrinsic non-idealities of eNVM devices can cause conductance updates to deviate from target values, thereby limiting the performance of on-chip training. To address this challenge, this paper presents a Non-ideality Optimized eNVM Accelerator (NOVA) architecture for on-chip training. Specifically, we first fabricate a two-dimensional (2D) ferroelectric field-effect transistor (FeFET) and develop a conductance modulation behavioral model calibrated with experimental data. Building upon this device model, we propose, for the first time, a Non-ideality Avoidance Training (NAT) algorithm tailored for eNVM devices, which mitigates accuracy degradation by guiding weight convergence toward the most stable conductance regions of eNVM devices. Experimental results demonstrate that, even under severe device asymmetry, NAT improves the accuracy by an average of 15.1\% over the baseline methods across multiple benchmark tasks. Meanwhile, the NOVA achieves an average energy efficiency gain of approximately 33.58$\times$ compared with the peak energy efficiency of graphics processing units (GPUs).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Peng Dang, Youna Huang, Yintao He, Huawei Li
- 发布：2026-09-01；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
