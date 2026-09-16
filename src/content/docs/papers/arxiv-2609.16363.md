---
title: "FSNIC: A Low-Latency Flow-Based Intrusion Detection Architecture for FPGA SmartNICs"
description: "Modern data centres require high-performance networking alongside effective real-time security."
---

**评分：40/100** · AI 基础设施 > 集群与资源系统 > 存储与数据平面

[论文原文](https://arxiv.org/abs/2609.16363) · [PDF](https://arxiv.org/pdf/2609.16363)

## 一句话摘要

Modern data centres require high-performance networking alongside effective real-time security.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern data centres require high-performance networking alongside effective real-time security. Traditional Intrusion Detection Systems (IDS) commonly rely on general-purpose processors and often struggle to inspect high-speed traffic at line rate without introducing latency or performance bottlenecks. Smart Network Interface Cards (NICs) provide an alternative by enabling computation directly within the network data plane. This work presents a machine learning-based IDS implemented within an FPGA-based SmartNIC pipeline. The system integrates P4-based packet parsing with a LogicNets IDS model implemented in RTL, enabling deterministic, low-latency inference. Compared with traditional stateless packet-level classifiers, the proposed stateful flow-based IDS introduces minimal state by aggregating features across packets, capturing behavioural patterns not observable at the packet level. Experimental results on the UNSW-NB15 dataset show that the flow-based IDS improves detection accuracy from 86.92\% to 97.68\% compared with stateless packet-level classification. We also evaluate the proposed IDS on CICIDS2017 and compare its real-time hardware performance with prior FPGA-based IDS designs. Through hardware-software co-design, the proposed IDS achieves 6~ns inference latency using only 846 LUTs, with no BRAM or DSP usage, demonstrating a low latency and resource efficient implementation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: data plane
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nise O'Cuill, Changhong Li, Georgios Floros, Shreejith Shanker
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
