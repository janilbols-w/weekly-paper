---
title: "Mutable Inference: Architecting LLM Accelerators for Inference-Time Learning"
description: "Long-context LLMs must retain growing histories, but full attention makes each new token increasingly expensive."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.18523) · [PDF](https://arxiv.org/pdf/2611.18523)

## 一句话摘要

Long-context LLMs must retain growing histories, but full attention makes each new token increasingly expensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLMs must retain growing histories, but full attention makes each new token increasingly expensive. Inference-time learning (ITL) offers another approach. The model keeps training on the context during inference, retaining what it learns in its weights. Recent work shows that ITL can match full-context attention quality while attending only to a recent fixed-size window. This bounds attention costs but adds Learning (backward computation and weight updates) alongside Prediction (the forward pass) costs. Inference accelerators assume fixed weights, while training accelerators target complete training steps. This work identifies two opportunities. Attention's non-matrix operations leave enough idle matrix capacity for Learning, while selected layers can tolerate delayed weight updates with little quality loss. We exploit both with Learning While Serving (LWS), an inference accelerator architecture that shares compute hardware between latency-critical Prediction and deadline-flexible Learning. Hardware-managed per-layer weight versioning allows Learning to publish updates while in-flight computations read older versions. Resumable reduction blocks let Learning kernels span fragmented idle windows and yield to Prediction, while dedicated softmax-gradient units relieve vector contention. On modeled datacenter and edge NPUs, LWS hides Learning within Prediction, sustaining Prediction-only throughput while preserving 99.3% of fully fresh Learning's quality benefit for TTT-E2E 3B at 128K tokens. Across nine models, LWS achieves 1.6x the throughput of serial execution and 1.3x that of the best prior co-execution architecture. RTL synthesis shows that LWS adds 1.5% to NPU core area without another MAC array. By efficiently turning idle inference capacity into learning capacity, LWS establishes inference-time learning as a first-class workload for future LLM accelerators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yimin Gao, Liangtao Dai, Melika Morsali, Junting Huo, Mircea Stan
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
