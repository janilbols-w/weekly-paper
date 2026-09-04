---
title: "LLM Inference on IMC-NoC Architecture with Balanced Dataflow and Fine-Grained Parallelism"
description: "LLM inference has become an essential service, yet it imposes unprecedented demands on memory bandwidth, computational density, and communication efficiency."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.00857) · [PDF](https://arxiv.org/pdf/2609.00857)

## 一句话摘要

LLM inference has become an essential service, yet it imposes unprecedented demands on memory bandwidth, computational density, and communication efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM inference has become an essential service, yet it imposes unprecedented demands on memory bandwidth, computational density, and communication efficiency. While IMC is a promising solution to the memory wall issue, the heterogeneous data dynamicity of LLM requires complementary resources to handle intermediate data generated during run-time. Furthermore, the massive number of parameters in LLM necessitates scale-up architectures where on-chip data movement is often the primary performance bottleneck. This article presents a hardware-software co-design framework that unifies distributed compute, memory, and communication into a seamless processing-communication fabric. On the hardware side, we propose a scalable architecture, named LEAP, that integrates IMC PE, NMC PE, and INC. This allows each hardware layer to execute specialized tasks: IMC for static weights, NMC for dynamic data, and INC for partial result reduction. On the software side, we introduce a partitioning, mapping, and scheduling framework optimized for key metrics in LLM serving, including throughput and latency. To address the distinct computational intensities of the prefill and decode phases, we present a prefill-decode disaggregation approach that dynamically reconfigures PE organizations to maximize resource utilization. Compared to commercial GPU platforms, the proposed architecture provides a throughput and an energy efficiency improvement of $\geq{}1.52\times$ and $24.91\times$, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yimin Wang, Yue Jiet Chong, Xuanyao Fong
- 发布：2026-09-01；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
