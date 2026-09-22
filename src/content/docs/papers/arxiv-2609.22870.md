---
title: "Towards Full Pipeline FP8 Reinforcement Learning for LLMs"
description: "Reinforcement learning (RL) has become a key technique for improving the reasoning and agentic abilities of large language models (LLMs)."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.22870) · [PDF](https://arxiv.org/pdf/2609.22870)

## 一句话摘要

Reinforcement learning (RL) has become a key technique for improving the reasoning and agentic abilities of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) has become a key technique for improving the reasoning and agentic abilities of large language models (LLMs). Although FP8 quantization can accelerate RL training, maintaining stability throughout an FP8 RL pipeline remains challenging. While previous works have focused on resolving train-inference mismatches using correction techniques like TIS, we reveal that full-pipeline FP8 RL still suffers from severe training instability, manifesting as anomalous mid-training entropy surges and garbled outputs. We trace this instability to a previously overlooked cause: compounded FP8 quantization noise distorts the importance ratio, disproportionately pushing negative-advantage tokens outside the trust region and erroneously zeroing out their gradients. As a result, pathological outputs are not properly penalized and accumulate over the course of training. To address this, we propose Calibrated Clipping, a dynamic method that aligns the FP8 clipping bounds with high-precision BF16 distributions by matching the lower-bound clipping quantile and rebalancing the upper bound accordingly. Extensive experiments across GRPO and DAPO algorithms, model scales from 8B to 32B, and multiple FP8 scaling granularities demonstrate that our approach successfully eliminates entropy surges and restores performance comparable to the BF16 baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fanchao Chen, Ziheng Jiang, Ziyun Wei, Zheng Zhong, Du Li, Chi Zhang, Haibin Lin, Shivaram Venkataraman
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
