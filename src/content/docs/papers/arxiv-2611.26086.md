---
title: "ScaleWire: An End-to-End Scale-Up Ethernet Simulation Framework for LLM Systems"
description: "LLM training and inference rely on scale-up networks for high-bandwidth, low-latency memory-semantic communication among accelerators (XPUs)."
---

**评分：44/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](http://arxiv.org/abs/2611.26086v1) · [PDF](https://arxiv.org/pdf/2611.26086v1)

## 一句话摘要

LLM training and inference rely on scale-up networks for high-bandwidth, low-latency memory-semantic communication among accelerators (XPUs).

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM training and inference rely on scale-up networks for high-bandwidth, low-latency memory-semantic communication among accelerators (XPUs). Ethernet is emerging as an open interconnect for scale-up systems. In Ethernet systems, network-interface (NI) mechanisms across transport, network, and link layers interact, jointly shaping communication performance and on-chip resource requirements. We present ScaleWire, an end-to-end scale-up Ethernet simulation framework for LLM systems. It couples packet-level simulation of cross-layer NI mechanisms with a resource exploration engine that combines analytical estimates and simulation to size on-chip resources. We validate ScaleWire against hardware measurements and nine analytical checks, and evaluate six NI designs across four LLM communication workloads. For DeepSeek-R1 dispatch, NI design choices lead to a 4.5$\times$ difference in per-XPU on-chip storage budget. In grid-comparison experiments, the exploration engine uses 6-19% of the simulations required by exhaustive search. Using vLLM prefill traces with kernel times measured on GH200 GPUs, ScaleWire further guides resource provisioning under a completion-time constraint for inference execution. ScaleWire thus helps designers select NI mechanisms and provision on-chip resources to balance communication performance and resource cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kai Ma, Quanfeng Lv, Bowei Dai, Jingguo Ge, Kefan Ruan, Ruoqi Li
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
