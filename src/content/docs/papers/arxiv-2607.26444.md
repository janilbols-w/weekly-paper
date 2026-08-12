---
title: "StrataCL: Fabric-Native Communication Library for Production Supernodes"
description: "Modern distributed AI workloads run across hundreds of accelerators, making communication a major bottleneck."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2607.26444) · [PDF](https://arxiv.org/pdf/2607.26444)

## 一句话摘要

Modern distributed AI workloads run across hundreds of accelerators, making communication a major bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern distributed AI workloads run across hundreds of accelerators, making communication a major bottleneck. Existing communication libraries remain largely buffer-centric because user and communication buffers are managed separately, causing redundant data copies or costly user-buffer registration. This paper presents StrataCL, a zero-redundancy and fabric-native communication library for production supernodes. StrataCL introduces registration-on-allocation to realize user-buffer direct communication, and designs communication operators with workload-balanced NPU-core partitioning and NPU-driven SDMA offloading to exploit supernode architecture features. On the Huawei CloudMatrix384, StrataCL improves collective bus bandwidth by up to 1.6x and improves MoE dispatch/combine bus bandwidth by up to 1.4x. Across three production workloads, StrataCL improves LLM inference throughput by 1.9x, reduces P99 TTFT by 2.2x, and reduces LLM and Recsys training iteration time by 1.4x and 1.3x, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tiancheng Hu, Jin Qin, Yuzheng Wang, Ke Liu, TangShengsheng Li, Sheng Wang, Zhongzhe Hu, Tianlun Hu, Wei Wang, Lijun Li, Jingbin Zhou, Xiaoming Bao, Hongwei Sun, Jieru Zhao, Huimin Cui, Tao Xie, Chenxi Wang
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
