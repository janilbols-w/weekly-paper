---
title: "WiCi: Wireless GPU Computing Infrastructure"
description: "LLM inference applications are gaining significant traction."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.24204) · [PDF](https://arxiv.org/pdf/2608.24204)

## 一句话摘要

LLM inference applications are gaining significant traction.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM inference applications are gaining significant traction. The demand for inference is growing exponentially, and the GPU usage of inference is increasingly surpassing that of training. Due to the mobility penalty, edge-side inference fails to deliver satisfactory performance. Consequently, most inference service providers currently rely on cloud-based inference, which incurs substantial, not sustainable costs for enterprises, and is even increasing in the agentic paradigm. Therefore, our goal is to enable powerful computing capabilities as server-grade GPUs on mobile devices. We propose Wireless GPU Computing Infrastructure (WiCi) in this paper. Through WiCi, mobile devices can wirelessly access server-grade GPUs, running inference tasks on mobile clients but offloading GPU-related computations to a nearby GPU via WiFi. WiCi introduces a series of designs to make sure the infrastructure is scalable with different applications, compatible with different mobile devices, and has comparable performance to running on a physical GPU. We test WiCi from mobile devices and find that WiCi can reduce time to first token by up to 90%, improve the token rate by approximately 39x compared to local inference on mobile devices for the same model, and support much larger models. WiCi also achieves up to nearly 80% of the native performance of the server-grade GPU across different applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yibin Shen, Wei Li, Kaiqiang Xu, Zili Meng
- 发布：2026-08-25；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
