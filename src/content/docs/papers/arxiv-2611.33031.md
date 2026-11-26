---
title: "Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?"
description: "We give four large language models (LLMs) of the Claude family the complete weights of a 20k-parameter CIFAR-10 CNN as text and ask them to produce a 4-bit network without tools, data or the ability to run inference."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.33031) · [PDF](https://arxiv.org/pdf/2611.33031)

## 一句话摘要

We give four large language models (LLMs) of the Claude family the complete weights of a 20k-parameter CIFAR-10 CNN as text and ask them to produce a 4-bit network without tools, data or the ability to run inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

We give four large language models (LLMs) of the Claude family the complete weights of a 20k-parameter CIFAR-10 CNN as text and ask them to produce a 4-bit network without tools, data or the ability to run inference. Standard round-to-nearest (RTN) quantization to 4 bit lowers the test accuracy from 81.4% to 60.4%. We design four evaluation protocols that differ in the input and task description given to the LLMs and analyze their responses. In the first two protocols the LLMs are given the float and the 4-bit RTN network and are told that the accuracy has dropped significantly. In the last two they receive only the float network and the task to quantize it, which tests whether they apply an optimization on their own or fall back to plain RTN. Our analysis shows that a frontier LLM can recover most of the lost accuracy. Given one answer per layer, Opus 5.5 raises the accuracy of the 4-bit network to 77.95% by balancing the rounding errors within each 3x3 kernel, reasoning over the integer weights without tools. This is 3.5 pp below the float network and 2.8 pp below AdaRound, which learns the rounding from calibration data. Given only the float network, the LLMs name error-cancelling corrections but do not apply them and fall back to plain RTN, at most with mildly clipped scales, which still lifts Fable 5.2's quantized network to 70.0%. We analyze in detail what the LLMs did and why it works. Code and prompts can be found at https://github.com/urbste/weight-space-programming-ptq

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Steffen Urban
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/urbste/weight-space-programming-ptq](https://github.com/urbste/weight-space-programming-ptq)
- 阅读深度：metadata
