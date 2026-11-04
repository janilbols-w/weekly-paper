---
title: "Dystruct: Dynamically Structured Diffusion Language Model Decoding via Bayesian Inference"
description: "Diffusion language models (DLMs) have recently emerged as a promising alternative to autoregressive models, primarily due to their ability to enable parallel decoding."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2605.09820) · [PDF](https://arxiv.org/pdf/2605.09820)

## 一句话摘要

Diffusion language models (DLMs) have recently emerged as a promising alternative to autoregressive models, primarily due to their ability to enable parallel decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (DLMs) have recently emerged as a promising alternative to autoregressive models, primarily due to their ability to enable parallel decoding. Despite this advantage, most existing DLMs rely on a fixed generation length specified prior to decoding, which restricts their flexibility in real-world applications. While a few recent works attempt to support flexible-length generation, they typically suffer from notable limitations: some require costly retraining to accommodate variable-length outputs, while others depend solely on local confidence signals during decoding. Such local criteria fail to capture the evolving structure of the sequence, often resulting in suboptimal generation quality. In this paper, we propose a training-free, Bayesian structured decoding framework that formulates flexible-length generation as a dynamic structural inference problem. Our approach formulates flexible-length generation as a dynamic structural inference problem, jointly computing the expansion length, the block boundaries, and the decoding schedule. At each window expansion step, the method integrates local uncertainty with structural signals via a unified mechanism that supports dynamic structured generation, including both flexible block expansion and block organization, while maintaining coherence. Extensive experiments across multiple benchmarks demonstrate that our approach significantly improves generation quality and flexibility over existing fixed-length and flexible-length baselines. These results highlight the advantage of Bayesian structured decoding for diffusion language model, providing a principled and efficient solution for structured text generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bian Sun, Kevin Zhai, Mubarak Shah, Zhenyi Wang
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
