---
title: "Animation2Code: Evaluating Temporal Visual Reasoning in Video-to-Code Generation"
description: "While recent vision-language models (VLMs) have achieved significant improvements on static visual-to-code tasks such as generating code for webpages, charts, or SVGs, it remains unclear whether they can recover temporal dynamics when motion is present."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2606.28593) · [PDF](https://arxiv.org/pdf/2606.28593)

## 一句话摘要

While recent vision-language models (VLMs) have achieved significant improvements on static visual-to-code tasks such as generating code for webpages, charts, or SVGs, it remains unclear whether they can recover temporal dynamics when motion is present.

## 为什么值得关注

待编辑增强。

## 摘要原文

While recent vision-language models (VLMs) have achieved significant improvements on static visual-to-code tasks such as generating code for webpages, charts, or SVGs, it remains unclear whether they can recover temporal dynamics when motion is present. To this end, we introduce Animation2Code, a benchmark for evaluating temporal visual reasoning via reconstructing executable web animation code from videos. Animation2Code consists of 1,069 web animation videos with diverse visual appearances and motion patterns, paired with corresponding HTML/CSS/JavaScript implementations. We propose two human-aligned metrics, appearance similarity and temporal similarity, which allow us to disentangle visual fidelity from temporal alignment when comparing rendered animations against ground-truth samples. Benchmarking state-of-the-art VLMs on this dataset shows that current VLMs struggle to maintain temporal consistency in reconstruction, even when achieving high appearance similarity, including under finetuning and iterative refinement settings. Code and data are available at https://anya-ji.github.io/animation2code-website .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anya Ji, Abhijith Varma Mudunuri, David M. Chan, Alane Suhr
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
