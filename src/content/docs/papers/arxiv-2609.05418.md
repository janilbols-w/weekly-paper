---
title: "Benchmarking Storage Systems for Machine Learning Workloads Using NIO Bench"
description: "Machine learning training workloads place unique demands on storage systems, yet most existing benchmarks focus on computational throughput rather than file system I/O behavior."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.05418) · [PDF](https://arxiv.org/pdf/2609.05418)

## 一句话摘要

Machine learning training workloads place unique demands on storage systems, yet most existing benchmarks focus on computational throughput rather than file system I/O behavior.

## 为什么值得关注

待编辑增强。

## 摘要原文

Machine learning training workloads place unique demands on storage systems, yet most existing benchmarks focus on computational throughput rather than file system I/O behavior. We present a benchmarking framework, Neural I/O Benchmark (NIO Bench), that characterizes storage access patterns across six diverse ML model architectures: Language Transformers, Vision Transformers, Diffusion Models, Spiking Neural Networks, Artificial Neural Networks, and Reinforcement Learning. Our framework employs a two-layer tracing approach combining Python-level I/O hooks for semantic phase context with Linux strace for complete syscall coverage including DataLoader worker subprocesses. We evaluate all six models on a Nautilus Kubernetes cluster with Ceph distributed file system. Our results reveal that I/O is heavily concentrated in data preparation, model loading, and model checkpointing. We also found that training is compute-bound rather than data-bound once data is staged, and that storage access follows an extreme power law where fewer than 10% of files account for over 90% of bytes transferred, and that read tail latency from cache misses on distributed storage is the primary storage bottleneck. These findings suggest that storage systems optimized for ML should prioritize aggressive data prefetching, page cache pinning, and efficient handling of bursty checkpoint writes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint, checkpointing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jonathan W. Morris, Ionut Mistreanu, Connor Louie
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
