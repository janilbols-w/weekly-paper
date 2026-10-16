---
title: "PAGE404: Breaking GPU Isolation Through Hardware-assisted Page Migration"
description: "NVIDIA's Grace Hopper (GH200) superchip represents a new generation of heterogeneous computing, tightly integrating a 72-core Arm-based CPU with a Hopper GPU on a single module via a high-bandwidth, cache-coherent interconnect."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.20962) · [PDF](https://arxiv.org/pdf/2610.20962)

## 一句话摘要

NVIDIA's Grace Hopper (GH200) superchip represents a new generation of heterogeneous computing, tightly integrating a 72-core Arm-based CPU with a Hopper GPU on a single module via a high-bandwidth, cache-coherent interconnect.

## 为什么值得关注

待编辑增强。

## 摘要原文

NVIDIA's Grace Hopper (GH200) superchip represents a new generation of heterogeneous computing, tightly integrating a 72-core Arm-based CPU with a Hopper GPU on a single module via a high-bandwidth, cache-coherent interconnect. By eliminating the conventional PCIe bottleneck for CPU-GPU data movement, this design establishes a unified memory domain that scales to the capacities demanded by generative AI and high-performance computing (HPC) workloads. The architecture also introduces hardware-assisted page migration: driven by access counters, the system dynamically promotes frequently accessed pages from host CPU memory to GPU DRAM to improve memory locality. We study the security of this emerging architecture against new side- and covert-channel attacks targeting its page migration support. We analyze counter-driven migration across both the hardware mechanisms and the UVM driver's interrupt-handling pipeline, and identify two side-channel vulnerabilities: one rooted in the shared structure of access counters, and the other in the driver's response to migration interrupts. We further show that both channels are exploitable across Multi-Instance GPU (MIG) partitions, a feature intended to provide strong, hardware-enforced isolation between co-located tenants. Using proof-of-concept attacks, we build covert channels that reach roughly 8,500 bits per second through eviction-based signaling and 8,100 bits per second through migration-delay-based signaling across MIG instances. The interrupt-based channel also fingerprints inference workloads across distinct large language models (LLMs) and CPU SPEC2017 benchmarks, and estimates the prompt length processed during LLM inference with high accuracy. These results expose a security gap in hardware-managed heterogeneous memory systems and call into question the isolation guarantees of current MIG-enabled multi-tenant GPU deployments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: unified memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ravan Nazaraliyev, Yicheng Zhang, Nael Abu-Ghazaleh
- 发布：2026-10-14；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
