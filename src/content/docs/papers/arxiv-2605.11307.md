---
title: "Vision2Code: A Multi-Domain Benchmark for Evaluating Image-to-Code Generation"
description: "We study whether vision-language models (VLMs) can reconstruct structured, graphics-based images by writing executable code to generate them."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2605.11307) · [PDF](https://arxiv.org/pdf/2605.11307)

## 一句话摘要

We study whether vision-language models (VLMs) can reconstruct structured, graphics-based images by writing executable code to generate them.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study whether vision-language models (VLMs) can reconstruct structured, graphics-based images by writing executable code to generate them. Existing benchmarks on image-to-code generation are generally limited in the domains they cover, rely on reference source code for evaluation, and do not provide metrics to quantify domain-specific issues. To address this, we introduce Vision2Code, a multi-domain, reference-code-free benchmark containing 539 test examples from 15 different datasets, spanning charts and plots, geometry, graphs, scientific diagrams, documents and 3D spatial scenes. Evaluation is done by executing the generated programs and comparing their rendered outputs to the source images using dataset- and domain-specific rubrics for a VLM judge. We find that the final scores obtained in this manner have substantially higher correlation with human ratings than those obtained via generic VLM rubrics or standard pixel-based, embedding-based or perceptual similarity metrics. We further demonstrate the reliability of our evaluation under repeated sampling from the VLM judges, varying rubric weights, and in the presence of controlled errors. Our results highlight the variability across domains of existing image-to-code generation models, with accuracy on charts and graphs being significantly higher than other domains. Lastly, we demonstrate the utility of our scoring method for rejection sampling of generated programs for fine-tuning, improving Qwen3.5-9B by 16% and Phi-4-MM by 28% compared to their base checkpoints. Our code and data are publicly available at https://image2code.github.io/vision2code/.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ajay Vikram Periasami, Junlin Wang, Bhuwan Dhingra
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
