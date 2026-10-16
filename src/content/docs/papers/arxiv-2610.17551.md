---
title: "Capacity over TFLOPS: Memory-Centric Deployment of Large Clinical Language Models on Consumer CPUs"
description: "The dominant barrier to running large clinical language models at the point of care is not arithmetic throughput but graphics memory: consumer GPUs cap at 4-16 GB, while the working set of a 27-billion-parameter model in 4-bit precision is 17-25 GB."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.17551v1) · [PDF](https://arxiv.org/pdf/2610.17551v1)

## 一句话摘要

The dominant barrier to running large clinical language models at the point of care is not arithmetic throughput but graphics memory: consumer GPUs cap at 4-16 GB, while the working set of a 27-billion-parameter model in 4-bit precision is 17-25 GB.

## 为什么值得关注

待编辑增强。

## 摘要原文

The dominant barrier to running large clinical language models at the point of care is not arithmetic throughput but graphics memory: consumer GPUs cap at 4-16 GB, while the working set of a 27-billion-parameter model in 4-bit precision is 17-25 GB. We argue that the edge node should be treated as capacity-enabled (system RAM) rather than compute-limited (GPU VRAM), and we test this on commodity hardware. Using an INT4 build of a 27B open model as an architecture-faithful stand-in for a 27B medical model, we measure the memory footprint, inference latency, energy, and federated communication cost of a fully CPU-based pipeline driven by synthetic Fast Healthcare Interoperability Resources (FHIR) prompts. On two independent consumer machines (a desktop-class machine with 67 GB of RAM and a 6 GB GPU, and a mobile workstation with 34 GB of RAM and a 4 GB GPU) the model loads entirely into system RAM (37% and 60% utilization, respectively) while both GPUs are out-of-memory before the first step. Inference runs at overnight-batch speed (0.6-2.4 tokens/s for the 27B model), and federated fine-tuning would transmit only a 22.6 MB low-rank adapter, a 99.96% reduction over full weights. The capacity result is independent of CPU microarchitecture, RAM size, operating system, and GPU. We further identify an open, CPU- and NPU-optimized inference runtime as the natural production path for this approach, indicating a privacy-preserving and broadly deployable route for on-premises clinical AI. All data is synthetic; this is a research artifact and not a medical device.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 17 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Eli Yune, Umer Majeed, Mahesh Balan
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/balkeumlabs/LLM-on-CPU](https://github.com/balkeumlabs/LLM-on-CPU)
- 阅读深度：metadata
