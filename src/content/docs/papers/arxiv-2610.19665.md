---
title: "ESL-former: Event Sparse Linear Transformer for FPGA-Accelerated Malware Detection"
description: "Transformer based intrusion detection has shown strong potential for identifying unknown malware variants, but its deployment on resource constrained edge devices remains difficult due to the high computational and memory cost of self attention."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.19665) · [PDF](https://arxiv.org/pdf/2610.19665)

## 一句话摘要

Transformer based intrusion detection has shown strong potential for identifying unknown malware variants, but its deployment on resource constrained edge devices remains difficult due to the high computational and memory cost of self attention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer based intrusion detection has shown strong potential for identifying unknown malware variants, but its deployment on resource constrained edge devices remains difficult due to the high computational and memory cost of self attention. This paper presents an event sparse Linear Transformer framework for malware detection on FPGA edge platforms. Instead of relying on an explicit attention matrix, the proposed method derives token and channel importance directly from the accumulated key value state of Linear Transformer. A contribution aware scoring function is introduced to measure the perturbation of each token or kernel channel to the linear attention state, allowing redundant tokens and low contribution channels to be removed without constructing quadratic attention maps. To translate sparsity into practical hardware acceleration, the proposed design further replaces conventional binary mask based execution with a Top K active token buffer and a hardware compaction unit. The selected active tokens and channels are reorganized into dense fixed length data streams, enabling downstream processing elements to execute regular multiply accumulate operations with reduced redundant memory access and control overhead. This design is suitable for low power FPGA based malware detection, where both latency and on chip resource usage are critical. Experimental evaluation demonstrates that the proposed sparse Linear Transformer can reduce hardware cost while preserving malware classification accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jun Yang, Yumeng Cao, Yingxuan Xiao, Changhong Li, Shangru Zhou
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
