---
title: "Weaver: A System for AI-RAN Compute Sharing with Foundation Model Training"
description: "The emergence of AI-RAN infrastructure, which equips cell sites with GPU-accelerated hardware, creates an opportunity to colocate non-RAN workloads with primary RAN processing."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](http://arxiv.org/abs/2609.35276v1) · [PDF](https://arxiv.org/pdf/2609.35276v1)

## 一句话摘要

The emergence of AI-RAN infrastructure, which equips cell sites with GPU-accelerated hardware, creates an opportunity to colocate non-RAN workloads with primary RAN processing.

## 为什么值得关注

待编辑增强。

## 摘要原文

The emergence of AI-RAN infrastructure, which equips cell sites with GPU-accelerated hardware, creates an opportunity to colocate non-RAN workloads with primary RAN processing. We explore using this spare capacity for decentralized training of foundation models (FMs), one of the most compute-intensive AI workloads. We present the first characterization of spare GPU capacity in AI-RAN systems at both micro-scale--across transmission slots within a cell site--and macro-scale--across sites. Our analysis finds that 40-85% of GPU capacity is unused; although this capacity is temporally bursty at individual sites, it is spatially complementary across sites. To safely and efficiently harness these resources, we present Weaver, a system that opportunistically trains FMs alongside latency-critical RAN workloads without degrading RAN performance. Weaver adopts a RAN-first design: a spare-compute controller integrated into the MAC scheduler uses compute-aware scheduling to smooth RAN GPU demand and exposes more usable spare GPU capacity. A two-level elastic training framework then adapts to dynamic, heterogeneous spare capacity within and across sites. Experiments on an O-RAN-aligned system prototype show that Weaver creates up to 4.9x more usable spare compute and utilizes up to 83% of the available spare capacity. On a multi-site testbed, Weaver improves training throughput by 2.1-3.7x over baseline approaches.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: elastic training
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Leyang Xue, Tianxin Wang, Xin Zhe Khooi, Jiaxun Yang, Dheeraj Mahendiran, Yufeng Xia, Mun Choon Chan, Myungjin Lee, Mahesh K. Marina
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
