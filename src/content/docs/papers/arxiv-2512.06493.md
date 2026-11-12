---
title: "Programmable GPU-Accelerated dApps for Real-Time Edge Inference and ISAC on NVIDIA Aerial Testbed"
description: "The transition of cellular networks to (i) software-based systems on commodity hardware and (ii) platforms for services beyond connectivity introduces critical system-level challenges."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2512.06493) · [PDF](https://arxiv.org/pdf/2512.06493)

## 一句话摘要

The transition of cellular networks to (i) software-based systems on commodity hardware and (ii) platforms for services beyond connectivity introduces critical system-level challenges.

## 为什么值得关注

待编辑增强。

## 摘要原文

The transition of cellular networks to (i) software-based systems on commodity hardware and (ii) platforms for services beyond connectivity introduces critical system-level challenges. As sensing emerges as a key feature toward 6G standardization, supporting Integrated Sensing and Communication (ISAC) with limited bandwidth and piggybacking on communication signals, while maintaining high reliability and performance, remains a fundamental challenge. In this paper, we provide two key contributions. First, we present a programmable, open-source framework for processing PHY signals through real-time, GPU-accelerated Artificial Intelligence (AI) applications on the edge Radio Access Network (RAN) infrastructure. Building on the Open RAN dApp architecture, the framework interfaces with a GPU-accelerated gNB based on NVIDIA Aerial Testbed (ATB), feeding PHY data to custom AI logic with about 84 $\mu$s of framework latency per slot and control loops with inference in about 123 $\mu$s for lightweight TensorRT models, multiple inference engines, and support for several AI backends. We evaluate the framework on two GPU platforms, with different GPU sharing modes and an increasing number of cells and dApps. Second, we demonstrate the framework capabilities through cuSense, an indoor localization dApp that consumes uplink DMRS channel estimates, removes static multipath components, and runs a neural network to infer the position of a moving person. Evaluated on a 3GPP-compliant 5G NR deployment, cuSense achieves a mean localization error of 73 cm on runs unseen during training, with 79% of predictions falling within 1 meter, and runs live in 241 $\mu$s, without dedicated sensing hardware or modifications to the 5G signals. The framework is released as open source, together with the cuSense dataset, providing a reference design for future AI-native RANs and ISAC applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: edge inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Davide Villa, Mauro Belgiovine, Nicholas Hedberg, Michele Polese, Chris Dick, Tommaso Melodia
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
