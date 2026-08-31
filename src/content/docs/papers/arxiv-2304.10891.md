---
title: "Transformer-Based Autonomous Driving Models and Deployment-Oriented Compression: A Survey"
description: "Transformer-based models are becoming a central paradigm in autonomous driving because they can capture long-range spatial dependencies, multi-agent interactions, and multimodal context across perception, prediction, and planning."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2304.10891) · [PDF](https://arxiv.org/pdf/2304.10891)

## 一句话摘要

Transformer-based models are becoming a central paradigm in autonomous driving because they can capture long-range spatial dependencies, multi-agent interactions, and multimodal context across perception, prediction, and planning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer-based models are becoming a central paradigm in autonomous driving because they can capture long-range spatial dependencies, multi-agent interactions, and multimodal context across perception, prediction, and planning. At the same time, their deployment in real vehicles remains difficult because high-capacity attention-based architectures impose substantial latency, memory, and energy overhead. This survey reviews representative Transformer-based autonomous driving models and organizes them by task role, sensing configuration, and architectural design. More importantly, it examines these models from a deployment-oriented perspective and analyzes how efficiency constraints reshape model design choices in practice. We further review compression and acceleration strategies relevant to Transformer-based driving systems, including quantization, pruning, knowledge distillation, low-rank approximation, and efficient attention, and discuss their benefits, limitations, and task-dependent applicability. Rather than treating compression as an isolated post-processing step, we highlight it as a system-level design consideration that directly affects deployability, robustness, and safety. Finally, we identify open challenges and future research directions toward standardized, safety-aware, and hardware-conscious evaluation of efficient autonomous driving systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Juan Zhong, Yuhang Shi, Zukang Xu, Xi Chen
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
