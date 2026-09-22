---
title: "Stage-Aware Communication Scheduling for Disaggregated LLM Serving"
description: "Meeting stringent Time-To-First-Token (TTFT) requirements is crucial for LLM applications."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2603.17456) · [PDF](https://arxiv.org/pdf/2603.17456)

## 一句话摘要

Meeting stringent Time-To-First-Token (TTFT) requirements is crucial for LLM applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

Meeting stringent Time-To-First-Token (TTFT) requirements is crucial for LLM applications. To improve efficiency, modern LLM serving systems adopt disaggregated architectures with diverse parallelisms, introducing complex multi-stage workflows involving reusable KV-block retrieval, collective communication, and P2D transfer. Flows from dependent stages overlap within and across requests on shared bottleneck links, making TTFT highly susceptible to network contention and necessitating stage-aware scheduling. Unfortunately, most existing works schedule flows in a stage-agnostic manner, leading to uncoordinated contention that constitutes a primary cause of SLO violations. In this paper, we present Nuska, a holistic multi-stage flow scheduling mechanism designed to maximize TTFT SLO attainment. At its core, Nuska approximates the Least-Laxity-First (LLF) scheduling policy without requiring precise knowledge of a request's remaining slack. It achieves this through a Defer-and-Promote principle implemented through a Reverse Multi-Level Queue (RMLQ) structure. By dynamically promoting task precedence as effective laxity diminishes, Nuska prioritizes flows with less laxity while preventing requests with loose SLOs from prematurely consuming network bandwidth. We implement Nuska as a pluggable module integrated into vLLM, and evaluate it on an 8-server, 32-GPU testbed as well as through large-scale simulations. Our results demonstrate that Nuska effectively outperforms state-of-the-art baselines, improving the TTFT SLO attainment by 1.2x-2.4x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yijun Sun (Hong Kong University of Science and Technology), Xudong Liao (Hong Kong University of Science and Technology), Songrun Xie (Hong Kong University of Science and Technology), Hao Chen (Shanghai Jiao Tong University), Han Tian (University of Science and Technology of China), Wenxue Li (Hong Kong University of Science and Technology), Yiming Zhang (Shanghai Jiao Tong University), Kai Chen (Hong Kong University of Science and Technology)
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
