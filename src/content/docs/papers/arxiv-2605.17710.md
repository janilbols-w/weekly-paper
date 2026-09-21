---
title: "Sometin Beta Pass Notin: Improving Multilingual ASR for Nigerian Languages via Knowledge Distillation"
description: "Although modern multilingual Automatic Speech Recognition (ASR) systems support several Nigerian languages, their performance consistently lags behind resource-rich languages such as English and French."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.17710) · [PDF](https://arxiv.org/pdf/2605.17710)

## 一句话摘要

Although modern multilingual Automatic Speech Recognition (ASR) systems support several Nigerian languages, their performance consistently lags behind resource-rich languages such as English and French.

## 为什么值得关注

待编辑增强。

## 摘要原文

Although modern multilingual Automatic Speech Recognition (ASR) systems support several Nigerian languages, their performance consistently lags behind resource-rich languages such as English and French. Nigerian languages present unique modelling hurdles, including acute data scarcity, inconsistent orthography, tonal diacritics, diverse accents, frequent code-switching, and localised named entities. To address these challenges, we developed a multilingual ASR framework using a two-stage distillation process. First, we employed student-teacher knowledge distillation from existing monolingual models, conditioned on robust language-specific N-gram language models. Second, we performed iterative self improvement using pseudo-labelled data to further refine accuracy. Our method significantly bridges the performance gap, achieving on average a reduction in the relative Word Error Rate (WER) of 29% over the monolingual baselines. Our models also outperform state-of-the-art multilingual models across major benchmarks, including Common Voice and FLEURS. We introduce Sometin Beta Pass Notin (SBPN), a multilingual foundational ASR model that covers Yor\`ub\'a, Hausa, Igbo, Nigerian Pidgin, and Nigerian English.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sewade Ogun
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
