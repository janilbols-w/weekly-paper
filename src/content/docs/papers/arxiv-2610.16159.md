---
title: "LizTail: Unifying Shape Adaptation and Spatial Parallelism with Segment-Reconfigurable Systolic Arrays"
description: "Systolic arrays are widely used to accelerate neural-network inference, yet fixed two-dimensional arrays struggle with the substantial diversity in both matrix geometry and available parallelism across CNNs and Transformer-based large language models."
---

**评分：43/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](http://arxiv.org/abs/2610.16159v1) · [PDF](https://arxiv.org/pdf/2610.16159v1)

## 一句话摘要

Systolic arrays are widely used to accelerate neural-network inference, yet fixed two-dimensional arrays struggle with the substantial diversity in both matrix geometry and available parallelism across CNNs and Transformer-based large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Systolic arrays are widely used to accelerate neural-network inference, yet fixed two-dimensional arrays struggle with the substantial diversity in both matrix geometry and available parallelism across CNNs and Transformer-based large language models. This mismatch is particularly severe for skinny matrices, small-batch autoregressive decoding, and operators containing multiple independent partitions, leading to low processing-element (PE) utilization and repeated spatial folding. Existing reconfigurable arrays typically improve either shape adaptation or distributed execution, whereas supporting both through fine-grained routing incurs considerable interconnect, buffering, and control overheads. We present LizTail (named after lizard tail autotomy, where predefined fracture planes allow segments to detach and remain independently active, analogous to LizTail's predefined reconfiguration boundaries), a multi-mode systolic array that enables constrained segment-level reconfiguration by partitioning a $128\times128$ array into 32 regular $128\times4$ segments and adding connectivity only at predefined endpoints. The resulting substrate supports trimming, long-path extension through $180^\circ$ turn-back connections, and distributed execution in which each subarray can itself be trimmed or extended. Differentiated PE datapaths and segment-aware CEB/SIB buffers provide the required compute and data-delivery flexibility without unrestricted PE-level routing. A hardware-constrained mapper selects the execution organization, dataflow, task partition, and tiling. Across representative workloads, LizTail achieves geometric-mean speedups of $5.02\times$ on CNN inference and $25.67\times$ on LLM decoding over a TPU-like array, while reducing EDP by up to $38.23\times$. LizTail is open-sourced at https://github.com/kmjbwxa/LizTail.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Gang Liu, Chen Yang, Junyan Hu, Jianguo Chen, Lixin Duan
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/kmjbwxa/LizTail](https://github.com/kmjbwxa/LizTail)
- 阅读深度：metadata
