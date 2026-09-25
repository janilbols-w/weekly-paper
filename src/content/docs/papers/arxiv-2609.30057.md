---
title: "KREX: Concurrent Kernel Benchmarking on Shared GPUs via Region-Granular Exclusivity"
description: "LLM agents automate GPU kernel optimization by repeatedly composing candidates and measuring their duration on real GPUs."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.30057) · [PDF](https://arxiv.org/pdf/2609.30057)

## 一句话摘要

LLM agents automate GPU kernel optimization by repeatedly composing candidates and measuring their duration on real GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents automate GPU kernel optimization by repeatedly composing candidates and measuring their duration on real GPUs. Existing systems preserve measurement fidelity by reserving a GPU for an entire agent session or benchmarking command. However, this results in poor utilization because only a small fraction of command execution requires exclusive GPU access. Sharing GPUs could recover this idle capacity, but introduces contention that compromises measurement fidelity and misdirects the agent's search. We present KREX, a runtime for concurrent kernel agent benchmarking with region-granular exclusivity. KREX lets agents mark critical regions involving timing-sensitive operations within a benchmarking command. The runtime then enforces exclusivity within marked regions and allows concurrent execution outside them, achieving high throughput while preserving measurement fidelity. To enforce in-region exclusivity, KREX blocks new competing GPU submissions and drains outstanding work before freezing sibling processes and isolating CPU cores, protecting both GPU execution and the host threads that drive measurements. To maximize off-region concurrency, KREX reuses GPU contexts in persistent context processes to avoid repeated, node-wide serialized context creation. We evaluate KREX on NVIDIA and AMD GPUs. Compared with command-granular exclusivity baselines, KREX delivers up to $3.4\times$ the benchmarking throughput with a negligible p95 timing inflation of $0.30\%$, $1.58\%$, and $3.90\%$ for kernels longer than 10 ms, 1 ms, and 0.1 ms, respectively.

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

- taxonomy keywords: gpu kernel, kernel optimization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianyu Feng, Haoxuan Yu, Tianyuan Wu, Lingyun Yang, Daocheng Ying, Yuxiao Wang, Ruibo Fan, Yinghao Yu, Guodong Yang, Liping Zhang, Wei Wang
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
