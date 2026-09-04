---
title: "AdaVLA: Adaptive Step Flow Matching for Training-free Acceleration of Vision-Language-Action Models"
description: "Vision-Language-Action (VLA) models, built upon Vision-Language Models (VLMs), have significantly enhanced robotic capabilities by leveraging internet-scale knowledge and multimodal reasoning."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.29208) · [PDF](https://arxiv.org/pdf/2608.29208)

## 一句话摘要

Vision-Language-Action (VLA) models, built upon Vision-Language Models (VLMs), have significantly enhanced robotic capabilities by leveraging internet-scale knowledge and multimodal reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-Language-Action (VLA) models, built upon Vision-Language Models (VLMs), have significantly enhanced robotic capabilities by leveraging internet-scale knowledge and multimodal reasoning. However, the intensive computational overhead of VLAs constrains on-device deployment, hindering real-time responses to environmental changes. While various acceleration techniques have been proposed, they often rely on fine-tuning or access to training datasets, which are frequently unavailable due to privacy and proprietary concerns. Moreover, although flow-matching-based VLAs have emerged as efficient alternatives to standard diffusion models, current acceleration efforts largely target VLM inference costs, failing to address the iterative ODE solving process inherent in flow matching inference. To address these limitations, we propose AdaVLA, an online, training-free adaptive framework for fast yet accurate flow-matching-based Vision-Language-Action models. We introduce a novel metric derived from the flow matching trajectory curvature to quantify action generation confidence during inference. This metric enables the dynamic reduction of inference steps and the adaptive adjustment of MLP pruning ratios through an efficiently computed importance evaluation, requiring no access to training data. Experimental results on the LIBERO benchmark using a Jetson AGX Orin device demonstrate that our method achieves $1.87\times$ and $2.24\times$ speedups for $\pi_{0.5}$ and X-VLA, respectively, with negligible degradation in success rates. Furthermore, we validate the robustness of our approach on real-world robotic tasks using SmolVLA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sunghwan Han, Youngtae Han, Youngmin Yi
- 发布：2026-08-29；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
