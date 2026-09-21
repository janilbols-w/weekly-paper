---
title: "HBFSim: Fast and Faithful Simulation of High-Bandwidth Flash Under Real GPU Execution"
description: "High-Bandwidth Flash (HBF) places high-capacity NAND beside HBM to relieve the memory-capacity bottleneck of LLM inference, yet its system-level behavior cannot be evaluated before hardware becomes available."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.09800) · [PDF](https://arxiv.org/pdf/2609.09800)

## 一句话摘要

High-Bandwidth Flash (HBF) places high-capacity NAND beside HBM to relieve the memory-capacity bottleneck of LLM inference, yet its system-level behavior cannot be evaluated before hardware becomes available.

## 为什么值得关注

待编辑增强。

## 摘要原文

High-Bandwidth Flash (HBF) places high-capacity NAND beside HBM to relieve the memory-capacity bottleneck of LLM inference, yet its system-level behavior cannot be evaluated before hardware becomes available. Cycle-level GPU simulators are too slow for production-scale models. Trace replay has a further shortcoming: it cannot capture the allocation, migration, and execution changes induced by different HBM-HBF configurations. Our key insight is that HBF need not be evaluated by simulating the GPU: only the program-visible effects of HBF need to be modeled. And only a real LLM workload running on real hardware can answer the arguments about HBF. Hence the modeled service has to be injected into that running program, and the injection must not destroy the GPU concurrency that would hide the original I/O latency. We present HBFSim, an open-source HBF simulator that executes LLM workloads on a real GPU while modeling HBF timing, thermal, and other behaviors online. HBFSim rewrites the PTX of the workload's kernels and routes accesses inside a registered address range into the HBF simulator. It supports asynchronous TMA transfers and capacities beyond physical GPU memory. HBFSim leaves the model's run unaffected across ordinary-memory, TMA, and capacity-mode tests. The delay it injects matches the delay requested to within 0.152%. We also design a coupled thermal module that puts HBF, HBM, and the GPU in one advanced package, which is important for answering how severe the hot throttling problem becomes after HBF runs for a long time. Experiments with Qwen3-30B show how package heating, HBM-HBF allocation, and shared MoE demand jointly constrain the design space of future HBF accelerators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yanpeng Hu, Yiwei Yang, Yuanwu Zhu, Yusheng Zheng, Wei Zhang, Andi Quinn
- 发布：2026-09-09；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
