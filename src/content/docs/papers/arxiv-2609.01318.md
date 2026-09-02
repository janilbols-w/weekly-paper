---
title: "Reliability Challenges in Diffusion Vision-Language Models"
description: "Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.01318) · [PDF](https://arxiv.org/pdf/2609.01318)

## 一句话摘要

Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation. Despite rapid progress, their reliability properties remain largely uncharacterized. We present the first systematic reliability evaluation of hallucination and bias in dLVLMs, benchmarking six diffusion models against competitive AR baselines across four dimensions. Our key findings are: (1) dLVLMs reverse the yes-bias of AR models in binary visual queries; (2) they achieve competitive hallucination rates yet exhibit degraded linguistic quality; (3) they collapse to near-zero accuracy on underrepresented racial groups with opposite-polarity gender bias; and (4) they exhibit accuracy collapse in multiple-choice settings when the correct option is shorter than its distractors, associated with a length prior that emerges at the first denoising step. Tokens committed at late denoising steps with low confidence further correlate with hallucinated content, pointing to a mechanistic signal unique to diffusion generation. These patterns vary across model families, suggesting reliability is shaped by the generative paradigm together with training data.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Md. Atabuzzaman, Chris Thomas
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
