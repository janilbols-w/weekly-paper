---
title: "H-Scale: Hessian-Guided Scale Refinement for NVFP4 Sub-Byte LLM Inference"
description: "The NVIDIA Blackwell architecture, with native support for the ultra-fine-grained NVFP4 format, opens new opportunities for accelerating large language model (LLM) inference."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.28113) · [PDF](https://arxiv.org/pdf/2608.28113)

## 一句话摘要

The NVIDIA Blackwell architecture, with native support for the ultra-fine-grained NVFP4 format, opens new opportunities for accelerating large language model (LLM) inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

The NVIDIA Blackwell architecture, with native support for the ultra-fine-grained NVFP4 format, opens new opportunities for accelerating large language model (LLM) inference. NVFP4's micro-block design, such as a group size of 16, offers strong representational flexibility for capturing local weight distributions and isolating outliers, but it also introduces a large and highly sensitive space of per-group scaling factors. Existing post-training quantization (PTQ) methods primarily focus on refining quantized weight values, leaving this scale-selection step underexplored. To address this gap, we propose \textbf{H-Scale}, a lightweight post-processing method for NVFP4 per-group scale refinement. Instead of minimizing plain weight reconstruction error, H-Scale selects hardware-valid group scales using a diagonal second-order proxy derived from calibration activations, thereby targeting layer output perturbation more directly. It is designed as a drop-in replacement for RTN-style scale selection in diverse NVFP4 pipelines, requires only modest offline calibration, and introduces strictly zero overhead at inference time. Under a fixed evaluation protocol, experiments on mainstream LLMs show that H-Scale generally improves a broad range of NVFP4 baselines and brings several variants closer to the BF16 reference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hao Yu, Zheng Li, Dayiheng Liu, Jianwei Zhang
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
