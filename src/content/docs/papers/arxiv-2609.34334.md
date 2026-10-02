---
title: "HOCCL: Offloading Collective Communication from GPU Cores to Accelerate Distributed Training"
description: "Large language model training involves massive computation on GPU streaming multiprocessors (SMs), the primary compute units of GPUs."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](http://arxiv.org/abs/2609.34334v1) · [PDF](https://arxiv.org/pdf/2609.34334v1)

## 一句话摘要

Large language model training involves massive computation on GPU streaming multiprocessors (SMs), the primary compute units of GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model training involves massive computation on GPU streaming multiprocessors (SMs), the primary compute units of GPUs. Since SMs host specialized accelerators such as Tensor Cores, their efficient utilization is critical to training efficiency. Unfortunately, existing collective communication systems compete with computation for SMs, as they consume SMs for communication-related data movement and synchronization operations. We observe that communication can, in principle, be driven by DMA engines, thereby eliminating SM involvement in communication. Based on this insight, we propose HOCCL, a zero-SM collective communication framework consisting of three components: a stream manager, a point-to-point (P2P) executor, and a collective scheduler. The stream manager preserves operator-level temporal ordering with other GPU kernels. The P2P executor enables zero-SM point-to-point communication, while the collective scheduler orchestrates P2P transfers to maximize bandwidth. Experiments show that HOCCL preserves near-peak communication performance, achieving within 3% of the state of the art on average, while eliminating communication occupancy on nearly 10% of total GPU SMs. By freeing SM resources for computation, HOCCL improves end-to-end training throughput by up to 5%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yao Fei, Gongming Zhao, Hongli Xu, Jin Fang, Jiacheng Zhu, Shuo Xu, Kun Huang, Zhuolong Yu
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
