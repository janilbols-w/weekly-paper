---
title: "When Personality Meets Quantization: A Layer-wise MBTI Analysis of Quantized LLMs"
description: "Personality is increasingly important in large language models (LLMs), as it shapes users' trust, engagement, and emotional experiences."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.25977) · [PDF](https://arxiv.org/pdf/2608.25977)

## 一句话摘要

Personality is increasingly important in large language models (LLMs), as it shapes users' trust, engagement, and emotional experiences.

## 为什么值得关注

待编辑增强。

## 摘要原文

Personality is increasingly important in large language models (LLMs), as it shapes users' trust, engagement, and emotional experiences. While the Myers--Briggs Type Indicator (MBTI) has emerged as a common framework for assessing LLMs' personality, existing studies focus primarily on full-precision models and evaluate only final outputs. They overlook the widespread deployment of quantized LLMs requiring low memory footprints, whose personality traits remain underexplored. In this work, we present a systematic MBTI analysis of open-source LLMs across multiple precisions, including mainstream 4-bit methods (GPTQ, AWQ) and extreme 2-bit settings (AQLM variants). Beyond output-level evaluation, we examine how personality emerges across layers through option-level entropy and confidence-gap dynamics, and introduce Uncertainty-Amplified Layer Decoding (UALD) to study decoding-induced personality drift at inference time. Our results reveal a key insight: LLMs' personality is not a static property, but an emergent, layer-dependent decision process sensitive to quantization, prompting, and decoding. Specifically, we find that (1) ENFJ remains dominant across model families and precisions; (2) 4-bit quantization largely preserves coarse personality structure, while 2-bit quantization disrupts fine-grained prompt consistency and cross-precision agreement; (3) personality decisions emerges in upper layers, following substantial ambiguity in early layers; and (4) inference decoding can shift personality, while personality-aligned conditioning improves robustness. These findings provide a new perspective on the behavioral reliability of quantized LLMs and highlight the importance of considering internal dynamics and inference strategies in personality-sensitive chatbot applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yao Fu, Lijia Huang, Xiaomin Li, Runchao Li, Yu Yin, Kenneth A. Loparo
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
