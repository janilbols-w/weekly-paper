---
title: "KernelShift: Benchmarking Kernel Optimization Across Evolving Hardware"
description: "Efficient AI computation depends on hardware that evolves over time, shifting the strategies needed to implement performant code."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2611.29590) · [PDF](https://arxiv.org/pdf/2611.29590)

## 一句话摘要

Efficient AI computation depends on hardware that evolves over time, shifting the strategies needed to implement performant code.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficient AI computation depends on hardware that evolves over time, shifting the strategies needed to implement performant code. For CPU kernels, a key evolving factor is the set of available architectural extensions, which expose specialized hardware instructions that change the techniques used to optimize kernels. We study how effectively coding agents use these new, potentially unfamiliar extensions to write fast code. We introduce KernelShift, a benchmarking pipeline and a set of environments for evaluating coding agents in kernel optimization across evolving CPU architectures. Its agent-assisted, human-verified pipeline turns code repositories into benchmark instances, and its environments let agents optimize code with feedback from the target hardware. Using this pipeline, we construct 99 kernels from real-world, actively developed repositories (ncnn, llama.cpp, Arm SIMD Loops, and KleidiAI), including inference workloads derived from real model executions. KernelShift supports incorporating new kernels and hardware configurations as libraries and processors evolve. We evaluate agents with proprietary and open-weight models across progressively newer architectural extensions (Arm Neon, SVE, SVE2, and SME2), examining how performance changes as hardware evolves. On established extensions, agents beat the auto-vectorized compiler everywhere (2.4-19.8x) and exceed general-purpose libraries such as ncnn (getting up to 2.74x over its Neon kernels), but fall behind Arm's hand-tuned KleidiAI kernels (0.70x). In end-to-end inference of two LLMs, agent-written kernels achieve a 1.3-1.6x prefill speedup over llama.cpp's fast path. However, current agents do not yet reliably adapt to new extensions that require unfamiliar programming models, such as SME2's matrix tiles.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kernel optimization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Shuaiwei Huang, Weihua Du, Allen Wu, Ivan Fox, Manupa Karunaratne, Yiming Yang, Sean Welleck
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
