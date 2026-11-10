---
title: "MorphSched: Workload-Aware Adaptive Scheduler Generation for Linux"
description: "Modern Linux scheduling increasingly requires workload-specific policies to meet the dynamic performance needs of heterogeneous applications."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.08509) · [PDF](https://arxiv.org/pdf/2611.08509)

## 一句话摘要

Modern Linux scheduling increasingly requires workload-specific policies to meet the dynamic performance needs of heterogeneous applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern Linux scheduling increasingly requires workload-specific policies to meet the dynamic performance needs of heterogeneous applications. The recent sched_ext framework enables custom BPF schedulers, but building practical policies still requires coordinating Rust user-space control logic, BPF scheduling callbacks, generated user-kernel interfaces, and strict eBPF verifier constraints. This paper presents MorphSched, an LLM-driven system for synthesizing complete Rust+BPF sched_ext schedulers. MorphSched profiles target workloads under Linux EEVDF to construct dynamic, workload-specific optimization objectives, and uses a scaffold-constrained generation pipeline to translate scheduling intent into deployable scheduler implementations. To improve synthesis reliability, MorphSched separates implementation repair from strategy search: verifier, build, and runtime failures are handled through a DAG-structured repair process, while performance feedback is accumulated in an evolutionary memory pool to refine high-level scheduling strategies across iterations. We evaluate MorphSched across 120 machine/workload/interferer configurations on a real Linux kernel. The generated schedulers compile, pass eBPF verification, load successfully, and remain stable throughout our benchmark runs without manual edits to generated scheduler source code. Across these configurations, MorphSched improves the primary foreground metric over EEVDF by 26.5% on average and up to 87.3%. In selected comparisons, the generated schedulers are also competitive with representative hand-written sched_ext schedulers. These results show that scaffold-constrained, system-grounded LLM generation can be a practical tool for exploring workload-specific Linux scheduling policies.

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

- taxonomy keywords: memory pool
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yifan Zhang, Hengxuan Lou, Xinkui Zhao, Rengrong Xiong, Naibo Wang, Chang Liu, Guanjie Cheng, Shuiguang Deng, Jianwei Yin
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
