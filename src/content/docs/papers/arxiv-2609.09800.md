---
title: "HBFSim: Fast and Faithful Simulation of High-Bandwidth Flash Under Real GPU Execution"
description: "Serving a large language model (LLM) is limited by memory capacity."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.09800) · [PDF](https://arxiv.org/pdf/2609.09800)

## 一句话摘要

Serving a large language model (LLM) is limited by memory capacity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving a large language model (LLM) is limited by memory capacity. High-Bandwidth Flash (HBF) stacks NAND flash inside the accelerator package, one tier below high-bandwidth memory (HBM); the specification was published on August 3, 2026, and the first inference devices are expected to sample in early 2027. Decisions about capacity and data placement cannot wait for silicon. No existing method settles those decisions: a storage simulator replaying a recorded access sequence never executes the workload, a GPU simulator does not run the real compute kernels, and a cycle-accurate simulator cannot finish one LLM inference run. We present HBFSim, the first evaluation platform that applies HBF timing, capacity, and thermal effects to a real inference workload while that workload executes on a real GPU. HBFSim rewrites PTX, the intermediate code NVIDIA's compiler emits, and gates kernel launches; issue is separated from consumption, so real hardware supplies the computation that hides an access. Timing comes from measurements of a real device rather than a parameter sheet, and junction temperature sets both the rate HBF sustains and the retention deadline that forces refresh writes. HBFSim matches the measured device exactly at all six calibration breakpoints, with zero unsafe launches, and an unmodified vLLM 0.15.1 serving Qwen3-30B-A3B returns the token identifiers of the uninstrumented baseline. The device fast path serves the same Qwen3-30B-A3B case in 2s against 44s on the detailed reference path, 20.8x faster. Before HBF parts sample, HBFSim lets a designer measure a capacity or placement decision under a real workload instead of assuming one.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yanpeng Hu, Yiwei Yang, Yuanwu Zhu, Yusheng Zheng, Wei Zhang, Andi Quinn
- 发布：2026-09-09；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
