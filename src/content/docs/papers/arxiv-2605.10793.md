---
title: "ConQuR: Corner Aligned Activation Quantization via Optimized Rotations for LLMs"
description: "Large language models (LLMs) are costly to deploy due to their large memory footprint and high inference cost."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.10793) · [PDF](https://arxiv.org/pdf/2605.10793)

## 一句话摘要

Large language models (LLMs) are costly to deploy due to their large memory footprint and high inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are costly to deploy due to their large memory footprint and high inference cost. Weight-activation quantization can reduce these costs, but low-bit activation quantization remains difficult because activation outliers induce large quantization error. Recent rotation-based methods address this by applying orthogonal transformations that redistribute activation magnitude across dimensions, but existing approaches either require expensive end-to-end rotation training or rely on stored activation corpora, introducing significant compute or storage overhead. We propose a lightweight post-training rotation calibration method for LLM activation quantization. Our method learns orthogonal rotations that align normalized activations with the corners of an inscribed hypercube, encouraging activation energy to be distributed more evenly across dimensions. This objective admits an efficient closed-form update via the orthogonal Procrustes problem, avoiding gradient-based optimization over the orthogonal group. We further introduce an online calibration procedure that updates rotations as calibration samples are processed, eliminating the need to store activations on disk and allowing rotations to adapt to quantized activation distributions during calibration. Experiments on Llama-2 and Llama-3 models from 3B to 70B parameters show that our method achieves competitive or improved performance across perplexity benchmarks and common sense reasoning tasks while avoiding both costly end-to-end training and large offline activation storage.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chayne Thrash, Ali Abbasi, Soheil Kolouri
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
