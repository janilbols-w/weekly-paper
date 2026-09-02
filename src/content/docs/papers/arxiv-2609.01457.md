---
title: "Just Talk Once: Communication-Efficient Split Federated LLM Fine-Tuning on Edge Devices"
description: "Large language model (LLM) fine-tuning is increasingly shifting toward data generated on edge devices, where memory, computation, bandwidth, and connectivity constraints make conventional federated learning difficult to sustain."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.01457) · [PDF](https://arxiv.org/pdf/2609.01457)

## 一句话摘要

Large language model (LLM) fine-tuning is increasingly shifting toward data generated on edge devices, where memory, computation, bandwidth, and connectivity constraints make conventional federated learning difficult to sustain.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) fine-tuning is increasingly shifting toward data generated on edge devices, where memory, computation, bandwidth, and connectivity constraints make conventional federated learning difficult to sustain. Split federated fine-tuning (SFT) improves client-side efficiency by offloading most model parameters and computation to the server but requires step-by-step bidirectional communication loop across the split interface and forces continuous client involvement throughout training. In this paper, we present L-shaped SFT, a split fine-tuning framework that removes this bidirectional bottleneck. Our key insight is that weight tying in modern LLMs enables server-side hidden activations to be directly supervised using target embeddings, allowing the training loss to be computed on the server without returning server outputs to the client. To further eliminate the need for continuous client participation, based on L-shaped SFT, we introduce one-shot SFT, in which clients upload activations once and then go offline while the server continues optimization over cached representations. We implement our design in a real system testbed with heterogeneous edge clients, including commercial smartphones and NVIDIA developer boards. Experiments demonstrate that our schemes significantly reduce communication costs and client online time compared with existing SFT baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiaxiang Geng, Xianhao Chen, Bing Luo
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
