---
title: "Omni-Diffusion-Distill: Few-Step Distillation of Unified Multimodal Diffusion Large Language Models"
description: "Unified multimodal diffusion large language models (dLLMs) offer a single architecture for both image generation and multimodal understanding, but their iterative decoding requires tens to hundreds of forward passes."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.10990) · [PDF](https://arxiv.org/pdf/2610.10990)

## 一句话摘要

Unified multimodal diffusion large language models (dLLMs) offer a single architecture for both image generation and multimodal understanding, but their iterative decoding requires tens to hundreds of forward passes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Unified multimodal diffusion large language models (dLLMs) offer a single architecture for both image generation and multimodal understanding, but their iterative decoding requires tens to hundreds of forward passes. Existing few-step distillation methods largely focus on either image generation or text generation, making it unclear how to compress a fully discrete multimodal dLLM into a single efficient student while preserving both generation and understanding. We introduce Omni-Diffusion-Distill, a unified two-stage distillation framework that retains strong generation and understanding capabilities while substantially reducing the inference cost of a unified multimodal dLLM. Omni-Diffusion-Distill aligns the distillation of both generation and understanding, for both images and text, in the discrete token space. In the first stage, the student is trained to skip decoding steps by replaying cached teacher trajectories, and in the second stage the student is refined on intermediate states along its own rollouts. We further remedy two sources of degradation in unified distillation with a pairwise collision penalty that reduces repetition under parallel text decoding, and entropy-matched guidance that prevents entropy collapse caused by fitting the sharpened teacher distribution in image generation. Omni-Diffusion-Distill achieves state-of-the-art trade-offs between decoding efficiency and generation and understanding performance for multimodal dLLMs, reducing image generation from 128 to 8 decoding steps and multimodal understanding from 512 to 64, giving 18.2x and 21.2x wall-clock speedups. Under these budgets, it scores 0.828 on GenEval and 83.0 on DPG-Bench for text-to-image generation, while reaching GPT judge scores of 20.0 on MM-Vet and 57.2 on COCO captioning (twice the teacher's 28.4 at the same steps) for multimodal understanding.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hong Huang, Chenhongyi Yang, Junzhe Sun, Animesh Sinha, Wuyang Chen, Yifan Jiang
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
