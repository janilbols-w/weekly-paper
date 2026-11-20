---
title: "LEDGE: An Efficient Simulator for Distributed LLM Serving on Heterogeneous Edge Devices"
description: "Evaluating distributed large language model (LLM) serving on heterogeneous edge devices requires exploring diverse model partitions, device placements, and network conditions, making repeated physical experiments costly."
---

**评分：56/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.24085) · [PDF](https://arxiv.org/pdf/2611.24085)

## 一句话摘要

Evaluating distributed large language model (LLM) serving on heterogeneous edge devices requires exploring diverse model partitions, device placements, and network conditions, making repeated physical experiments costly.

## 为什么值得关注

待编辑增强。

## 摘要原文

Evaluating distributed large language model (LLM) serving on heterogeneous edge devices requires exploring diverse model partitions, device placements, and network conditions, making repeated physical experiments costly. An efficient simulator for edge LLM serving must support diverse, fine-grained placement configurations, capture runtime behavior, and accurately predict execution times while keeping simulation overhead low. We present LEDGE, a lightweight simulator for fast, fine-grained evaluation of distributed LLM serving on heterogeneous edge devices without executing tensor operations. LEDGE constructs event graphs supporting non-uniform tensor and pipeline parallelism, estimates execution costs using reusable performance models calibrated from end-to-end measurements, and simulates shared-link contention. We evaluate LEDGE on a heterogeneous testbed of 10 Jetson and Raspberry Pi devices, covering 17 model--precision combinations across 4 LLM families. On Qwen deployments, LEDGE achieves request-level mean absolute percentage errors below 3.6% and a 135.3 times aggregate speedup over physical inference. Performance model calibrated on one LLM family yield 7.44% zero-shot end-to-end latency MAPE across three other families. Further simulations show how shared-link contention affects placement decisions and network topology constrains scaling. Across four edge environments, LEDGE completes 26,773 simulation runs in 83.8 minutes, enabling efficient exploration of deployment strategies under diverse resource conditions and serving objectives. The source code is publicly available at https://github.com/gdfwj/LEDGE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Zihao Wang, Ye Tian, Tajana Rosing, Nalini Venkatasubramanian
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/gdfwj/LEDGE](https://github.com/gdfwj/LEDGE)
- 阅读深度：metadata
