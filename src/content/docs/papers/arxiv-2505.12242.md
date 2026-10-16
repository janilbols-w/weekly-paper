---
title: "ZenFlow: Enabling Stall-Free Offloading for LLM Training"
description: "Fine-tuning large language models (LLMs) often exceeds GPU memory limits, prompting systems to offload model states to CPU memory."
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2505.12242) · [PDF](https://arxiv.org/pdf/2505.12242)

## 一句话摘要

Fine-tuning large language models (LLMs) often exceeds GPU memory limits, prompting systems to offload model states to CPU memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fine-tuning large language models (LLMs) often exceeds GPU memory limits, prompting systems to offload model states to CPU memory. However, existing offloaded training frameworks like ZeRO-Offload treat all parameters equally and update the full model on the CPU, causing severe GPU stalls, where fast, expensive GPUs sit idle, waiting for slow CPU updates and limited-bandwidth PCIe transfers. We present ZenFlow, a new offloaded training framework that decouples updates between GPU and CPU by prioritizing important gradients. ZenFlow performs in-place updates of important gradients on GPU while offloading and accumulating less important ones on CPU without blocking training iterations, fully overlapping CPU work with GPU computation. To make this importance-aware design scalable, ZenFlow leverages a novel spatio-temporal locality of important gradients, concentrated in specific positions that remain stable across iterations, to make important gradient identification efficient and lightweight while preserving fidelity. Evaluation shows that ZenFlow achieves up to 5x end-to-end speedup, 2x lower PCIe traffic, 85% less GPU stalls, and up to 72% lower cloud GPU cost, all while preserving accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tingfeng Lan, Yusen Wu, Bin Ma, Zhaoyuan Su, Rui Yang, Tekin Bicer, Masahiro Tanaka, Olatunji Ruwase, Dong Li, Yue Cheng
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
