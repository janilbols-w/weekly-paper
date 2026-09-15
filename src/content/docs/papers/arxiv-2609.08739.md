---
title: "Tools-CC-Bench: a Benchmark Suite for Collective Communication with Compression in HPC and AI Workloads"
description: "Distributed HPC and LLM workloads increasingly require efficient communication for scalability, yet growing data movement has become a major performance bottleneck."
---

**评分：52/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2609.08739) · [PDF](https://arxiv.org/pdf/2609.08739)

## 一句话摘要

Distributed HPC and LLM workloads increasingly require efficient communication for scalability, yet growing data movement has become a major performance bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed HPC and LLM workloads increasingly require efficient communication for scalability, yet growing data movement has become a major performance bottleneck. Communication compression can reduce this overhead and complement execution-level optimizations, but its benefits remain difficult to assess because existing benchmarks lack support for diverse backends, realistic datasets, application-specific accuracy metrics, and overlap-induced resource contention. We present CC-Bench, a lightweight, extensible, and application-oriented benchmark suite for evaluating communication compression under realistic execution conditions. CC-Bench uses declarative application-environment modeling to decouple profiling logic from communication libraries, datasets, and fidelity metrics, enabling portable cross-library evaluation. It further combines function-level interception and hardware counter monitoring to characterize per-phase latency, hardware utilization, numerical fidelity, and computation interference. With representative datasets from HPC and LLM workloads, CC-Bench evaluates three compression-enabled communication libraries on CPU and GPU clusters, revealing accuracy-performance trade-offs and bottlenecks to guide practical deployment and optimization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 15 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: collective communication
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haozhe Fan (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China), Wei Wang (School of Computer Science, Nanjing University, Nanjing, China), Xingchen Liu (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China), Man Liu (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China), Xingjian Tian (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China), Haoquan Long (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China), Zedong Liu (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China), Daran Sun (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China), Jinwu Yang (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China), Bo Yang (College of Computer Science and Technology, National University of Defense Technology, Changsha, China), Jie Liu (College of Computer Science and Technology, National University of Defense Technology, Changsha, China), Yonggang Che (College of Computer Science and Technology, National University of Defense Technology, Changsha, China), Hairui Zhao (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China), Guangming Tan (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China), Dingwen Tao (Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China)
- 发布：2026-09-09；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
