---
title: "Introducing Cluster Efficiency to LLM Serving: Pooling Economical Accelerators over Fast Interconnects"
description: "Long-context large language model (LLM) serving places substantial demands on compute, memory capacity, and memory bandwidth."
---

**评分：48/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.02975) · [PDF](https://arxiv.org/pdf/2611.02975)

## 一句话摘要

Long-context large language model (LLM) serving places substantial demands on compute, memory capacity, and memory bandwidth.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context large language model (LLM) serving places substantial demands on compute, memory capacity, and memory bandwidth. Economical accelerators can offer these resources at lower cost, but their limited per-device capacity requires pooling across devices, making communication overhead critical. We study cluster efficiency, measured in tokens per dollar and per joule, and show how low-latency, high-bandwidth interconnects enable economical accelerators to retain their cost advantage. Guided by a characterization of coding-agent workloads and accelerator scaling, we realize this design on the Tenstorrent Galaxy, a cluster of Blackhole chips. The serving stack combines integrated communication engines, pipelined ring transfers, communication-computation overlap, and device-side decode replay to reduce collective overhead. Across three dense models in BF16 and 8-bit configurations with 8K-256K-token contexts, the Galaxy achieves 1.07-2.24$\times$ the tokens per dollar of an eight-GPU RTX PRO 6000 Blackwell server under a three-year acquisition-and-electricity cost model. Emulating TCP-class communication on the same chips reduces throughput by 23.5-67.4% and eliminates the cost advantage in every evaluated configuration. These results demonstrate how fast interconnects translate the per-dollar resource advantages of economical accelerators into cost-efficient long-context LLM serving.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Youhe Jiang, Pavle Glu\v{s}ac, Binhang Yuan, Eiko Yoneki
- 发布：2026-11-03；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
