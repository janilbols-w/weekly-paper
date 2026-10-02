---
title: "EdgeDAE: Acceleration of Diffusion Action Experts for Real-Time Physical AI with Tiny VLAs on Edge FPGA-GPU Systems"
description: "Physical AI models such as Vision-Language-Action (VLA) architectures enable generalist robotic policies through large-scale transformer backbones and diffusion-based action decoders."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.00311) · [PDF](https://arxiv.org/pdf/2610.00311)

## 一句话摘要

Physical AI models such as Vision-Language-Action (VLA) architectures enable generalist robotic policies through large-scale transformer backbones and diffusion-based action decoders.

## 为什么值得关注

待编辑增强。

## 摘要原文

Physical AI models such as Vision-Language-Action (VLA) architectures enable generalist robotic policies through large-scale transformer backbones and diffusion-based action decoders. While edge GPU platforms excel at parallelizing the compute-intensive vision-transformer workloads, they exhibit fundamental limitations for the Diffusion Action Expert (DAE) module: the iterative denoising process requires repeated parameter loading from DRAM across multiple steps, resulting in memory-bound performance where the GPU's massive computational throughput remains underutilized. This mismatch between DAE's I/O-intensive characteristics and GPU's compute-centric architecture motivates a heterogeneous acceleration approach. This paper presents \textbf{EdgeDAE}, a heterogeneous FPGA-GPU system that strategically partitions workloads based on computational characteristics. We offload the perception-heavy vision-transformer to GPU while accelerating DAE inference on FPGA through complete on-chip parameter storage in BRAM/URAM. This architecture eliminates the memory bottleneck by co-designing quantization strategies, fixed-point arithmetic, and hardware-efficient random number generation for the FPGA fabric. Compared to an edge GPU baseline, EdgeDAE reduces end-to-end inference latency by 52.5\% for Octo-Small and 38.7\% for Octo-Base, with up to $2.10\times$ higher throughput; compared to a consumer GPU (RTX~4090), it achieves ${\sim}17\times$ higher energy efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiheng Chen, Ye Qiao, Mohammad Abdullah Al Faruque, Sitao Huang
- 发布：2026-09-28；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
