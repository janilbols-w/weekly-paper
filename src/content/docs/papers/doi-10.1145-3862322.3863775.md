---
title: "MoMoVL: Modality-Aware Adaptive Compression for On-Device Sparsely-Activated Vision-Language Models"
description: "The rise of the agentic web has been accompanied by growing demand for on-device Vision-Language Models (VLMs) that perform diverse cross-modal web tasks with enhanced privacy and reduced latency."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.23695) · [PDF](https://arxiv.org/pdf/2611.23695)

## 一句话摘要

The rise of the agentic web has been accompanied by growing demand for on-device Vision-Language Models (VLMs) that perform diverse cross-modal web tasks with enhanced privacy and reduced latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rise of the agentic web has been accompanied by growing demand for on-device Vision-Language Models (VLMs) that perform diverse cross-modal web tasks with enhanced privacy and reduced latency. Mixture-of-Experts (MoE) models are widely adopted in modern VLMs for compute-efficient scalability, yet their multi-expert architecture poses deployment challenges due to substantial memory demands. Mixed-precision quantization is an effective compression technique that reduces bit-widths while adapting to the heterogeneous hardware budgets of edge devices, particularly well-suited for MoE due to its inherent structural sparsity, which causes imbalanced importance among experts. While prior work has applied quantization for efficient MoE inference at the edge, we point out that in MoE-based VLMs, the modality-specific characteristics of visual and text tokens further impact expert quantization. To address this issue, we present MoMoVL, a modality-aware adaptive compression framework for MoE-based VLMs that brings vision-language inference within reach of on-device resource budgets. Motivated by our empirical findings on modality-induced disparities across experts, MoMoVL jointly exploits the per-expert activation profile and per-modality quantization sensitivity to guide bit-width assignment. Experimental results show that MoMoVL improves the accuracy-compression trade-off relative to state-of-the-art mixed-precision baselines and reduces memory footprint by up to 15.44% with a modest drop in accuracy over its uniform-precision baseline. Our code and data are publicly available at https://github.com/sco-edge/MoMoVL.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Dongkeun Lee, Wonjun Lee
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/sco-edge/MoMoVL](https://github.com/sco-edge/MoMoVL)
- 阅读深度：metadata
