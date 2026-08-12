---
title: "MoE Proxy Models for Low-Cost Failure Reproduction and Diagnosis in LLM RL Post-Training"
description: "Reinforcement learning (RL) post-training of large language models (LLMs) is computationally intensive and involves complex system pipelines with substantial debugging overhead."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.10823) · [PDF](https://arxiv.org/pdf/2608.10823)

## 一句话摘要

Reinforcement learning (RL) post-training of large language models (LLMs) is computationally intensive and involves complex system pipelines with substantial debugging overhead.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) post-training of large language models (LLMs) is computationally intensive and involves complex system pipelines with substantial debugging overhead. In practice, factors such as framework adaptation, numerical precision, and operator implementation can cause failures, including gradient overflow and loss divergence. Reproducing such failures directly on large models requires considerable time and computational resources. This paper systematically analyzes failures encountered during large-scale RL training on the Huawei Ascend platform, summarizes representative failure types, and identifies three model-side factors relevant to fault reproduction. Based on these factors, we propose a proxy-model construction method for low-cost fault investigation and auxiliary diagnosis. It employs structure-preserving, clustering-based expert pruning to select representative experts while retaining the model's backbone architecture, routing mechanism, and basic task capabilities. Our experimental results show that the proxy models reduce accelerator requirements by 50%-87.5% and achieve up to a 33.3x reduction in per-step NPU-hour cost, while preserving major training dynamics and reproducing fault responses consistent with the original models. Overall, the proxy models can serve as low-cost surrogates for fault reproduction, targeted validation, and auxiliary diagnosis in RL post-training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yikai Wang, Chuansai Zhou, Yuhang Zhou, Weiqiang Wu, Cong Wu, Yue Deng, Ben Feng, Mingming Zhu, Beirong Zhou, Zhibin Wang, Sheng Zhong, Chen Tian, Wangze Zhang
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
