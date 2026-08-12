---
title: "Progressive Semantic Communication for Efficient Edge-Cloud Vision-Language Models"
description: "Deploying Vision-Language Models (VLMs) on edge devices remains challenging due to their substantial computational and memory demands, which exceed the capabilities of resource-constrained embedded platforms."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2604.26508) · [PDF](https://arxiv.org/pdf/2604.26508)

## 一句话摘要

Deploying Vision-Language Models (VLMs) on edge devices remains challenging due to their substantial computational and memory demands, which exceed the capabilities of resource-constrained embedded platforms.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying Vision-Language Models (VLMs) on edge devices remains challenging due to their substantial computational and memory demands, which exceed the capabilities of resource-constrained embedded platforms. Conversely, fully offloading inference to the cloud is often impractical in bandwidth-limited environments, where transmitting raw visual data introduces substantial latency overhead. While recent edge-cloud collaborative architectures attempt to partition VLM workloads across devices, they typically rely on transmitting fixed-size representations, lacking adaptability to dynamic network conditions and failing to fully exploit semantic redundancy. In this paper, we propose a progressive semantic communication framework for edge-cloud VLM inference, using a Meta AutoEncoder that compresses visual tokens into adaptive, progressively refinable representations, enabling plug-and-play deployment with off-the-shelf VLMs without additional fine-tuning. This design allows flexible transmission at different information levels, providing a controllable trade-off between communication cost and semantic fidelity. We implement a full end-to-end edge-cloud system comprising an embedded NXP i.MX95 platform and a GPU server, communicating over bandwidth-constrained networks. Experimental results show that, at 1 Mbps uplink, the proposed progressive scheme significantly reduces network latency compared to full-edge and full-cloud solutions, while maintaining high semantic consistency even under high compression. The implementation code will be released upon publication at https://github.com/open-ep/ProSemComVLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Cyril Shih-Huan Hsu, Wig Yuan-Cheng Cheng, Chrysa Papagianni
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/open-ep/ProSemComVLM](https://github.com/open-ep/ProSemComVLM)
- 阅读深度：metadata
