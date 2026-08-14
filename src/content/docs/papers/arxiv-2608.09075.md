---
title: "SLAC: Access-Driven CPU-to-GPU Side-channel Attacks via System-Level Cache on Apple Silicon"
description: "Modern heterogeneous System-on-Chip designs integrate CPU cores and a GPU that share a last-level cache (LLC) or system-level cache (SLC)."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.09075) · [PDF](https://arxiv.org/pdf/2608.09075)

## 一句话摘要

Modern heterogeneous System-on-Chip designs integrate CPU cores and a GPU that share a last-level cache (LLC) or system-level cache (SLC).

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern heterogeneous System-on-Chip designs integrate CPU cores and a GPU that share a last-level cache (LLC) or system-level cache (SLC). This sharing exposes a new cross-domain attack surface, and existing attacks on integrated platforms either exploit coarse-grained cache-occupancy contention or require the adversary to co-reside on the GPU with the victim to obtain accurate timing measurements. In this work, we target Apple Silicon heterogeneous SoCs and discover that GPU memory accesses leave set-level footprints in the shared SLC, observable to an unprivileged CPU process. This keen observation enables the first fine-grained, access-driven, Prime+Probe-style CPU-to-GPU cache side-channel attacks against GPU workloads. We first reverse-engineer the Apple M1 SLC set-indexing functions and the interactions between local private caches and the SLC. Building on these findings, we construct the CPrime+CProbe SLC side-channel technique, which monitors GPU victim activity from the CPU at cache-set granularity. We then introduce an accelerated variant, GPrime+CProbe, in which an adversary leverages the GPU for faster SLC priming, yielding a 6.4x increase in the covert-channel throughput. Lastly, we demonstrate two end-to-end privacy attacks using the new side-channels: a graph-edge reconstruction attack on Graph Neural Networks (GNNs) that achieves 90% edge accuracy across five datasets, and an LLM privacy attack that recovers input keywords with up to 94.8% accuracy and model responses with up to 88.9% accuracy across TinyLlama and GPT-2 Medium models. Our results reveal a new class of microarchitectural vulnerabilities in Apple Silicon and call for secure system cache designs for heterogeneous SoCs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tianhong Xu, Saion K. Roy, Ruyi Ding, Aidong Adam Ding, Yunsi Fei
- 发布：2026-08-10；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
