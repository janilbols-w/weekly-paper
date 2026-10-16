---
title: "Bias Mitigation in Audio-Enabled LLMs through Adversarial Training and Distillation Methods"
description: "Audio-enabled large language models (AuLLMs) allow users to interact with them simply by talking to them, without the need for an intermediate transcription."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.21763) · [PDF](https://arxiv.org/pdf/2610.21763)

## 一句话摘要

Audio-enabled large language models (AuLLMs) allow users to interact with them simply by talking to them, without the need for an intermediate transcription.

## 为什么值得关注

待编辑增强。

## 摘要原文

Audio-enabled large language models (AuLLMs) allow users to interact with them simply by talking to them, without the need for an intermediate transcription. This expands the model's accessibility and capabilities by encoding non-verbal cues. However, using non-verbal cues may lead to biased behaviour based on the attributes inferred (or assumed) from them. In this work, we focus on the gender attribute and show that models' perception of it can be unlearned using adversarial methods without a loss in performance on other benchmarked tasks. Such models are useful in situations where gender inference is unwanted. However, in other practical settings, gender perception (without bias) may be desired.As a less radical measure, we distil the gender-agnostic model, creating a model that perceives gender but responds similarly to the gender-agnostic teacher, unless explicitly asked.We apply our newly proposed methods to three AuLLMs and obtain satisfactory results in the gender-unlearning part and partially satisfactory results in the distilling part.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Adnan Al Ali, Jindřich Libovický, Anne Lauscher
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
