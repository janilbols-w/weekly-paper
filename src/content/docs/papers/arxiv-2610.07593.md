---
title: "TRANSIT: Transparent Scale-in for Multi-Node LLM Training"
description: "TRANSIT is a transparent scale-in framework to enable multi-node model training on fewer GPUs while maintaining training efficiency by transparently leveraging CPU DRAM as an extension of GPU memory during distributed training."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.07593) · [PDF](https://arxiv.org/pdf/2610.07593)

## 一句话摘要

TRANSIT is a transparent scale-in framework to enable multi-node model training on fewer GPUs while maintaining training efficiency by transparently leveraging CPU DRAM as an extension of GPU memory during distributed training.

## 为什么值得关注

待编辑增强。

## 摘要原文

TRANSIT is a transparent scale-in framework to enable multi-node model training on fewer GPUs while maintaining training efficiency by transparently leveraging CPU DRAM as an extension of GPU memory during distributed training. It achieves this through a user-space interposition layer, requiring no modifications to the application, training framework, cluster scheduler, device driver, or operating system. Furthermore, TRANSIT achieves higher efficiency by leveraging a zero-copy data path for CPU-GPU transfers. We evaluate TRANSIT on dense and MoE models across scales up to 64 NVIDIA H100 GPUs and multiple parallelism configurations over a RoCE network. Our evaluation shows that TRANSIT can: (a) outperform state-of-the-art framework-managed offloading techniques, achieving up to 68%, 59%, and 42% higher per-GPU throughput than TorchTitan, ZeRO-Offload, and ZeRO-Infinity, respectively, (b) enables training with 50% fewer GPUs while maintaining over 90% of baseline per-GPU throughput, (c) lower per-node network traffic by up to 33%, and (d) improve per-GPU throughput by up to 35% in communication-bound settings.

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

- taxonomy keywords: gpu memory, offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hyungyo Kim, Nicholas Satchanov, Hrishi Shah, Gaohan Ye, Jiaqi Lou, Robert Walkup, Shweta Salaria, I-Hsin Chung, Hubertus Franke, Seetharami Seelam, Apoorve Mohan, Nam Sung Kim
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
