---
title: "AIR-LLM: Broadcasting AI Weights over Radio for Memory-Free Edge LLM Inference via RF Computing"
description: "Next-generation large language models (LLMs) are expanding from the cloud to ubiquitous edge devices."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.00465) · [PDF](https://arxiv.org/pdf/2610.00465)

## 一句话摘要

Next-generation large language models (LLMs) are expanding from the cloud to ubiquitous edge devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Next-generation large language models (LLMs) are expanding from the cloud to ubiquitous edge devices. However, edge devices typically either lack the memory to store increasingly large LLM weights or, even with enough memory, spend unaffordable energy on loading the weights. This raises our question: can an edge device run an LLM without storing or loading its weights, but receive them over the air and consume them on the fly? Inspired by wireless broadcasting, we present AIR-LLM, an LLM inference architecture for edge devices, which is composed of: (i) a central radio (e.g., 5G base stations) that broadcasts the LLM weights into the air, and (ii) the edge user that receives the weights and completes the general matrix-vector multiplication (GEMV) of LLM inference directly in the radio frequency (RF) domain using RF mixers. To further shorten the airtime, AIR-LLM exploits MIMO spatial multiplexing and proposes an energy-efficient precoder-postcoder pair on the edge to calibrate its own wireless channel. Since the central radio stays user-unaware, AIR-LLM is user-scalable so that one broadcast serves unlimited users within its coverage. We implement AIR-LLM on the NVIDIA Sionna ray-traced channels of two real-world urban scenes and the profiling of a real RF mixer. With a WikiText-2 perplexity degradation of 4.0% on LLaMA-3.1-8B, AIR-LLM saves the energy by 157.7x/40.4x against the FP16 and weight-only quantization baselines; with 20 users, its airtime is 104.1x/26.0x shorter, respectively.

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

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhihui Gao, Tingjun Chen, Dirk Englund
- 发布：2026-09-30；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
