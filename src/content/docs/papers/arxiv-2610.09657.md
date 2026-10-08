---
title: "Fast and Memory Efficient Offload Training Framework with Hybrid XPU Computation"
description: "With the ever-growing size of deep learning models, GPU memory is prone to being insufficient during training."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.09657) · [PDF](https://arxiv.org/pdf/2610.09657)

## 一句话摘要

With the ever-growing size of deep learning models, GPU memory is prone to being insufficient during training.

## 为什么值得关注

待编辑增强。

## 摘要原文

With the ever-growing size of deep learning models, GPU memory is prone to being insufficient during training. A prominent approach is ZeRO-Offload, which moves the optimizer states to CPU memory and performs parameter update using CPU. However, the deficiencies of ZeRO-Offload include low GPU utilization, imperfect overlapping of communication and computation, and inflexible offloading. In this paper, we leverage Direct Host Access (DHA) on the GPU that can compute data in CPU memory, forming a novel hybrid on-GPU and DHA. We design and implement MemFerry consisting of an execution scheduler and a shadow model. The scheduler strategically chooses layers of parameters for DHA computation and transmits the remaining parameters to GPU memory simultaneously to shorten forward propagation time, and further loads DHA parameters to GPU memory to reduce backward propagation time. The shadow model presents a unified memory abstraction for the parameter partitions stored separately in GPU and CPU memories. To further reduce GPU memory usage, we present MemFerry along with its dynamic programming algorithm that offloads gradients to CPU memory via DHA. We further extend MemFerry to emerging scale-up domains with ScaleUp-MemFerry, which exploits otherwise underutilized accelerator interconnect bandwidth to assist host-to-accelerator data movement through adaptive multi-path transfer. Our experiments show that \system trains up to $1.68\times$ faster and MemFerry can train $1.52\times$ larger model compared to ZeRO-Offload on a single GPU, and increase training speed by at least $28.1\%$ when scaling to data parallelism on 8 GPUs. We further extend the design to a Huawei CloudMatrix384 scale-Up node with up to 8 NPUs, and our ScaleUp-MemFerry reduces the end-to-end iteration time by up to $20.7\%$ over DeepSpeed.

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

- taxonomy keywords: gpu memory, offloading, unified memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiyi Yao, Zuning Liang, Yuedong Xu, Jin Zhao, Jessie Hui Wang, Tong Li
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
