---
title: "NeuroPrefetcher: Storage-Aware Sparse LLM Inference via Delta Prefetching"
description: "Deploying large language models on edge devices is increasingly limited by a widening gap between model size and available memory."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.22643) · [PDF](https://arxiv.org/pdf/2608.22643)

## 一句话摘要

Deploying large language models on edge devices is increasingly limited by a widening gap between model size and available memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying large language models on edge devices is increasingly limited by a widening gap between model size and available memory. Existing approaches such as quantization, smaller models, and offloading can raise the effective memory limit, but they still assume that the model can be compressed or partitioned to fit within some budget. We target the harder model-exceeds-memory setting, in which the model remains larger than resident memory throughout execution and storage becomes an active source of weights on the critical path. We observe that MLP activity during autoregressive decoding has strong temporal locality: approximately 82-85% of active neurons persist from one token to the next. This means that most sparse weights needed for the current token are already resident, and only the newly needed rows must be fetched from storage. We present NeuroPrefetcher, a storage-backed LLM inference system that exploits this property through predictive delta prefetching. After layer 0, a single GPU-resident predictor, occupying 2.86% of base model parameters, predicts sparse activity for all downstream MLP layers in one forward pass. The runtime compares these predictions against resident GPU buffers and issues application-scheduled NVMe reads only for incoming delta rows, replacing reactive operating-system demand paging with explicit, model-aware weight movement. On real unified-memory edge hardware, NeuroPrefetcher achieves 7.9-12.0x speedup over llama.cpp across constrained memory budgets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Nobel Dhar, Md Romyull Islam, Xuechen Zhang, Gongjin Sun, Sahidul Islam, Bobin Deng, Kun Suo
- 发布：2026-08-23；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/nobeldhar/NeuroPrefetcher](https://github.com/nobeldhar/NeuroPrefetcher)
- 阅读深度：metadata
