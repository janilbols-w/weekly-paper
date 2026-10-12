---
title: "SlackSwap: Bandwidth-Aware Activation Swapping and Recomputation for Memory-Efficient DNN Training"
description: "Swapping saved activations to host memory once enabled GPUs to train models that exceeded their device-memory capacity when compute throughput and host-link bandwidth were roughly balanced."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.13003) · [PDF](https://arxiv.org/pdf/2610.13003)

## 一句话摘要

Swapping saved activations to host memory once enabled GPUs to train models that exceeded their device-memory capacity when compute throughput and host-link bandwidth were roughly balanced.

## 为什么值得关注

待编辑增强。

## 摘要原文

Swapping saved activations to host memory once enabled GPUs to train models that exceeded their device-memory capacity when compute throughput and host-link bandwidth were roughly balanced. For example, on a 2015 Titan X, PCIe bandwidth was sufficient to offload all VGG-16 activations during the forward pass. This balance no longer holds. From the Titan X to the H100, peak training throughput increased by 141x, whereas host-link bandwidth improved by only 3.9x. On an A100, the host link can hide transfers for only 11-38% of the activations in the transformer models we study. Existing swapping approaches, such as vDNN, SuperNeurons, and SwapAdvisor, offload tensors according to memory requirements without explicitly respecting the available link-time budget, resulting in transfer-induced stalls; block checkpointing, in contrast, leaves the host link underutilized. We present SlackSwap, which treats host-link time as an explicit resource budget. Using a single profiled iteration, SlackSwap allocates the forward-pass link budget to tensors that are most expensive to recompute, resolves the remaining memory deficit by recomputing the least expensive tensors, and schedules FIFO offloads and earliest-deadline-first prefetches without per-layer synchronization barriers. In trace-driven simulations of BERT-Large, GPT-2 XL, and a Llama-7B-style model on an A100, SlackSwap retains 96-100% of unlimited-memory GPU throughput while using half the activation memory, achieving 1.10-1.11x the throughput of the best baseline. Its plans are within 0.5% of a genetic search over 6,600-14,000 candidate plans, while requiring less than 0.4 seconds to generate.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpointing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hui Feng, Xun Zhou, Yuxin Wang
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
