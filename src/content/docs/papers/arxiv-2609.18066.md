---
title: "Towards Training Private LLMs: Exploring Fine-Tuning Language Models on Apple Silicon with RDMA over Thunderbolt"
description: "Private large language model (LLM) fine-tuning is increasingly important for organizations that need to adapt models using sensitive data, but it often exceeds the memory capacity of commodity datacenter accelerators."
---

**评分：49/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2609.18066) · [PDF](https://arxiv.org/pdf/2609.18066)

## 一句话摘要

Private large language model (LLM) fine-tuning is increasingly important for organizations that need to adapt models using sensitive data, but it often exceeds the memory capacity of commodity datacenter accelerators.

## 为什么值得关注

待编辑增强。

## 摘要原文

Private large language model (LLM) fine-tuning is increasingly important for organizations that need to adapt models using sensitive data, but it often exceeds the memory capacity of commodity datacenter accelerators. Apple Silicon offers a different design point through large unified memory and lower complete-system cost, while recent Apple software support enables distributed execution over RDMA-over-Thunderbolt (TB). This paper studies whether Apple Silicon can serve as a practical platform for private LLM fine-tuning. We characterize RDMA-over-TB communication on Mac Studio nodes, showing that the measured bandwidth is far below nominal TB specifications. Next, we extend Apple's implementation with multi-trunk communication, persistent worker threads, and CPU-side gradient overlap to better exploit multiple direct TB links for LLM fine-tuning workloads. Finally, on a four-node Mac Studio cluster that fine-tunes a Qwen3-9B, our optimizations improve weak-scaling throughput by up to 1.6X over the single-trunk, non-overlapped baseline and reach 936 tokens/s for sequence length 17408. We further compare Apple Silicon with an NVIDIA H100 platform to quantify the trade-off between memory capacity, throughput, and acquisition cost, showing that Apple Silicon can provide a cost-effective solution for private LLM fine-tuning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: rdma
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：En-Ming Huang, Yao-Ting Hsieh, Hsiang-Yu Tsou, Mu-Chi Chen, Shih-Hao Hung, H. T. Kung
- 发布：2026-09-16；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
