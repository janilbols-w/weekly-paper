---
title: "Visual Information-Guided Parallel Decoding for Diffusion Multimodal Large Language Models"
description: "Diffusion multimodal large language models (dMLLMs) have recently emerged as a new decoding paradigm for multimodal generation."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.26580) · [PDF](https://arxiv.org/pdf/2608.26580)

## 一句话摘要

Diffusion multimodal large language models (dMLLMs) have recently emerged as a new decoding paradigm for multimodal generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion multimodal large language models (dMLLMs) have recently emerged as a new decoding paradigm for multimodal generation. Starting from a fully masked sequence, dMLLMs progressively decode the sequence by unmasking a subset of the remaining masked positions at each step. Since the selected tokens serve as the prediction context for subsequent steps, deciding which tokens to decode is crucial to the quality of the final output. The most common strategy prioritizes tokens based on a certainty measure that tends to favor tokens frequently observed in the training data. Recent approaches instead order tokens according to their influence on subsequent predictions, but do not explicitly account for the input image. We propose the Visual Information-Guided Sampler (VIG-Sampler), which prioritizes tokens based on their attention to image tokens. We further impose a constraint that penalizes candidate tokens whose image-attention distributions are similar to those of previously selected tokens, thereby increasing the information gain of the decoded subset. Extensive experiments on 7 captioning and VQA benchmarks with 3 open-source dMLLMs demonstrate the effectiveness of VIG-Sampler, which outperforms the Info-Gain Sampler by an average of 19.3 CIDEr points across the captioning benchmarks and surpasses it on COCO Caption while using only half as many decoding steps.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Insu Lee, Wooje Park, Wonseok Shin, Jinwoo Son, Byonghyo Shim
- 发布：2026-08-27；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
