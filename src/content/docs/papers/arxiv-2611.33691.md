---
title: "L2C2: Enhancing Large-scale Chiplets for Agent Long-Context LLM Inference with Sparse and Distributed Attention"
description: "Long-context inference is a rising demand for LLMs, especially for agent applications."
---

**评分：42/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2611.33691) · [PDF](https://arxiv.org/pdf/2611.33691)

## 一句话摘要

Long-context inference is a rising demand for LLMs, especially for agent applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context inference is a rising demand for LLMs, especially for agent applications. Sparse attention (SpAt) and chiplet technology are promising solutions to reduce computations and scale hardware performance. However, deploying SpAt on distributed chiplets necessitates context parallelism for workload partitioning, introducing complex distributed attention. In this work, we present L2C2, a system optimization for distributed SpAt in long-context inference. During the partial-prefill stage, we propose a novel Split-Comm Attention mechanism that leverages the high-bandwidth interconnect of chiplets to trade communication overhead for reduced memory access. We combine it with conventional Ring Attention to form a Bi-Mode method that adapts to varying input sequence lengths. During the decoding stage, we analyze the cause of memory access imbalance and address it by static interleaved token assignment. Dynamic agile cache balancing is also proposed to adapt to SpAt skewness. Evaluations show our optimization can achieve 1.45$\times$ and 1.53$\times$ speedup in partial-prefill and decoding with SpAt on large-scale chiplets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kangbo Bai, Zhonghua Mu, Hongze Zhou, Tianyu Jia
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
