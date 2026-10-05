---
title: "FastKernels: Benchmarking GPU Kernel Generation in Production"
description: "LLM-based agents for GPU kernel generation are advancing rapidly, but the benchmarks they optimize against evaluate kernels in isolation, with synthetic inputs and weak baselines, rewarding sandbox speedups that break or vanish in real inference systems."
---

**评分：56/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2605.23215) · [PDF](https://arxiv.org/pdf/2605.23215)

## 一句话摘要

LLM-based agents for GPU kernel generation are advancing rapidly, but the benchmarks they optimize against evaluate kernels in isolation, with synthetic inputs and weak baselines, rewarding sandbox speedups that break or vanish in real inference systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-based agents for GPU kernel generation are advancing rapidly, but the benchmarks they optimize against evaluate kernels in isolation, with synthetic inputs and weak baselines, rewarding sandbox speedups that break or vanish in real inference systems. We introduce FastKernels, a benchmark of 384 tasks drawn from 47 representative architectures across 8 categories, whose kernels suffice to reimplement 94.6% (472/499) of HuggingFace Transformers architectures with outputs matching the native implementations. Each task mirrors the interface of the corresponding production module and is scored against the kernels production frameworks ship, and tasks form a compositional hierarchy, from primitives to full models, in which higher-level modules import lower-level ones. Candidates are scored at the kernel level and end to end inside the models they come from, on the production execution path, and MacroEval aggregates calibrated correctness, coverage, and speedup into a leaderboard. Seeding it with five representative agents (6,900 agent-hours), we find that kernel-level speedups of $1.6$-$6.6\times$ shrink to at most $1.25\times$ end to end, only 20% of winning kernel sets run correctly as-is, and kernel-level scores mis-rank agents: Claude Code matches or beats KDA at every level in isolation, yet KDA scores $3\times$ higher end to end. Code is available at https://github.com/Snowflake-AI-Research/fastkernels.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Gabriele Oliaro, Jaeseong Lee, Yichao Fu, Zhaoyuan Su, Owen Lu, Sreeram Vennam, May Jiang, Junli Wang, Hao Zhang, Zhihao Jia, Samyam Rajbhandari
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Snowflake-AI-Research/fastkernels](https://github.com/Snowflake-AI-Research/fastkernels)
- 阅读深度：metadata
