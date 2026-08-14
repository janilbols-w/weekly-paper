---
title: "Hidden Language Consistency Phenomena in Reasoning LLMs"
description: "Multilingual reasoning models are commonly evaluated by whether they arrive at the correct answer, but not by whether they preserve the intended language while reasoning and responding."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.08447) · [PDF](https://arxiv.org/pdf/2608.08447)

## 一句话摘要

Multilingual reasoning models are commonly evaluated by whether they arrive at the correct answer, but not by whether they preserve the intended language while reasoning and responding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multilingual reasoning models are commonly evaluated by whether they arrive at the correct answer, but not by whether they preserve the intended language while reasoning and responding. This omission conceals important multilingual behaviors that emerge as tasks become harder. In this paper, we study task difficulty, task accuracy, thinking-language consistency (TC), and answer-language consistency (AC) across reasoning models using PolyMath benchmark in eight languages and four difficulty levels. We uncover four findings: (1) language consistency exhibits four difficulty-dependent behaviors: output-language consistency remains aligned with input, remains misaligned, degrades gradually, or collapses abruptly. (2) We identify the language consistency breakdown effect, where increasing difficulty can cause a sudden drop in output-language consistency, especially in less strongly represented and non-Latin-script languages. (3) Due to this breakdown effect, accuracy can be preserved or even improved at a harder difficulty level as the model shifts to its internal dominant language. (4) Quantization can improve or degrade output-language consistency independently of its effect on accuracy, with GPTQ and AWQ often outperforming AutoRound under tolerance-based voting with {\epsilon} = 1.0. These results show that multilingual capability cannot be characterized by accuracy alone; reliable evaluation should jointly consider task accuracy, language consistency, and task difficulty for multilingual benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Muhammad Ali Shafique, Kelly Marchisio
- 发布：2026-08-09；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
