---
title: "A 420 GOPS/W CGRA with a Configurable MAC and Dynamic Truncation"
description: "Edge devices demand for highly efficient yet flexible processing capability to handle dynamic real-time workloads."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.16600) · [PDF](https://arxiv.org/pdf/2609.16600)

## 一句话摘要

Edge devices demand for highly efficient yet flexible processing capability to handle dynamic real-time workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge devices demand for highly efficient yet flexible processing capability to handle dynamic real-time workloads. Coarse grain reconfigurable architecture (CGRA) emerges as a suitable accelerator candidate in edge devices, because they are as flexible as general purpose processors and offer high efficiency close to that of domain specific accelerators. However, a typical CGRA requires two cycles for a multiply-and-accumulate (MAC) operation, and workloads such as neural network inference and signal processing involve many MAC operations, resulting in long CGRA processing time. This work proposes a CGRA that has configurable MAC units in the processing elements (PEs) that can perform an addition (ADD) or multiplication (MUL) or a MAC by using the same multiplier and adder, in a single cycle. The readout precision of MAC result can be adjusted by a truncation block. The proposed CGRA is implemented with 40nm CMOS technology. It attains an energy efficiency of 420.6GOPS/W operating at supply of 0.6V and frequency of 21MHz, which is 1.4 times higher than the state-of-the-art.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yi Sheng Chong, Rakshith Harish, Rajesh Chandrasekhara Panicker, Vishnu P. Nambiar, Anh Tuan Do
- 发布：2026-09-15；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
